''' Есть список, каждый элемент которого — это словарь с контактами пользователя следующего вида:

    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }
Словарь содержит имя пользователя name, его email, телефонный номер phone и свойство favorite —
избранный контакт или нет.

Разработайте две функции для сериализации и десериализации списка контактов с помощью пакета csv и
хранения полученных данных в текстовом файле.

Первая функция write_contacts_to_file принимает два параметра: filename — имя файла, contacts — список контактов.
Она сохраняет указанный список в файл формата csv.

Структура csv файла должна быть следующей:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True
Обратите внимание, первой строкой в файле идут заголовки — это названия ключей.

Вторая функция read_contacts_from_file читает, выполняет преобразование данных и
 возвращает указанный список contacts из файла filename, сохраненного ранее функцией write_contacts_to_file.

Примечание: При чтении csv файла мы получаем свойство словаря favorite в виде строки, т.е. например favorite='False'.
Необходимо его привести к логическому выражению обратно, чтобы стало favorite=False. '''

import csv

filename = 'test.csv'
contacts = [{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False
}]


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as f:
        for i in contacts:
            field_names = i.keys()
        writer = csv.DictWriter(f, delimiter=',', fieldnames=field_names)
        writer.writeheader()
        for row in contacts:
            writer.writerow(row)


def read_contacts_from_file(filename):
    lis = []
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for i in reader:
            if i.get("favorite") == "True":
                v = True
            if i.get("favorite") == "False":
                v = False
            clear = i.pop("favorite")
            i.update({"favorite": v})
            lis.append(i)
        return lis


write_contacts_to_file('test.csv', contacts)
print(read_contacts_from_file('test.csv'))
