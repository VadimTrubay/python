from collections import UserDict
import os
import pickle
import re
from time import sleep

# ----------OOP----------


class Body:

    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Title(Body):

    @property
    def value(self):
        return self._value

    @Body.value.setter
    def value(self, title: str):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not re.match(r'^[a-zA-Z0-9 ,]{1,50}$', title):
            raise ValueError("Title must be up to 50 characters long and include only latin letters and digits")
        self._value = title


class Note(Body):

    @property
    def value(self):
        return self._value

    @Body.value.setter
    def value(self, value: str):
        self._value = value


class Tag(Body):

    @property
    def value(self):
        return self._value

    @Body.value.setter
    def value(self, value: str):
        if not re.match(r'^[a-zA-Z0-9_]{1,20}$', value):
            raise ValueError("Tag must be up 20 characters long and include only latin letters or digits")
        self._value = value


class Record:

    def __init__(self, title: str, note=None, tag=None) -> None:
        self.title = title
        if note is None:
            self.tag = []
            self.note = [{'note': '',
                          'tag': self.tag}]
        else:
            self.tag = [tag]
            self.note = [{'note': str(note),
                          'tag': self.tag}]

    def add_note(self, new_note):
        self.note[0]['note'] += ' ' + str(new_note)

    def del_note(self, tag1):
        if tag1 in self.note[0]['tag']:
            print("The note will be deleted.")

    def add_tag(self, new_tag):
        if new_tag in self.note[0]['tag']:
            print(f"Tag {new_tag} already exist!")
        else:
            self.note[0]['tag'].append(new_tag)

    def find_note(self, tag1):
        tags_collection = []
        for tag_value in self.note[0]['tag']:
            tags_collection.append(str(tag_value))
        if tag1 in tags_collection:
            return (self.note[0]['note'])

    def __repr__(self) -> str:
        note_value = ''
        for i in self.note:
            for key, value in i.items():
                if key == 'note':
                    note_value = value
                return 'Title: ' + f'{self.title}\n' \
                                   'Note: ' + f'{note_value}\n' \
                                              'Tag: ' + f'{self.tag}\n'


class NoteBook(UserDict):

    def add_record(self, record: list):
        self.data[record.title] = record

    def del_record(self, record):
        del self.data[record.title]

    def iterator(self, n=None):
        step = 1
        result = ''
        for record in self.data.values():
            if n is None or n(record):
                result += str(record) + '\n'
                if step < 1:
                    step += 1
                else:
                    yield result
                    step = 1
                    result = ' ' * 40 + '\n'
        yield result


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, text):
        try:
            return self.func(text)
        except IndexError:
            return "Please, enter the correct message!"
        except ValueError:
            return "Please, enter the right command!"
        except KeyError:
            return "Sorry, user not found!"
        except TypeError:
            return "Please, give me only one command!"
        except AttributeError:
            return "AttributeError!"


# ----------Work with file----------

file_1 = 'Notebook.bin'


def save_file(notebook):
    with open(file_1, "wb") as f:
        pickle.dump(notebook, f)


def load_file():
    try:
        with open(file_1, "rb") as f:
            reader = pickle.load(f)
            return reader
    except FileNotFoundError:
        reader = NoteBook()
        return reader


# ----------Functional----------

@InputError
def add_new_note(text):
    new_title = input("Write the title: ")
    new_note = input("Write your note: ")
    new_tag = input("Write special tag: ")
    if new_note and new_tag:
        title = Title(new_title)
        new_record = Record(str(title), Note(new_note), Tag(new_tag))
    else:
        new_record = Record(Title(new_title))
    text.add_record(new_record)
    save_file(text)
    return "\nThe note saved!"


@InputError
def ad_tag(text):
    all_titles = list(text.keys())
    print(f"All titles:\n {all_titles} ")
    title = input("Enter the title to which you want to add a new tag: ")
    if title in all_titles:
        new_tag = input("Add new tag:")
        text[title].add_tag(new_tag)
        save_file(text)
        return f"The tag {new_tag} saved!"
    else:
        return "Note was not found!"


