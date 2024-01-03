import os
import re
import sys
from pathlib import Path
import shutil

suff_dict = {'images': ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.ico', '.bmp', '.webp', '.svg'],
             'documents': ['.md', '.epub', '.txt', '.docx', '.doc', '.ods', '.odt', '.dotx', '.docm', '.dox',
                           '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.xml'],
             'archives': ['.tar', '.gz', '.zip', '.rar'],
             'audio': ['.aac', '.m4a', '.mp3', '.ogg', '.raw', '.wav', '.wma'],
             'video': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mpg', '.mpeg', '.3gp'],
             'pdf': ['.pdf'],
             'html': ['.html', '.htm', '.xhtml'],
             'exe_msi': ['.exe', '.msi']}


def normalize(name: str, suffix: str) -> str:
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
    return new_name + suffix


def unpack_archive(path: str):
    if path.is_dir():
        for item in path.iterdir():
            if item.name == 'archives':
                for arch in item.iterdir():
                    name = item / arch.stem
                    name.mkdir(parents=True, exist_ok=True)
                    try:
                        shutil.unpack_archive(arch, name)
                    except shutil.ReadError:
                        continue
            if item.is_dir():
                result = [f for f in os.listdir(item)]
                print(f"files in category {item.name}: {', '.join(result)}")
            else:
                continue


def sort_func(path: Path):
    try:
        for p in path.iterdir():
            if p.is_dir():
                sort_func(p)
                if not list(p.iterdir()):
                    # Delete the empty folder
                    p.rmdir()
            else:
                try:
                    new_name = normalize(p.stem, p.suffix)
                    for key, value in suff_dict.items():
                        if p.suffix in value:
                            target_dir = path / key
                            target_dir.mkdir(exist_ok=True)
                            shutil.move(p, target_dir / new_name)
                            break  # Exit the loop once we've moved the file to the correct category
                    else:
                        # If no match found, move to 'unknown' directory
                        target_dir = path / 'unknown'
                        target_dir.mkdir(exist_ok=True)
                        shutil.move(p, target_dir / new_name)
                except Exception as e:
                    print(f"Error while processing {p}: {e}")

    except FileExistsError as error:
        print(error)


def main():
    print('starting sorting...')
    print('===================\n')
    path = Path('mess')
    if not path.exists():
        print('path does not exist')
        sys.exit(4)
    else:
        sort_func(path)
    unpack_archive(path)

    print('================')
    print('ending sorting!')


if __name__ == "__main__":
    main()
