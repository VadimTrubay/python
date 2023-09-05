#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


file_name = 'Penguins.jpg'
with open(file_name, 'rb') as f:
    img_bytes = f.read()


import base64
img_base64 = base64.b64encode(img_bytes).decode('utf-8')


with open('image_png.py', 'w', encoding='utf-8') as f:
    f.write('''\
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


FILE_NAME_IMAGE = "{}"
IMAGE = "{}"

import base64
img_bytes = base64.b64decode(IMAGE)

import os
import tempfile

def save_and_run():
    NEW_FILE_NAME = os.path.join(tempfile.gettempdir(), FILE_NAME_IMAGE)

    # Save file
    with open(NEW_FILE_NAME, 'wb') as f:
        f.write(img_bytes)

    os.startfile(NEW_FILE_NAME)

    '''.format(file_name, img_base64))


import image_png
image_png.save_and_run()
