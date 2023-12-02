import console_bot.ab_work as ab
from console_bot.handlers import no_command, instruction
import console_bot.Notes as Notes
import console_bot.sort as sort
from console_bot.interface import ConsoleInterface

MAIN_INSTRUCTION = 'instruction for menu.txt'


def help(*args, **kwargs):
    return instruction(MAIN_INSTRUCTION)


def good_bye(*args, **kwargs):
    return 'Good bye'


MAIN_COMMANDS = {
    'help': help,
    'address book': ab.main,
    'notes': Notes.main,
    'sort': sort.main,
    'exit': good_bye
}


MAIN_COMMANDS_WORDS = '|'.join(MAIN_COMMANDS)


def run_bot(interface):
    interface.show_output(help())
    while True:
        user_input = interface.get_input('Choose points: address book, notes, sort: ')
        command, _ = ab.parser(user_input, MAIN_COMMANDS_WORDS)
        handler = MAIN_COMMANDS.get(command, no_command)
        output = handler(interface)
        if output:
            interface.show_output(output)
        if output == 'Good bye':
            break

def main():
    main_interface = ConsoleInterface()
    run_bot(main_interface)

if __name__ == '__main__':
    main()





