import sys
import os

from pathlib import Path

from normalize import normalize
from subfunctions import path_folder, move_os, make_dirs, unpuck, del_dir 



path = None
try:
    path = sys.argv[1]
except:
    print("Have not argument")

file_extension = {'archives': ['zip', 'gz', 'tar'],
                  'video': ['avi', 'mp4', 'mov', 'mkv'],
                  'audio':['mp3', 'ogg', 'wav', 'amr'],
                  'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
                  'images': ['jpeg', 'png', 'jpg', 'svg'],
                  'others': []
                  }

def sorted_folder(path):  #""" розсортовує вміст папки path """
    p = Path(path)    # p Вказує на папку path
    
    for i in p.iterdir():    #ітерація по всім файлам та папкам всередині папки p
        
        if i.is_dir() and i.name not in file_extension:
            sorted_folder(i)
            del_dir(i)
        if i.is_file():
            sorted_file(i)

def sorted_file(file):   # сортує файли за розширенням та номалізує ім'я    
    
    if file.suffix:
        name_norm = normalize('.'.join(file.name.split('.')[:-1])) + file.suffix
                 
    else:
        name_norm = normalize(file.name)               
 
    if file.suffix[1:] in file_extension['archives']:
        name_suffics_is.add(file.suffix[1:])
        file_archivs.append(name_norm)
        move_os(file, os.path.join(folder_list[0], name_norm))
        unpuck(os.path.join(folder_list[0], name_norm), os.path.join(folder_list[0], name_norm.split('.')[0]))

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


    
if path:
    name_suffics_is = set()
    name_suffics_not = set()
    file_archivs = []
    file_video = []
    file_audio = []
    file_documents = []
    file_images = []
    file_others = []

    folder_list = path_folder(path)

    make_dirs(folder_list)
    
    sorted_folder(path)
    
    print('archives: ', *file_archivs, 'video: ', *file_video,
          'audio: ', *file_audio, 'documents: ', *file_documents,
          'images: ', *file_images, 'others: ', *file_others, sep='\n')
    print('Відомі розширення файлів:', name_suffics_is)
    print('Невідомі розширення файлів:', name_suffics_not)

else:
    print('Try again')
     



