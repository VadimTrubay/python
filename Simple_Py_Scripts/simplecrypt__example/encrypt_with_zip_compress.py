#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


def encrypt(password, message, use_zip=False):
    if use_zip:
        import io
        zip_data_io = io.BytesIO()

        # Append as data in file
        import zipfile
        with zipfile.ZipFile(zip_data_io, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            zf.writestr('message.txt', message)

        message = zip_data_io.getvalue()

    from simplecrypt import encrypt
    message = encrypt(password, message)
    return message


def decrypt(password, message, use_zip=False):
    from simplecrypt import decrypt
    message = decrypt(password, message)

    if use_zip:
        import io
        zip_data_io = io.BytesIO(message)

        import zipfile
        with zipfile.ZipFile(zip_data_io, mode='r') as zf:
            message = zf.read('message.txt')

    return message


def get_digest(data):
    import hashlib
    sha1 = hashlib.sha1(data)
    return sha1.hexdigest()


import time
import binascii


def get_logger(name):
    import logging
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s] %(message)s')

    import sys
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    return log


log = get_logger('encrypt_with_zip_compress')


def run_crypt_decrypt(message, password, use_zip=False, show_hex=False):
    start_time = time.time()

    text_hex = binascii.hexlify(message)
    message_digest = get_digest(message)
    log.debug('Message len: {}, digest: {}'.format(len(message), message_digest))
    show_hex and log.debug('text_hex: "{}"'.format(text_hex))
    log.debug('')

    log.debug('Encrypt...')
    encrypt_text = encrypt(password, message, use_zip)
    encrypt_text_hex = binascii.hexlify(encrypt_text)
    encrypt_message_digest = get_digest(encrypt_text)
    log.debug('Encrypt message len: {}, digest: {}'.format(len(encrypt_text), encrypt_message_digest))
    show_hex and log.debug('encrypt_text_hex: "{}"'.format(encrypt_text_hex))

    log.debug('')
    log.debug('Decrypt...')
    decrypt_text = decrypt(password, encrypt_text, use_zip)
    decrypt_text_hex = binascii.hexlify(decrypt_text)
    decrypt_message_digest = get_digest(decrypt_text)
    log.debug('Decrypt message len: {}, digest: {}'.format(len(decrypt_text), decrypt_message_digest))
    show_hex and log.debug('decrypt_text_hex: "{}"'.format(decrypt_text_hex))

    log.debug('')
    log.debug('Digest is equal: {}'.format(message_digest == decrypt_message_digest))
    log.debug('Total time: {:.3f} seconds'.format(time.time() - start_time))


# Random message
import random
import string
MESSAGE = ''.join(random.choice(string.hexdigits) for _ in range(5000000)).encode()
PASSWORD = "secret"


if __name__ == '__main__':
    log.debug('CRYPT_DECRYPT_TEST: use_zip=False')
    run_crypt_decrypt(MESSAGE, PASSWORD, use_zip=False)

    log.debug('')
    log.debug('_' * 100)
    log.debug('')

    log.debug('CRYPT_DECRYPT_TEST: use_zip=True')
    run_crypt_decrypt(MESSAGE, PASSWORD, use_zip=True)
