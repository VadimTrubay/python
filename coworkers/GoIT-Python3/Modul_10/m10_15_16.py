''' Продолжаем расширять функциональность класса Contacts.
На этом этапе мы добавим в класс метод get_contact_by_id.
Метод должен искать контакт по уникальному id в списке contacts и возвращать словарь из него с указанным ключом id.
Если словаря с указанным id в списке contacts не найдено, метод возвращает None.
Примечание: для правильного прохождения теста не создавайте экземпляр класса в коде. '''


def add_contacts(self, name, phone, email, favorite):
    self.contacts.append(
        {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite,
        }
    )
    Contacts.current_id += 1


def get_contact_by_id(self, id):
    for contact in self.contacts:
        for k in contact.keys():
            if contact[k] == id:
                return contact

