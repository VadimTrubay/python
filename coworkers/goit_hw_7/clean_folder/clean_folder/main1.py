import re
import shutil
import sys
import os

from pathlib import Path


file_extension = {'archives': ['zip', 'gz', 'tar'],
                  'video': ['avi', 'mp4', 'mov', 'mkv'],
                  'audio': ['mp3', 'ogg', 'wav', 'amr'],
                  'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
                  'images': ['jpeg', 'png', 'jpg', 'svg'],
                  'others': []
                  }

name_suffics_is = set()
name_suffics_not = set()
file_archivs = []
file_video = []
file_audio = []
file_documents = []
file_images = []
file_others = []


def main1(path):
    folder_list = path_folder(path)
    make_dirs(folder_list)
    sorted_folder(path, folder_list)
    print('archives: ', *file_archivs, 'video: ', *file_video,
          'audio: ', *file_audio, 'documents: ', *file_documents,
          'images: ', *file_images, 'others: ', *file_others, sep='\n'
          )
    print()
    print('Відомі розширення файлів:', *name_suffics_is)
    print('Невідомі розширення файлів:', *name_suffics_not)
    print()
    print('FINISH SORTED')


def sorted_file(file, folder_list):   # сортує файли за розширенням та номалізує ім'я

    if file.suffix:
        name_norm = normalize(
            '.'.join(file.name.split('.')[:-1])) + file.suffix

    else:
        name_norm = normalize(file.name)

    if file.suffix[1:] in file_extension['archives']:
        name_suffics_is.add(file.suffix[1:])
        file_archivs.append(name_norm)
        move_os(file, os.path.join(folder_list[0], name_norm))
        unpuck(os.path.join(folder_list[0], name_norm), os.path.join(
            folder_list[0], name_norm.split('.')[0]))

    elif file.suffix[1:] in file_extension['video']:
        name_suffics_is.add(file.suffix[1:])
        file_video.append(name_norm)
        move_os(file, os.path.join(folder_list[1], name_norm))

    elif file.suffix[1:] in file_extension['audio']:
        name_suffics_is.add(file.suffix[1:])
        file_audio.append(name_norm)
        move_os(file, os.path.join(folder_list[2], name_norm))

    elif file.suffix[1:] in file_extension['documents']:
        name_suffics_is.add(file.suffix[1:])
        file_documents.append(name_norm)
        move_os(file, os.path.join(folder_list[3], name_norm))

    elif file.suffix[1:] in file_extension['images']:
        name_suffics_is.add(file.suffix[1:])
        file_images.append(name_norm)
        move_os(file, os.path.join(folder_list[4], name_norm))

    else:
        file_others.append(name_norm)
        move_os(file, os.path.join(folder_list[5], name_norm))
        if file.suffix:
            name_suffics_not.add(file.suffix[1:])


def sorted_folder(path, folder_list):  # """ розсортовує вміст папки path """
    p = Path(path)    # p Вказує на папку path

    for i in p.iterdir():  # ітерація по всім файлам та папкам всередині папки p

        if i.is_dir() and i.name not in file_extension:
            sorted_folder(i, folder_list)
            del_dir(i)
        if i.is_file():
            sorted_file(i, folder_list)


def path_folder(path):   # визначити шляхи до директорій
    folder_list = [os.path.join(path, 'archives'),
                   os.path.join(path, 'video'),
                   os.path.join(path, 'audio'),
                   os.path.join(path, 'documents'),
                   os.path.join(path, 'images'),
                   os.path.join(path, 'others')
                   ]
    return folder_list


def make_dirs(folder_list):  # створити директорії за шляхами з folder_list

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


def unpuck(file, extract_dir):  # розпаковка файла file в директорію extract_dir
    shutil.unpack_archive(file, extract_dir)


def del_dir(path):  # видалити директорію
    os.rmdir(path)


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    return (name.translate(TRANS))


def normalize(name):

    return re.sub(r'\W', '_', translate(name))


def start():
    path = None

    try:
        path = sys.argv[1]
        print(path)
    except:
        print("Have not argument")

    if path:
        main1(path)


if __name__ == '__main__':
    start()
