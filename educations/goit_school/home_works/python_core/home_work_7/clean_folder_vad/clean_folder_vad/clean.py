import os
import re
import sys
from pathlib import Path
import shutil

suff_dict = {'images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
             'documents': ['.md', '.epub', '.txt', '.docx', '.doc', '.ods', '.odt', '.dotx', '.docm', '.dox',
                           '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.xml'],
             'archives': ['.tar', '.gz', '.zip'],
             'audio': ['.aac', '.m4a', '.mp3', '.ogg', '.raw', '.wav', '.wma'],
             'video': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mpg', '.mpeg', '.3gp'],
             'pdf': ['.pdf'],
             'html': ['.html', '.htm', '.xhtml'],
             'exe_msi': ['.exe', '.msi'],
             'python': ['.py', '.pyw']}


def normalize(name: str) -> str:
    cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    translation = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
        "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja")

    trans = {}
    for c, l in zip(cyrillic, translation):
        trans[ord(c)] = l
        trans[ord(c.upper())] = l.upper()
    new_name = name.translate(trans)
    new_name = re.sub(r'\W', '_', new_name)
    return new_name


def move_file(dir_p: Path, path_file: Path):

    dir_p.mkdir(exist_ok=True)
    if (Path(dir_p) / path_file.name).exists():
        path_file.rename(dir_p.joinpath(f'{path_file.name[0:-len(path_file.suffix)]}{path_file.suffix}'))
    else:
        path_file.rename(dir_p / path_file.name)


def extension_comparison(curr_dir: Path, path_file: Path, suf: str) -> bool:

    if path_file.suffix in suff_dict[suf]:
        move_file(Path(curr_dir) / suf, path_file)
        return True
    return False


def name_normalize(root: str, file: str) -> Path:

    path_file = Path(root) / file
    normalize_n = f"{normalize(path_file.name[0:-len(path_file.suffix)])}{path_file.suffix}"
    path_file = path_file.rename(Path(root) / normalize_n)
    return path_file


def remove_dir(subdir: list):

    for path in subdir:
        try:
            if len(os.listdir(path)) > 0 or Path(path).name in suff_dict:
                continue
            Path(path).rmdir()
        except FileNotFoundError:
            continue


def sort_func(path: str) -> tuple:

    curr_dir = path
    subdir = []
    known_extensions, unknown_extensions = set(), set()
    try:
        for root, dirs, files in os.walk(path):
            for d in dirs:
                if not d:
                    continue
                subdir.append(f"{curr_dir / d}")
            for file in files:
                path_file = name_normalize(root, file)
                ex_comp = False
                for suf in suff_dict:
                    ex_comp = extension_comparison(curr_dir, path_file, suf)
                    if ex_comp:
                        known_extensions.add(path_file.suffix)
                        break
                if not ex_comp:
                    unknown_extensions.add(path_file.suffix)
    except FileExistsError:
        pass

    remove_dir(subdir)
    return list(known_extensions), list(unknown_extensions)


def main():

    print('starting sorting...')
    print('===================\n')
    known, unknown = '', ''
    path = Path(sys.argv[1])
    # path = Path('mess')
    if not path.exists():
        print('path does not exist')
        sys.exit(4)
    else:
        known, unknown = sort_func(path)

    if path.is_dir():
        for item in path.iterdir():
            if item.name == 'archives':
                for arch in item.iterdir():
                    name = item / arch.stem
                    name.mkdir(parents=True, exist_ok=True)
                    try:
                        shutil.unpack_archive(arch, name)
                    except Exception:
                        continue
            if item.is_dir():
                result = [f for f in os.listdir(item)]
                print(f"files in category {item.name}: {', '.join(result)}")
            else:
                continue

    if len(known) >= 0:
        print(f"\nknown extensions: {', '.join(known)}")
    if len(unknown) >= 0:
        print(f"unknown extensions: {', '.join(unknown)}\n")

    print('================')
    print('ending sorting!')


if __name__ == "__main__":
    main()
