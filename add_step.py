import os

from FolderAndFile import (
    remove_content,
    copy_to_folder,
    replace_or_add_file,
    is_in_witignor,
)


def add_func(path, name):

    wit_path = os.path.join(path, ".wit")
    add_path = os.path.join(wit_path, "add")

    if name == ".":
        remove_content(add_path)
        result = copy_to_folder(path, add_path)
        if isinstance(result, str):
            return result
    else:
        file_path = os.path.join(path, name)
        if not os.path.isfile(file_path):
            return "error, this file is not exist"

        result = is_in_witignor(path, os.path.join(path, name))
        if isinstance(result, str):
            return result
        if result:
            replace_or_add_file(file_path, add_path)
