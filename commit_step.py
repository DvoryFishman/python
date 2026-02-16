import os.path
import shutil
from datetime import datetime

from FolderAndFile import creat_folder, write_number_to_file, copy_to_folder, read_line_in_file, bool_compare_folder, \
    write_describe


def commit_func(path, name_commit):
    wit_path = os.path.join(path,".wit")
    commit_path = os.path.join(wit_path, "commit")
    id_path = os.path.join(commit_path, "id_file.txt")
    text = read_line_in_file(id_path)
    num = int(text)
    prev_commit = str(num-1)
    in_prev_commit = os.path.join(commit_path, prev_commit)
    if num > 1 and bool_compare_folder(os.path.join(wit_path, "add"),os.path.join(in_prev_commit, "files") ):
       return "no changes in this commit"
    else:
       error_message1 = creat_folder(commit_path,str(num))
       if error_message1:
           return error_message1
       name_folder = os.path.join(commit_path, str(num))
       add_path = os.path.join(wit_path, "add")
       error_message2 = creat_folder(name_folder, "files")
       if error_message2:
           return error_message2
       copy_to_folder(add_path, os.path.join(name_folder, "files"))
       write_describe(name_folder,num,name_commit)
       num += 1
       write_number_to_file(id_path,str(num))


