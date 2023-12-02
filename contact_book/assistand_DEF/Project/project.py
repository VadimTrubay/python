import re
import pickle
import json
from colorit import *
import pprint

class Error(Exception):
    pass

STOPLIST =[".", "end", "close","exit","bye","good bye"]
users = []

def verificate_email(text:str):
    email_re = re.findall(r"\w+3\@{1}\w+\.\w+", text)
    email = "".join(email_re)
    if bool(email) == True:
        return email
    else:
        raise Error

def verificate_birthday(text:str): 
    date_re = re.findall(r"\d{4}\.\d{2}\.\d{2}", text)
    date = "".join(date_re)
    if bool(date) == True:
        return date
    else:
        raise Error

def verificate_number(num): #Done
    flag = True
    try:
        number = re.sub(r"\+\(\)A-Za-z\ ", "", num)
        if len(number) == 12:
            number = "+" + number

        elif len(number) == 10:
            number = "+38" + number

        elif len(number) == 9:
            number = "+380" + number

        else:
            flag = False
            raise Error
    except Error:
        print(color(f"This number dont correct {number}",Colors.red))

    return number if flag else ""

def add_user(text:str):  #Done
    text = text.split()
    phones = []

    if text[0] == "None":
        return color("Please enter the name",Colors.red)

    for num in text[1:]:
        num = verificate_number(num)
        phones.append(num)


    example = {
    "Name": text[0],
    "Phone": phones,
    "Email": [],
    "Birthday": None,
    "Tags": [],
    "Adress": None
    }

    users.append(example)
    return color("Done",Colors.blue)

def show_all(nothing= ""):  # Done
    if len(users) == 0:
        return color("Adressbook is empty!", Colors.blue)
    for user in users:
        pprint.pp(user)
    return color("Done",Colors.blue)

