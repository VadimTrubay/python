import sys
import os
import re
import shutil
import os.path
from time import sleep


def main():
    # створюємо папки для сортування файлів
    def creat_folder(path, new_folders):

        # global path_root, dst_doc, dst_img, dst_aud, dst_vid, dst_arh, dst_un
        path_root = path

        for el in new_folders:
            try:
                os.mkdir(path_root + '\\' + el)
            except FileExistsError:
                print("File already exists:", el)
            except OSError:
                print("")

    def normalize(name):  # заміна кирилиці на латиницю
        CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ!#$%&()*+,-/:;<>=?@[]^~{|}'\\`. "
        TRANSLATION = (
            "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
            "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g",
            "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_",
            "_",
            "_", "_", "_", "_", "_", "_", "_", "_", "_")
        TRANS = {}
        CYRILLIC = tuple(CYRILLIC_SYMBOLS)

        for c, l in zip(CYRILLIC, TRANSLATION):
            TRANS[ord(c)] = l
            TRANS[ord(c.upper())] = l.upper()

        if re.search(r'\..{2,5}$', name):
            s_res = re.search(r'\..{2,5}$', name)
            suffix = s_res.group()
            name = name.removesuffix(suffix)
            name = name.translate(TRANS)
            name = name + suffix
        else:
            name = name.translate(TRANS)
        return name

    # перемфщує відомі файлу у спеціальну теку
    def move_file(files_patrn, path, el, dst):

        for doc_patern in files_patrn:
            if re.search(doc_patern, el):
                new_el = normalize(el)  # змінюю назву файлу
                src = os.path.join(path, el)  # шлях папки, з якої переміщуємо файл
                dst = os.path.join(dst, new_el)  # шлях папки, куди переміщуємо файл

                # print('Source standart file after normmalizing:', src)

                # пробуємо перемісти файл (переміщуємо з видаленням)
                try:
                    shutil.copy(src, dst)
                    print("File is copied successfully.", el)
                    os.remove(src)
                    print("File is deleted successfully.", el)


                # If source and destination are same
                except shutil.SameFileError:
                    print("Source and destination represents the same file.", el)
                    os.remove(src)
                    print("File is deleted successfully.", el)

                # If there is any permission issue
                except PermissionError:
                    print("Permission denied.", el)

                # For other errors
                except:
                    print("Error occurred while copying file.", el)

    # переміщує невідомі файлу у спеціальну папку
    def move_unknown_file(files_patrn, path, el, dst):
        for doc_patern in files_patrn:
            # result_seach = re.search(doc_patern, el)
            if re.search(doc_patern, el) == None:
                new_el = normalize(el)  # змінюю назву файлу
                src = os.path.join(path, el)
                dst = os.path.join(dst, new_el)
                try:
                    shutil.copy(src, dst)
                    os.remove(src)
                    print("File is copied successfully.")
                except shutil.SameFileError:
                    print("Source and destination represents the same file.")
                except PermissionError:
                    print("Permission denied.")
                except OSError:
                    pass

    def delete_empty_folders(path):  # видаляє порожні папки
        for el in os.listdir(path):  # перебираємо всі елементи в структурі (теки, файли)
            if os.path.isdir(path + '\\' + el):  # якщо елемент є тека
                try:
                    # os.rmdiros.rmdir(path + '\\' + el)
                    os.rmdir(path + '\\' + el)
                    print("Directory '%s' has been removed successfully" % (path + '\\' + el))
                    delete_empty_folders(path)
                except OSError:
                    print("Directory '%s' can not be removed" % (path + '\\' + el))
                    delete_empty_folders(path + '\\' + el)

    def rec_sort(path):  # сортуємо файли
        el_list = os.listdir(path)
        for folder in new_folders:  # видаляємо стандартні папки з циклу
            for el in el_list:
                if folder == el:
                    el_list.remove(el)
        for el in el_list:

            image_files = ['\.jpeg$', '\.png$', '\.jpg$', '\.svg$', '\.tiff$', '\.tif$']
            video_files = ['\.avi$', '\.mp4$', '\.mov$', '\.mkv$', '\.3gp$', '\.3g2$', '\.mpg$', '\.mpeg$']
            doc_files = ['\.doc$', '\.docx$', '\.txt$', '\.pdf$',
                         '\.xls$', '\.xlsx$', '\.pptx$', '\.mpp$', '\.html$', '\.csv$', '\.bin$']
            audio_files = ['\.mp3$', '\.ogg$', '\.wav$', '\.amr$', '\.mid$', '\.midi$', '\.mpa$', '\.wma$']
            arch_files = ['\.zip$', '\.gz$', '\.tar$', '\.7z$', '\.rar$']
            program_files = ['\.exe$', '\.bat$', '\.apk$']
            unknown_files = []

            # створив список з відомих розширень файлів
            unknown_files.extend(photo_files)
            unknown_files.extend(video_files)
            unknown_files.extend(doc_files)
            unknown_files.extend(audio_files)
            unknown_files.extend(arch_files)

            if os.path.isdir(path + '\\' + el) == False:  # It is a file
                # move the file
                move_file(photo_files, path, el, dst_img)  # переміщуємо картинки
                move_file(video_files, path, el, dst_vid)
                move_file(doc_files, path, el, dst_doc)
                move_file(audio_files, path, el, dst_aud)
                move_file(arch_files, path, el, dst_arh)
                move_unknown_file(unknown_files, path, el, dst_un)
            elif os.path.isdir(path + '\\' + el):  # It is a folder
                rec_sort(path + '\\' + el)

    def about():
        description = '******************************* description ******************************\n' \
                      'The script helps to sort files in folders according to popular file types.\n' \
                      'As a result, files will be moved into folders:\n' \
                      '<images>\n' \
                      '<documents>\n' \
                      '<audio>\n' \
                      '<video>\n' \
                      '<archives>\n' \
                      '<unknown>\n' \
                      f"If the folder doesn't contain files of some file type\n" \
                      'then a new folder for this type will not create.\n' \
                      '***************************************************************************\n'
        return description

    def menu():
        menu = '********* menu *********\n' \
               '1| about\n' \
               '2| run script\n' \
               '3| exit\n' \
               '************************\n'

        return menu

    while True:
        os.system('cls')
        print(menu())
        item = input("Your choose >>>: ")
        if item == '1':
            os.system('cls')
            print(about())
            input('<press Enter to continue>')
        elif item == '2':
            path = input('Input the file path >>>: ')
            path_root = path
            global new_folders

            # створюємо повну назву (шлях) нових папок для сортування файлів
            new_folders = ['images', 'documents',
                           'audio', 'video', 'archives', 'unknown']
            dst_doc = os.path.join(path_root, 'documents')
            dst_img = os.path.join(path_root, 'images')
            dst_aud = os.path.join(path_root, 'audio')
            dst_vid = os.path.join(path_root, 'video')
            dst_arh = os.path.join(path_root, 'archives')
            dst_un = os.path.join(path_root, 'unknown')

            try:
                creat_folder(path, new_folders)
                rec_sort(path)
                delete_empty_folders(path)
                print('Sorting completed successfully')
                input('<press Enter to continue>')
                os.system('cls')
            except FileNotFoundError:
                os.system('cls')
                print('The system cannot find the path specified: ')
                input('<press Enter to continue>')

        elif item == '3':
            print('good bye!')
            sleep(1.5)
            return 'exit'


if __name__ == '__main__':
    main()
