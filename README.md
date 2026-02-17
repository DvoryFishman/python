# WIT - Version Control System

## תיאור הפרויקט

פרויקט זה מיישם מערכת ניהול גרסאות בסיסית בדומה ל-Git. המערכת פועלת דרך ממשק שורת פקודה (CLI) ותומכת בפקודות עיקריות כמו `init`, `add`, `commit`, `status` ו-`checkout`.

## ארכיטקטורה

הפרויקט מחולק למודולים לפי פונקציונליות:

- **`wit.py`** - ממשק ה-CLI הראשי (entry point)
- **`init_step.py`** - יצירת מאגר (.wit)
- **`add_step.py`** - הוספת קבצים לשטח staging
- **`commit_step.py`** - יצירת snapshots של קבצים
- **`checkout_step.py`** - שחזור של commit ישן
- **`status_step.py`** - הצגת סטטוס הפרויקט
- **`FolderAndFile.py`** - פונקציות עזר לעבודה עם קבצים ותיקיות

## מבנה פנימי (.wit)

```
.wit/
├── add/              # staging area
└── commit/           # ניהול commits
    ├── 1/
    │   ├── files/    # הקבצים בcommit
    │   └── describe.txt  # מסר + timestamp
    ├── 2/
    ├── id_file.txt      # מזהה הcommit הבא
    └── current_id.txt   # ה-commit הנוכחי
```

## דרישות

- Python 3.10+
- click >= 8.0.0

## התקנה

### דרך 1: התקנה מקומית (מומלצת)

```bash
pip install -e .
```

לאחר התקנה, תוכל להריץ את הפקודות בעזרת `wit` ישירות:

```bash
wit init
wit add .
wit commit "message"
wit status
wit checkout 1
```

### דרך 2: התקנת dependencies בלבד

```bash
pip install click
```

ולאחר מכן הריץ דרך Python:

```bash
python wit.py init
python wit.py add .
python wit.py commit "message"
python wit.py status
python wit.py checkout 1
```

## פקודות

### `wit init`
אתחול מאגר חדש. יוצר את תיקיית `.wit` עם תיקיות `add` ו-`commit`.

```bash
wit init
```

**פלט:**
```
Initialization completed successfully.
```

### `wit add <path>`
הוספת קובץ או ספריה לשטח ה-staging (add area).

```bash
# הוספת קובץ יחיד
wit add file.txt

# הוספת כל הקבצים (פרט ל-.wit)
wit add .
```

**פלט:**
```
Add file successfully
```

**הערות:**
- אם קובץ כלול ב-.witignore, הוא לא יתווסף.
- אם קובץ לא קיים, תקבל שגיאה.
- אם ה-.witignore חסר, תקבל הודעת שגיאה ברורה.

### `wit commit <message>`
יצירת snapshot של כל הקבצים בשטח ה-staging.

```bash
wit commit "Initial commit"
wit commit "Fixed bug in feature X"
```

**פלט:**
```
The commit worked successfully.
```

**הערות:**
- אם אין שינויים מאז ה-commit האחרון, לא ייווצר commit חדש.
- כל commit מקבל ID ייחודי, מסר, וtimestamp.

### `wit status`
הצגת סטטוס הפרויקט.

```bash
wit status
```

**פלט (דוגמה):**
```
=== Repository Status ===

Untracked files:
  file1.txt
  file2.py

Modified (not staged):
  modified.txt

Staged (not committed):
  (none)
```

**הסבר:**
- **Untracked files** - קבצים בעבודה לא בstaging
- **Modified (not staged)** - קבצים שהשתנו בעבודה אך לא staged
- **Staged (not committed)** - קבצים בstaging לא בcommit האחרון

### `wit checkout <commit_id>`
שחזור הפרויקט למצב של commit ספציפי.

```bash
wit checkout 1
wit checkout 2
```

**פלט:**
```
The checkout worked successfully
```

**הערות:**
- משחזר את כל הקבצים מה-commit שנבחר.
- משדרג את `current_id.txt` כך שה-commit הבא יהיה עם ID עוקב.

## קובץ .witignore

קובץ זה מכיל רשימה של שמות קבצים להתעלם מהם.

**דוגמה (.witignore):**
```
.DS_Store
__pycache__
*.pyc
.idea
```

**הערות:**
- חובה ש-.witignore יהיה קיים בתיקיית השורש של הפרויקט.
- אם הקובץ חסר, תקבלי הודעת שגיאה.

## דוגמאות שימוש

### מעבר שלם מ-init ל-commit

```bash
# אתחול מאגר
wit init

# הוספת כל הקבצים
wit add .

# יצירת commit ראשון
wit commit "Initial commit"

# בדיקת סטטוס
wit status

# שינוי קובץ כלשהו...
# (עדכן קובץ)

# הוספת הקבצים המשונים
wit add .

# יצירת commit שני
wit commit "Updated feature"

# חזרה לcommit הראשון
wit checkout 1

# חזרה לcommit השני
wit checkout 2
```

## טיפול בשגיאות

המערכת מספקת הודעות שגיאה משמעותיות:

- **"error, this file is not exist"** - הקובץ שניסית להוסיף לא קיים.
- **"error: .witignore.txt not found..."** - קובץ .witignore חסר.
- **"no changes in this commit"** - אין שינויים מאז ה-commit האחרון.
- **"no exist this commit"** - ה-commit שבחרת לא קיים.

## PEP8 Compliance

הקוד עוקב אחר PEP8:
- שמות משתנים בـ snake_case
- שמות פונקציות בـ snake_case
- docstrings ברור עבור פונקציות
- רווחים נכונים וייבוא מסודר

## יצירתה

הפרויקט נוצר עם:
- Click ליצירת CLI
- os וshutil לעבודה עם קבצים
- datetime עבור timestamps

## הערות וידועות

- `REPO_PATH` מוגדר כקבוע בפרויקט - ניתן לשנות אותו לנתיב שלך.
- קבצי `.pyc` וקבצי `__pycache__` נוצרים אוטומטית ויכולים להתעלם מהם.
- ה-commit IDs הם מספרים עוקבים (1, 2, 3, ...).
