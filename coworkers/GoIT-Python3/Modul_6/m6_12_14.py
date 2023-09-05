'''Функция get_credentials_users из предыдущей задачи возвращает нам список строк username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реализуйте функцию encode_data_to_base64(data), которая принимает в параметре data указанный список,
выполняет кодирование каждой пары username:password в формат Base64 и
возвращает список с закодированными парами username:password в виде:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']'''

import base64


def encode_data_to_base64(data):
    result = []
    for i in data:
        j = i.encode("utf-8")
        list = base64.b64encode(j)
        list_cl = list.decode("utf-8")
        result.append(list_cl)

    return result