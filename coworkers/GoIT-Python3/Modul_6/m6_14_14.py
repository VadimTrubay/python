'''Создайте функционал для распаковки архива.

Сделайте import пакета shutil

Создайте функцию unpack(archive_path, path_to_unpack), которая будет вызывать метод пакета shutil unpack_archive
 и распаковывать архив archive_path в место path_to_unpack.

Функция ничего не возвращает.'''

import shutil


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)