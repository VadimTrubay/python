from goit_school.home_works.python_core.home_work_12.temp.contact_book import *


class Bot:

    def __init__(self):
        self.book = ContactBook()

    def handler(self, command):
        try:
            if command == 'help':
                CommandHelp.command_help()

            elif command == 'add':
                name = Name(input('add name: ')).value.strip().lower()
                if name:
                    if not self.book:
                        phone = Phone(input('phone(+380xxxxxxxxx): ')).value.strip()
                        birth = Birthday(input('birthday(dd.mm.YYYY): ')).value.strip()
                        record = Record(name, phone, birth)
                        self.book.add(record)
                    else:
                        for contact in self.book:
                            if not name in contact.values():
                                phone = Phone(input('phone(+380xxxxxxxxx): ')).value.strip()
                                birth = Birthday(input('birthday(dd.mm.YYYY): ')).value.strip()
                                record = Record(name, phone, birth)
                                self.book.add(record)
                                break
                            else:
                                print('this name already exists\nenter command to edit')
                                break
                else:
                    print('please enter a name')

            elif command == 'all':
                n = int(input('number of contacts per page: ').strip())
                if self.book:
                    self.book.get_page(n)
                else:
                    print('address_book_vad_1.0.01 empty')

            elif command == 'find':
                pattern = input('pattern: ').strip().lower()
                if pattern:
                    self.book.find_info(pattern)
                else:
                    print('please enter a pattern')

            elif command == 'edit':
                name = input('name: ')
                if name:
                    print('which parameter to edit(phone, birthday)')
                    parameter = input('enter parameter : ').strip()
                    new_value = input('new value: ')
                    self.book.edit(name, parameter, new_value)
                else:
                    print('please enter a name')

            elif command == 'birthday':
                name = input('birthday name: ').strip().lower()
                if name:
                    self.book.days_to_birthday(name)
                else:
                    print('please enter a name')

            elif command == 'delete':
                value = input('delete name: ').strip().lower()
                if value:
                    self.book.delete(value)
                else:
                    print('please enter a name')

            elif command == 'clear':
                self.book.clear_book()

            elif command == 'save':
                file_name = input('save file name: ').strip()
                if file_name:
                    self.book.save(file_name)
                    print(f'address_book_vad_1.0.01 {file_name} saved')
                else:
                    print('please enter file name')

            elif command == 'load':
                file_name = input('load file name: ').strip()
                if file_name:
                    self.book.load(file_name)
                    print(f'address_book_vad_1.0.01 {file_name} loaded')
                else:
                    print('please enter file name')

            elif command == 'exit':
                pass

            else:
                print('invalid command')

        except Exception:
            print('invalid input, try again')

        finally:
            self.book.save('save')
