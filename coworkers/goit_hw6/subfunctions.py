import shutil
import os

from pathlib import Path



def path_folder(path):   # визначити шляхи до директорій
    folder_list = [os.path.join(path, 'archives'),
                    os.path.join(path, 'video'),
                    os.path.join(path, 'audio'),
                    os.path.join(path,'documents'),
                    os.path.join(path, 'images'),
                    os.path.join(path, 'others')
                    ]
    return folder_list

def make_dirs(folder_list):  #створити директорії за шляхами з folder_list
       
    if not os.path.exists(folder_list[0]):
        os.mkdir(folder_list[0])
    if not os.path.exists(folder_list[1]):
        os.mkdir(folder_list[1])
    if not os.path.exists(folder_list[2]):
        os.mkdir(folder_list[2])
    if not os.path.exists(folder_list[3]):
        os.mkdir(folder_list[3])
    if not os.path.exists(folder_list[4]):
        os.mkdir(folder_list[4])
    if not os.path.exists(folder_list[5]):
        os.mkdir(folder_list[5])

def move_os(old_file, new_file):   # перенесення файлу
    os.replace(old_file, new_file)

def unpuck(file, extract_dir):   #розпаковка файла file в директорію extract_dir
    shutil.unpack_archive(file, extract_dir)



def del_dir(path):  #видалити директорію
    os.rmdir(path)