def add_phone(text:str):
    text = text.split()

    if len(users) == 0:
                return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if text[0] in user.values():
            user["Phone"].append(verificate_number(text[1]))
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def add_email(text:str):
    text = text.split()
    email_re = re.findall(r"[\w+3\@{1}\w+\.\w+]", text[1])
    email = "".join(email_re)

    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)
    
    for user in users:
        user:dict
        if text[0] in user.values():
            user["Email"].append(email)
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def add_birthday(text:str):
    text = text.split()
    date_re = re.findall(r"\d{4}\.\d{2}\.\d{2}", text[1])
    date = "".join(date_re)

    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)
    
    for user in users:
        user:dict
        if text[0] in user.values():
            if bool(user["Birthday"]) == True:
                return color("This user already has birthday date", Colors.red)
            else:
                user["Birthday"] = date
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def add_tags(text:str):
    text = text.split()

    for user in users:
        user: dict
        if text[0] in user.values():
            user["Tags"].append(" ".join(text[1:]))
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def add_adress(text:str):
    text = text.split()

    
    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if text[0] in user.values():
            if bool(user["Adress"]) == True:
                return color("This user already has adress", Colors.red)
            else:
                user["Adress"] = " ".join(text[1:])
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def change_adress(text:str):
    text = text.split()

    for user in users:
        user: dict
        if text[0] in user.values():
            user["Adress"]= (" ".join(text[1:]))
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def change_phone(text:str):
    text = text.split()
    name = text[0]
    oldphone = verificate_number(text[1])
    newphone = verificate_number(text[2])
    if len(users) == 0:
                return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            if oldphone in user["Phone"]:
                user["Phone"].remove(oldphone)
                user["Phone"].append(newphone)
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def change_email(text:str):
    text = text.split()
    name = text[0]
    oldemail = verificate_email(text[1])
    newemail = verificate_email(text[2])
    if len(users) == 0:
                return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            if oldemail in user["Email"]:
                user["Email"].remove(oldemail)
                user["Email"].append(newemail)
            else:
                return color("This user or email dont exist in addressbook",Colors.red)
        else:
            return color("This user or email dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def change_birthday(text:str):
    text = text.split()
    name = text[0]
    birthday = verificate_birthday(text[1])
    
    if len(users) == 0:
                return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            user["Birthday"] = birthday
        else:
            return color("This date dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def remove_phone(text:str):
    text = text.split()
    name = text[0]
    oldphone = verificate_number(text[1])

    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            user["Phone"].remove(oldphone)
        else:
            return color("This number dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def remove_email(text:str):
    text = text.split()
    name = text[0]
    oldemail = verificate_email(text[1])

    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            if oldemail in user["Email"]:
                user["Email"].remove(oldemail)
            else:
                return color("This email dont exist in addressbook",Colors.red)
        else:
            return color("This email dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def remove_birthday(text:str):
    text = text.split()
    name = text[0]

    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            if user["Birthday"] !=None:
                user["Birthday"] = None
            else:
                return color("This birthday dont exist in addressbook",Colors.red)
        else:
            return color("This birthday dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def remove_tags(text:str):
    text = text.split()
    name = text[0]
    tags = " ".join(text[1:])

    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            if tags in user["Tags"]:
                user["Tags"].remove(tags)
            else:
                return color("This tags dont exist in addressbook",Colors.red)
        else:
            return color("This tags dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def remove_user(text:str):
    text = text.split()
    name = text[0]

    if len(users) == 0:
        return color("Addressbook is empty", Colors.red)

    for user in users:
        user: dict
        if name in user.values():
            users.remove(user)
        else:
            return color("This user dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def remove_adress(text:str):
    text = text.split()

    for user in users:
        user: dict
        if text[0] in user.values():
            user["Adress"]= None
        else:
            return color("This adress dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)
    
def find_name(text):

    text = text.split()

    for user in users:
        user: dict
        if text[0] in user["Name"]:
            return f"Name: {user['Name']} \nPhone: {user['Phone']} \nEmail: {user['Email']} \nBirthday: {user['Birthday']} \nTags: {user['Tags']} \nAdress: {user['Adress']} "
        # else:
        #     return color("This name dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def find_tags(text:str):
    text = text.split()

    for user in users:
        user: dict
        if text[0] in user["Tags"]:
            return f"Name: {user['Name']} \nPhone: {user['Phone']} \nEmail: {user['Email']} \nBirthday: {user['Birthday']} \nTags: {user['Tags']} \nAdress: {user['Adress']} "
        # else:
        #     return color("This tags dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def find_phone(text:str):
    text = text.split()
    phone = verificate_number(text[0])

    for user in users:
        user: dict
        if phone in user["Phone"]:
            user:dict
            return f"Name: {user['Name']} \nPhone: {user['Phone']} \nEmail: {user['Email']} \nBirthday: {user['Birthday']} \nTags: {user['Tags']} \nAdress: {user['Adress']} "
        # else:
        #     return color("This phone dont exist in addressbook",Colors.red)
    return color("Done",Colors.blue)

def help(tst=""):
    instruction = """
    \nCOMMANDS\n
    show all
    add user <FirstName_LastName> <phone>
    add phone <user> <phone>
    add email <user> <email>
    add birthday <user> <date>
    add tags <user> <tags>
    add adress <user> <adress>
    change adress <user> <new_adress>
    change email <user> <oldEmail> <newEmail>
    change birthday <user> <newBirthday>
    remove phone <user> <phone>
    remove email <user> <email>
    remove birthday <user>
    remove phone <user> <phone>
    remove email <user> <email>
    remove tags <user> <tags>
    remove user <user>
    remove adress <user>
    find name <name>
    find tags <tags>
    find phone <phone>
    """
    return instruction


commands = {
    "Help": help,
    "add phone": add_phone,
    "add user": add_user,
    "show all": show_all,
    "add email": add_email,
    "add birthday": add_birthday,
    "add tags": add_tags,
    "add adress": add_adress,
    "change adress": change_adress,
    "change phone": change_phone,
    "change email": change_email,
    "change birthday": change_birthday,
    "remove phone": remove_phone,
    "remove email" :remove_email,
    "remove birthday": remove_birthday,
    "remove tags": remove_tags,
    "remove user": remove_user,
    "remove adress": remove_adress,
    "find name": find_name,
    "find tags": find_tags,
    "find phone": find_phone,
#     "sort directory": sort_directory,
#     "birthdays within": birthdays_within,
#     "days to birthday": days_to_birthday
}

def parser(userInput:str):
    if len(userInput.split()) == 2:
        return commands[userInput.strip()], "None"

    for command in commands.keys():
        if userInput.startswith(str(command)):
            text = userInput.replace(command, "")
            command = commands[command]
            # print(text.strip().split())
            return command, text.strip()
        

def main():
    print(background(color("WRITE HELP TO SEE ALL COMMANDS",Colors.blue),Colors.orange))
    while True:
        user_input = input(color("Enter your command: ",Colors.green)).strip().lower()
        if user_input in STOPLIST:
            print(color("Good bye!..",Colors.yellow))
            break

        elif user_input == "help":
            print(help())
            continue

        elif (len(user_input.split())) == 1:
            print(color("Please write full command", Colors.red))
            continue
        else:
            try:
                command, text = parser(user_input)
                print(command(text))
            except KeyError:
                print(color("You enter wrong command Keyerror", Colors.purple))
            except Error:
                print(color("You enter wrong command Error", Colors.purple))
            except TypeError:
                print(color("You enter wrong command TypeError", Colors.purple))
            except IndexError:
                print(color("You enter wrong command IndexError", Colors.purple))
            except ValueError:
                print(color("You enter wrong command IndexError", Colors.purple))




if __name__ == "__main__":
    main()


        


