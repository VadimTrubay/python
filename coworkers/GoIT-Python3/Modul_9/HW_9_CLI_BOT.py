''' Задание#
Напишите консольного бота помощника, который будет распознавать команды, вводимые с клавиатуры, и отвечать согласно введенной команде.

Бот помощник должен стать для нас прототипом приложения-ассистента.
Приложение-ассистент в первом приближении должен уметь работать с книгой контактов и календарем.
В этой домашней работе сосредоточимся на интерфейсе самого бота.
Наиболее простой и удобный на начальном этапе разработки интерфейс - это консольное приложение CLI (Command Line Interface).
CLI достаточно просто реализовать. Любой CLI состоит из трех основных элементов:

Парсер команд. Часть, которая отвечает за разбор введенных пользователем строк, выделение из строки ключевых слов и модификаторов команд.
Функции обработчики команд — набор функций, которые ещё называют handler, они отвечают за непосредственное выполнение команд.
Цикл запрос-ответ. Эта часть приложения отвечает за получение от пользователя данных и возврат пользователю ответа от функции-handlerа.
На первом этапе наш бот-ассистент должен уметь сохранять имя и номер телефона, находить номер телефона по имени,
изменять записанный номер телефона, выводить в консоль все записи, которые сохранил.
Чтобы реализовать такую несложную логику, воспользуемся словарем.
В словаре будем хранить имя пользователя как ключ и номер телефона как значение.

Условия#
Бот должен находиться в бесконечном цикле, ожидая команды пользователя.
Бот завершает свою работу, если встречает слова: .
Бот не чувствительный к регистру вводимых команд.

Бот принимает команды:
"hello", отвечает в консоль "How can I help you?"
"add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.

"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.

"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
Вместо ... пользователь вводит имя контакта, чей номер нужно показать.

"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.

"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того, как выведет в консоль "Good bye!".

Все ошибки пользовательского ввода должны обрабатываться при помощи декоратора input_error.
Этот декоратор отвечает за возврат пользователю сообщений вида "Enter user name", "Give me name and phone please" и т.п.
 Декоратор input_error должен обрабатывать исключения, которые возникают в функциях-handler (KeyError, ValueError, IndexError)
 и возвращать соответствующий ответ пользователю.
Логика команд реализована в отдельных функциях и эти функции принимают на вход одну или несколько строк и возвращают строку.
Вся логика взаимодействия с пользователем реализована в функции main, все print и input происходят только там. '''

DB = {}
list_command = []

def input_error(func):
    def wrapper():
        try:
            return func()
        except IndexError:
            return "This command 'add' please write 'add' 'name' 'number'"
        except KeyError:
            return "This command 'phone' please write 'phone' 'name'"
        except ValueError:
            return "This command 'change' please write 'change' 'name' 'number'"
    return wrapper


def greeting():
    return "How can I help you?"


def exiting():
    return "Good bye!"

def exiting1():
    return "Good bye!"

def exiting2():
    return "Good bye!"

@input_error
def adding():
    if len(list_command) > 3:
        raise IndexError
    DB.update({list_command[1]: list_command[2]})
    return "You add new contact"

@input_error
def changing():
    if len(list_command) > 3:
        raise ValueError
    for k in DB.keys():
        if k == list_command[1]:
            DB[k] = list_command[2]
    return f"Contact {list_command[1].title()} was changed"
@input_error
def get_phone():
    if not 1 < len(list_command) < 3:
        raise KeyError
    result = DB.get(list_command[1])
    return f'Contact find {list_command[1].title()} {result}'

def get_contacts():
    cont_list = []
    for k, v in DB.items():
        _ = k.title() + ' ' + str(v)
        cont_list.append(_)
        stroka = ('\n').join(cont_list)
    return f'Contacts list:\n{stroka}'


COMMANDS = {greeting: "hello", exiting: "good bye", exiting1: "close", exiting2: "exit", get_contacts: 'show all'}


def main():
    flag = True
    while flag:
        user_in = input(">>> ")
        if user_in == '.':
            break
        user_input = user_in.lower()
        for k, v in COMMANDS.items():
            if user_input.startswith(v):
                print(k())
            if user_input in ['good bye', 'exit', 'close']:
                flag = False
        lst = user_input.split(' ')
        if lst[0] == 'add':
            list_command.extend(lst)
            print(adding())
            list_command.clear()
        if lst[0] == 'change':
            list_command.extend(lst)
            print(changing())
            list_command.clear()
        if lst[0] == 'phone':
            list_command.extend(lst)
            print(get_phone(), end='\n')
            list_command.clear()


if __name__ == "__main__":
    main()
