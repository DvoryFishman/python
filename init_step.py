import os

from FolderAndFile import creat_folder, write_to_id_file_initial


def init_func(path):

    error_message1 = creat_folder(path, ".wit")
    if error_message1:
        return error_message1

    wit_folder_path = os.path.join(path, ".wit")
    error_message2 = creat_folder(wit_folder_path, "add")
    if error_message2:
        return error_message2

    error_message3 = creat_folder(wit_folder_path, "commit")
    if error_message3:
        return error_message3

    commit_folder_path = os.path.join(wit_folder_path, "commit")
    write_to_id_file_initial(commit_folder_path, 'id_file.txt')
    write_to_id_file_initial(commit_folder_path, 'current_id.txt')
    return None
