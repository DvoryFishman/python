import os

from FolderAndFile import (
    remove_content,
    copy_from_commit_to_folder,
    write_number_to_file,
)


def checkout_func(path, commit_name):
    wit_path = os.path.join(path, ".wit")
    commit_path = os.path.join(wit_path, "commit")
    id_path = os.path.join(commit_path, commit_name)
    add_path = os.path.join(path, "add")
    if os.path.exists(id_path):
        remove_content(path)
        copy_from_commit_to_folder(os.path.join(id_path, "files"), path)
        remove_content(add_path)
        copy_from_commit_to_folder(path, add_path)
        write_number_to_file(
            os.path.join(commit_path, "current_id.txt"), int(commit_name) + 1
        )
    else:
        return "no exist this commit"
