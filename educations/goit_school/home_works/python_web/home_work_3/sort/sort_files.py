import pathlib
from threading import Thread
suff_dict = {'images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
             'documents': ['.md', '.epub', '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.xml'],
             'text': ['.txt', '.docx', '.doc', '.ods', '.odt', '.dotx', '.docm', '.dox'],
             'archives': ['.tar', '.gz', '.zip'],
             'audio': ['.aac', '.m4a', '.mp3', '.ogg', '.raw', '.wav', '.wma'],
             'video': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mpg', '.mpeg', '.3gp'],
             'pdf': ['.pdf'],
             'html': ['.html', '.htm', '.xhtml'],
             'exe_msi': ['.exe', '.msi'],
             'dll': ['.dll'],
             'python': ['.py', '.pyw'],
             'log': ['.log'],
             'unknown': ['']
             }


def create_folder(folder_name):
    for folder in folder_name:
        if not pathlib.Path.is_dir(pathlib.Path.cwd() / f'{user_input}' / f'{folder}'):
            pathlib.Path.mkdir(pathlib.Path.cwd() / f'{user_input}' / f'{folder}')


def move_file(file_path):
    suff_dict_list = list(suff_dict.items())
    try:
        for elem in range(len(suff_dict_list)):
            if file_path.suffix in suff_dict_list[elem][1]:
                file_path.rename(pathlib.Path.cwd()/f'{user_input}'/f'{suff_dict_list[elem][0]}'/file_path.name)
                print(f"File {file_path.name} moving in  folder {pathlib.Path.cwd()/f'{suff_dict_list[elem][0]}'}")
    except FileNotFoundError as error:
        print(f'Error moving file, {error}')


def delete_empty_folders(file_path):
    for elem in file_path.iterdir():
        if elem.is_dir():
            delete_empty_folders(elem)
            if not list(elem.iterdir()):
                elem.rmdir()


if __name__ == '__main__':
    while True:
        user_input = input('Enter path to  directory for sorted(or "exit" for exit)\n>>>: ')

        if user_input == 'exit':
            print('Good bye!')
            break

        path = pathlib.Path(user_input)
        if not path.exists():
            print('Path does not exist, try again')
            continue

        else:
            create_folder(suff_dict)
            for file_path in path.glob('**/*.*'):
                th = Thread(target=move_file, args=(file_path,),)
                th.start()
                th.join()
            delete_empty_folders(path)
            print('Sorting completed')
            break