@InputError
def del_note(text):
    print(f"All titles:\n {list(text.keys())} ")
    sp_title = input("Enter the title to which you want to delete: ")
    if sp_title in list(text.keys()):
        text.del_record(text[sp_title])
        save_file(text)
        return "The note deleted!"
    else:
        return "Note was not found!"


@InputError
def find_rec(text):
    list1 = []
    list2 = []
    count = 0
    case = input("Enter the special word to find note:")
    for dt in list(text.items()):
        list1.append(dict([dt]))
        dt_dict = dict([dt])
        for key, value in dt_dict.items():
            words = [key.lower(), value.note[0]['note'].lower()]
            for i in value.note[0]['tag']:
                words.append(str(i))
            if any(case.lower() in w for w in words):
                list2.append(dt)
                count += 1
    if count == 0:
        res = "Not found"
    else:
        res = f"Word '{case}' was found in {count} notes: \n"
    for i in list2:
        res += f"{i[1]}\n"
    return res


@InputError
def find_note_with_tag(text):
    print("All tags:\n")
    for k, v in text.items():
        print(k, str(v.note[0]['tag']))
    sp_tag = input("Enter a tag to search for a notes: ")
    notes_with_tag = []
    for value in text.values():
        notes_with_tag.append(value.find_note(sp_tag))
        for n in notes_with_tag:
            if n is None:
                notes_with_tag.remove(n)

    return notes_with_tag


@InputError
def edit(text):
    print(f"All titles:\n {list(text.keys())} ")
    sp_title = input("Enter the title to which you want to edit: ")
    if sp_title in list(text.keys()):
        new_note = input("Enter the new note: ")
        for key, value in text.items():
            if key == sp_title:
                note_0 = value.note[0]['note']
                value.note[0]['note'] = new_note
                save_file(text)
                return f"Note was changed!\nFrom '{note_0}' -> to '{new_note}'"


def to_exit(text):
    save_file(text)
    return "Good bye!"


def show_all(text):
    if not text:
        return 'NoteBook is empty'
    result = f"\nList of all notes:\n{'*' * 20}\n"
    result_list = text.iterator()
    for i in result_list:
        result += f"{i}"
    return result


def clean(text):
    cl = input("Are you sure for delete all? (yes/no)\n")
    if cl == 'yes':
        text.clear()
        save_file(text)
        return "Notebook is clean"


def help_for_user(*args):
    return '************************* menu ************************\n'\
           'Command                                          Action\n'\
           '*******************************************************\n'\
           '1| add, new                             create new note\n'\
           '2| tag                           add other tag for note\n'\
           '3| find note                       to find note by word\n'\
           '4| find by tag                      to find note by tag\n'\
           '5| edit                 replace the content of the note\n'\
           '6| show                               to show all notes\n'\
           '7| del, delete                          delete one note\n'\
           '8| clean                   delete all notes in Notebook\n'\
           '9| exit                            application shutdown\n'\
           '*******************************************************\n'


def unknow(*args):
    return "Please, try again!"


COMMANDS = {add_new_note: ['1', 'add', 'new'],
            ad_tag: ['tag', '2'],
            del_note: ['del', 'delete', '7'],
            find_note_with_tag: ['find by tag', '4'],
            find_rec: ['find note', '3'],
            edit: ['edit', '5'],
            to_exit: ['exit', '9'],
            show_all: ['show', '6'],
            clean: ['clean', '8']}


def command_parser(user_command: str):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknow, []


def main():
    text = load_file()
    print(help_for_user())
    while True:
        os.system('cls')
        print(help_for_user())
        user_command = input("Enter command >>>: ")
        if user_command == 'exit' or user_command == '9':
            print('good bye!')
            sleep(1.5)
            return 'exit'
        command, data = command_parser(user_command)
        print(command(text))
        input('<press Enter to continue>')


if __name__ == "__main__":
    main()

