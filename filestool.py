import os
import shutil


def check_if_file_exists(full_path, name):
    return os.path.exists(f'{full_path}\\{name}')


def read_exist_file(full_path, name):
    with open(f'{full_path}\\{name}', "r") as file:
        file.read()


def create_file(full_path, name):
    with open(f'{full_path}\\{name}', "w+") as file:
        file.write("")


def edit_file_content(full_path, name, content):
    with open(f'{full_path}\\{name}', "w+") as file:
        file.write(content + " \n")


def add_content_to_file(full_path, name, content):
    with open(f'{full_path}\\{name}', "a+") as file:
        file.write(content + " \n")


def remove_file(full_path, name):
    os.remove(f'{full_path}\\{name}')


def move_file(full_path, dst_path, name):
    shutil.move(f'{full_path}\\{name}', f'{dst_path}\\{name}')


def rename_file(full_path, old_name, new_name):
    shutil.move(f'{full_path}\\{old_name}', f'{full_path}\\{new_name}')


def run_file(full_path, name):
    os.system(f'{full_path}\\{name}')


def search_on_file(full_path, name, content):
    with open(f'{full_path}\\{name}', "r") as file:
        search = file.read()
        lines = []
        for line in search.split('\n'):
            if content in line:
                lines.append(line)
        return lines


def copy_file(full_path, dst_path, origin_name, new_name):
    shutil.copy(f'{full_path}\\{origin_name}', f'{dst_path}\\{new_name}')
