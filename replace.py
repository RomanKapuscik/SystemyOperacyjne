"""
Created on Sat April 09.03.2024
"""
import os.path
import sys
from datetime import datetime

path_to_file: str
searched_world: str
world_replace: str

try:
    path_to_file = sys.argv[1]
    searched_world = sys.argv[2]
    world_replace = sys.argv[3]
except IndexError:
    print("""To call the function with parameters from cmd add: file path
    , search world and replace world example: py -3 replace.py plik.txt old new""")
    sys.exit()


def create_backup_folder() -> str:
    """Create the backup folder for files to be changed.
    :return: the backup folder path"""
    folder_name = path_to_file.split('.')[0] + '_' + datetime.now().strftime('%Y%m%d')
    if not os.path.isdir(f'C:\\Backups\\{folder_name}'):
        os.makedirs(f'C:\\Backups\\{folder_name}')
    return f'C:\\Backups\\{folder_name}\\'


def check_how_many_files(directory: str):
    """Check how backups is already created, and if there are more than five remove the oldest one."""
    file_list = os.listdir(directory)
    file_list.sort()
    if len(file_list) > 5:
        for file_name in range(len(file_list) - 5):
            os.remove(directory + file_list[file_name])


def create_backup_file(path: str) -> str:
    """Create the backup of the file to be changed.
    :param path: path to the file to changed
    :return: path to the directory where the backup is"""
    directory = create_backup_folder()
    backup_file_name = path.split('.')[0] + '_' + datetime.now().strftime('%Y%m%d%H%M%S')
    full_path = f'{directory}/{backup_file_name}'
    try:
        with open(path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f'File "{path}" not found')
        sys.exit()

    with open(full_path, 'w', encoding='utf-8') as file:
        file.write(file_contents)

    return directory


def search_and_replace(path: str = '', search: str = '', replace: str = ''):
    """Replace searched word in the file from the path.
    :param path: path to the file to changed
    :param search: word to be replaced
    :param replace: word to be used to replace the searched word"""

    directory_for_backup = create_backup_file(path)
    check_how_many_files(directory_for_backup)

    try:
        with open(path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            updated_contents = file_contents.replace(search, replace)
    except FileNotFoundError:
        print(f'File "{path}" not found')
        sys.exit()

    with open(path, 'w', encoding='utf-8') as file:
        file.write(updated_contents)

    with open(path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    if search in file_contents:
        print('Something went wrong')
    else:
        print('All done')


try:
    search_and_replace(path=path_to_file, search=searched_world, replace=world_replace)
except AttributeError:
    print("""To call the function with parameters from cmd add: file path
    , search world and replace world example: py -3 replace.py plik.txt old new""")
    sys.exit()
