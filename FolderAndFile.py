# coding=utf-8

import os  # noqa: F401
import shutil
import filecmp
import difflib
from datetime import datetime


def bool_equal_files(file1, file2):

    return filecmp.cmp(file1, file2)


def write_to_id_file_initial(commit_folder_path, name_file):
    with open(os.path.join(commit_folder_path, name_file), 'w') as file:
        file.write("1")

def compare_and_update_folders(folder1, folder2):
    for filename in os.listdir(folder1):
        file1_path = os.path.join(folder1, filename)
        file2_path = os.path.join(folder2, filename)

        if os.path.isfile(file2_path):
            with open(file1_path, 'r') as file1:
                file1_lines = file1.readlines()

            with open(file2_path, 'r') as file2:
                file2_lines = file2.readlines()

            diff = difflib.ndiff(file1_lines, file2_lines)
            updated_lines = [line[2:] for line in diff if line.startswith('-')]

            with open(file1_path, 'w') as file1:
                file1.writelines(updated_lines)


def bool_compare_folder(folder1, folder2):
    comparison = filecmp.dircmp(folder1, folder2)
    return not comparison.diff_files and not comparison.left_only and not comparison.right_only


def replace_or_add_file(file_path, folder_path):
    file_name = os.path.basename(file_path)
    target_file_path = os.path.join(folder_path, file_name)

    if os.path.exists(target_file_path):
        os.remove(target_file_path)
    shutil.copy(file_path, folder_path)


def creat_folder(path, directory_name):
    full_path = os.path.join(path, directory_name)
    try:
        os.makedirs(full_path)
    except FileExistsError:
        return "error, this folder already exist"
    except Exception as e:
        return str(e)


def remove_content(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.basename(item) != ".wit":
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)


def is_in_witignor(path, file):
    wit_ignor_path = os.path.join(path, ".witignor.txt")
    if not os.path.exists(wit_ignor_path):
        return f"Warning: {wit_ignor_path} does not exist."

    file_name = os.path.basename(file)
    with open(wit_ignor_path, 'r') as witignore_file:
        for line in witignore_file:
            if line.strip() and line.strip() == file_name:
                return False
    return True


def copy_to_folder(source, dest):
    for item in os.listdir(source):
        result = is_in_witignor(source, item)
        if isinstance(result, str):
            return result

        if os.path.basename(item) != ".wit" and result:
            path_item = os.path.join(source, item)
            if os.path.isdir(path_item):
                shutil.copytree(path_item, os.path.join(dest, os.path.basename(item)))
            else:
                shutil.copy2(path_item, dest)


def copy_from_commit_to_folder(source, dest):
    for item in os.listdir(source):
        path_item = os.path.join(source, item)
        if os.path.isdir(path_item):
            shutil.copytree(path_item, os.path.join(dest, os.path.basename(item)))
        else:
            shutil.copy2(path_item, dest)


def write_number_to_file(file_path, number):
    with open(file_path, 'w') as file:
        file.write(str(number))


def read_line_in_file(path):
    with open(path, 'r') as file1:
        text = file1.readline().strip()
    return text


def get_unique_files(source_folder, target_folder):
    unique_files = set()

    for item in os.listdir(source_folder):
        source_path = os.path.join(source_folder, item)
        target_path = os.path.join(target_folder, item)

        if os.path.isdir(source_path):

            if os.path.isdir(target_path):
                unique_files.update(get_unique_files(source_path, target_path))
            else:

                unique_files.update(get_unique_files(source_path, ''))
        else:

            if not os.path.exists(target_path):
                unique_files.add(item)
    unique_files.discard('.wit')
    return list(unique_files)


def compare_directories(dir1, dir2):
    identical_items = []
    differing_items = []

    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))

    common_files = files1.intersection(files2)

    for file_name in common_files:
        file1_path = os.path.join(dir1, file_name)
        file2_path = os.path.join(dir2, file_name)

        if os.path.isfile(file1_path) and os.path.isfile(file2_path):
            if os.path.splitext(file1_path)[1] == os.path.splitext(file2_path)[1]:
                if filecmp.cmp(file1_path, file2_path, shallow=False):
                    identical_items.append(file_name)
                else:
                    differing_items.append(file_name)
        else:
            if os.path.isdir(file1_path) and os.path.isdir(file2_path):
                sub_differing = compare_directories(file1_path, file2_path)
                differing_items.extend(sub_differing)

    return differing_items


def first_word(s):
    return s.split()[0] if s else None


def second_word(s):
    words = s.split()
    return words[1] if len(words) > 1 else None


def third_word(s):
    words = s.split()
    return words[2] if len(words) > 2 else None


def write_describe(name_folder, num, name_commit):
    with open(os.path.join(name_folder, "describe.txt"), 'w') as file2:
        file2.write(name_commit + "\n")
        file2.write(str(datetime.now()) + "\n")
        file2.write(str(num))