from address_book import *


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, command):
        if command == 'hello':
            print('>how can i help you?')
        elif command == 'add':
            name = Name(input('name: ')).value.strip().lower()
            phone = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input('note: ')).value
            record = Record(name, phone, birth, email, status, note)
            return self.book.add(record)
        elif command == 'search':
            print('>there are following categories (name, phone, birthday, status, note)')
            category = input('>search category: ')
            pattern = input('>search pattern: ')
            result = (self.book.search(pattern, category))
            for key in result:
                if key['birthday']:
                    birth = key['birthday'].strftime('%d.%m.%Y')
                    result = '-' * 50 + f"\nname: {key['name']} " \
                             f"\nphone: {', '.join(key['phone'])} " \
                             f"\nbirthday: {birth} " \
                             f"\nemail: {key['email']} " \
                             f"\nstatus: {key['status']} " \
                             f"\nnote: {key['note']}\n" + '-' * 50
                    print(result)
        elif command == 'edit':
            contact_name = input('>contact name: ')
            print('>which parameter to edit(name, phone, birthday, status, email, note)')
            parameter = input('>enter parameter : ').strip()
            new_value = input('new value: ')
            return self.book.edit(contact_name, parameter, new_value)
        elif command == 'delete':
            value = input('>delete (contact name or phone): ')
            return self.book.delete(value)
        elif command == 'clear':
            return self.book.clear_book()
        elif command == 'save':
            file_name = input('>file name: ')
            return self.book.save(file_name)
        elif command == 'load':
            file_name = input('>file name: ')
            return self.book.load(file_name)
        elif command == 'congratulate':
            print(self.book.congratulate())
        elif command == 'all':
            if self.book:
                print(self.book)
            else:
                print('>address_book_vad_1.0.01 empty')
        elif command == 'exit':
            pass
        else:
            print('>invalid command')
            print('----------------------------------------')