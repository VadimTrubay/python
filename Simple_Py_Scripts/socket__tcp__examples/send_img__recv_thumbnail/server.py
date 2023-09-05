#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from PIL import Image
import io

import socket

import sys
sys.path.append('..')

from common import send_msg, recv_msg


PORT = 9090


with socket.socket() as sock:
    sock.bind(('', PORT))
    sock.listen()

    print('Server: {}'.format(sock.getsockname()))

    while True:
        conn, addr = sock.accept()
        print('Connected:', addr)

        data = recv_msg(conn)
        print('Receiving {} bytes'.format(len(data)))

        img = Image.open(io.BytesIO(data))
        print('Receiving image:', img)

        print('Transform image in thumbnail')

        # Transform in thumbnail
        img.thumbnail((75, 75))

        print('Img:', img)

        # Write thumbnail in buffer
        data_io = io.BytesIO()
        img.save(data_io, 'jpeg')

        response_data = data_io.getvalue()

        print('Sending {} bytes'.format(len(response_data)))

        send_msg(conn, response_data)

        print('Close\n')
