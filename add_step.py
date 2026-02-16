import os.path

from FolderAndFile import remove_content, copy_to_folder, replace_or_add_file, is_in_witignor


def add_func(path, name):
    # print("in add_func")
    wit_path = os.path.join(path,".wit")
    add_path = os.path.join(wit_path,"add")
    if name == ".":
        remove_content(add_path)
        copy_to_folder(path,add_path)
    else:
        file_path = os.path.join(path,name)
        if not os.path.isfile(file_path):
            return "error, this file is not exist"
        result = is_in_witignor(path,os.path.join(path,name))
        if isinstance(result, str):
            return result
        elif result:
            replace_or_add_file(file_path, add_path)



