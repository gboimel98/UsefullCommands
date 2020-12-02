import os
import shutil


def check_if_file_exists(name, full_path=".\\"):
    return os.path.exists(f'{full_path}\\{name}')


def read_exist_file(name, full_path=".\\"):
    with open(f'{full_path}\\{name}', "r") as file:
        file.read()


def create_file(name, full_path=".\\"):
    with open(f'{full_path}\\{name}', "w+") as file:
        file.write("")


def edit_file_content(name, content, full_path=".\\"):
    with open(f'{full_path}\\{name}', "w+") as file:
        file.write(content + " \n")


def add_content_to_file(name, content, full_path=".\\"):
    with open(f'{full_path}\\{name}', "a+") as file:
        file.write(content + " \n")


def remove_file(name, full_path=".\\"):
    os.remove(f'{full_path}\\{name}')


def move_file(dst_path, name, full_path=".\\"):
    shutil.move(f'{full_path}\\{name}', f'{dst_path}\\{name}')


def rename_file(old_name, new_name, full_path=".\\"):
    shutil.move(f'{full_path}\\{old_name}', f'{full_path}\\{new_name}')


def run_file(name, full_path=".\\"):
    os.system(f'{full_path}\\{name}')


def search_on_file(name, content, full_path=".\\"):
    with open(f'{full_path}\\{name}', "r") as file:
        search = file.read()
        lines = []
        for line in search.split('\n'):
            if content in line:
                lines.append(line)
        return lines


def replace_on_file(name, old_content, new_content, full_path=".\\"):
    with open(f'{full_path}\\{name}', "r+") as file:
        search = file.read()
        edited_content = ""
        for line in search.split('\n'):
            if old_content in line:
                line = line.replace(old_content, new_content)
            edited_content = edited_content + line
    with open(f'{full_path}\\{name}', "r+") as file:
        file.write(edited_content)


def copy_file(dst_path, origin_name, new_name, full_path=".\\"):
    shutil.copy(f'{full_path}\\{origin_name}', f'{dst_path}\\{new_name}')
