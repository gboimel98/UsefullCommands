import os
import shutil


def read_exist_file(fullpath, name):
    with open(f'{fullpath}\\{name}', "r") as file:
        return file.read()


def create_file(fullpath, name):
    with open(f'{fullpath}\\{name}', "w+") as file:
        return file.write("")


def write_to_file(fullpath, name, content):
    with open(f'{fullpath}\\{name}', "w+") as file:
        return file.write(content)


def remove_file(fullpath, name):
    return os.remove(f'{fullpath}\\{name}')


def move_file(fullpath, dstpath, name):
    return shutil.move(f'{fullpath}\\{name}', f'{dstpath}\\{name}')


def rename_file(fullpath, oldname, newname):
    return shutil.move(f'{fullpath}\\{oldname}', f'{fullpath}\\{newname}')
