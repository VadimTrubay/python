#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import socket

import sys
sys.path.append('..')

from common import send_msg__with_crc32, recv_msg__with_crc32


HOST, PORT = "localhost", 9090


with socket.socket() as sock:
    sock.connect((HOST, PORT))

    # Send file
    with open('img.png', 'rb') as f:
        data = f.read()

    print('Sending ({}): {}'.format(len(data), data))
    print()

    send_msg__with_crc32(sock, data)

    print('Receiving')

    response_data = recv_msg__with_crc32(sock)
    print('Response ({}): {}'.format(len(response_data), response_data))

    print('Close\n')
