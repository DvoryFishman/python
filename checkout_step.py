import os

from FolderAndFile import remove_content, copy_from_commit_to_folder


def checkout_func(path, commit_name):
    wit_path = os.path.join(path, ".wit")
    commit_path = os.path.join(wit_path, "commit")
    id_path = os.path.join(commit_path, commit_name)
    if os.path.exists(id_path):
        remove_content(path)
        copy_from_commit_to_folder(os.path.join(id_path, "files"),path)
    else:
        return "no exist this commit"
