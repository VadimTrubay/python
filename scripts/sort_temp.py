from pathlib import Path
import sys
import os
import shutil

# def create_dir(item):


# for i in dicts:
#     if item[1] in i:


def sort_func(path):
    # Path.mkdir('\work_it\GitHub\GoIt_school\home_works\home_work_6\mess\\images', exist_ok=True)
    # Path.mkdir('\work_it\GitHub\GoIt_school\home_works\home_work_6\mess\\video', exist_ok=True)
    # Path.mkdir('\work_it\GitHub\GoIt_school\home_works\home_work_6\mess\\documents', exist_ok=True)
    # Path.mkdir('\work_it\GitHub\GoIt_school\home_works\home_work_6\mess\\audio', exist_ok=True)
    # Path.mkdir('\work_it\GitHub\GoIt_school\home_works\home_work_6\mess\\archives', exist_ok=True)
    ignore = ['image', 'video', 'documents', 'audio', 'archives']

    dict_images = ['.jpeg', '.png', '.jpg', '.svg']
    dict_video = ['.avi', '.mov', '.mp4', '.mkv']
    dict_documents = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
    dict_audio = ['.mp3', '.ogg', '.wav', '.amr']
    dict_archives = ['.tar', '.gz', '.rar', '.zip']

    if path.is_dir():
        for file in path.iterdir():
            if file.name in ignore:
                continue
            elif file.is_file():
                norm_file = normalize(file)
                file_split = norm_file.split('.')
                if file_split[1] in dict_images:
                    shutil.move(path, '\work_it\GitHub\GoIt_school\home_works\home_work_6\mess\\images')



# elif cur_dir.is_dir():
#     sort_func(file)
# for suff in dir_suff_dict:
#     if file.suffix.lower() in dir_suff_dict[suff]:
#         dir_img = cur_dir / suff
#         dir_img.mkdir(exist_ok=True)
#         file.rename(dir_img.joinpath(file.name))

def normalize(name: str) -> str:
    CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja")

    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name


if __name__ == "__main__":
    path = Path('\work_it\GitHub\GoIt_school\home_works\home_work_6\mess')
    # path = Path(sys.argv[1])
    if not path.exists():
        print('directory does not exist')
    else:
        print(path)
        sort_func(path)
    # print('sorting files finally')
