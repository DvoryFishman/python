import os

from FolderAndFile import (
    compare_directories,
    read_line_in_file,
    get_unique_files,
)


def status_func(path):
    wit_path = os.path.join(path, ".wit")
    commit_path = os.path.join(wit_path, "commit")
    add_path = os.path.join(wit_path, "add")

    untracked_files = get_unique_files(path, add_path)
    modified_not_staged = compare_directories(path, add_path)

    prev_commit = read_line_in_file(os.path.join(commit_path, "current_id.txt"))
    prev = int(prev_commit) - 1

    staged_not_committed = get_unique_files(add_path, os.path.join(commit_path, str(prev)))

    return untracked_files, modified_not_staged, staged_not_committed
