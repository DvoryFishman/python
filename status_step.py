import os

from FolderAndFile import compare_directories, read_line_in_file, get_unique_files


def status_func(path):
    wit_path = os.path.join(path, ".wit")
    commit_path = os.path.join(wit_path, "commit")
    add_path = os.path.join(wit_path, "add")
    Untracked_files = get_unique_files(path, add_path)
    file_not_stage = compare_directories(path, add_path)
    prev_commit = read_line_in_file(os.path.join(commit_path,"id_file.txt"))
    prev = int(prev_commit)-1
    in_add_not_commit_file = get_unique_files(add_path,os.path.join(commit_path,str(prev)))
    not_commit_file2 = compare_directories(add_path,os.path.join(commit_path,str(prev)))
    return Untracked_files , file_not_stage , in_add_not_commit_file
    # return file_not_stage
    # return in_add_not_commit_file
    # print(not_commit_file2)

