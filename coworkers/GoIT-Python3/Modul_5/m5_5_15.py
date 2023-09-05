'''Задача: Сортировка списка телефонных номеров
Задание
Вернемся к нашей задаче с телефонными номерами. 
Компания расширяется и вышла на рынок Азии. 
Теперь в списке приходят телефоны разных стран. 
Каждая страна имеет свой телефонный код.

Компания работает со следующими странами

Страна	Код ISO	Префикс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Чтобы мы могли корректно выполнить маркетинговую SMS кампанию, 
необходимо выдать для каждой страны свой список телефонных номеров.

Напишите функцию get_phone_numbers_for_сountries, которая будет:

Принимать список телефонных номеров.
Санитизировать (нормализовать) полученный список телефонов клиентов 
с помощью нашей функции sanitize_phone_number.
Сортировать телефонные номера по указанным в таблице странам.
Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
{
    "UA" : [<здесь список телефонов>],
    "JP": [<здесь список телефонов>],
    "TW": [<здесь список телефонов>],
    "SG": [<здесь список телефонов>]
}
Если не удалось сопоставить код телефона с известными, 
этот телефон должен быть добавлен в список словаря с ключом "UA".'''



def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
        # .replace("3", "")
        # .replace("8", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    dict = {}
    UA_list =[]
    JP_list =[]
    TW_list =[]
    SG_list =[]
    start = 0
    end = 3
    for number in list_phones:
        number = sanitize_phone_number(number)
        if number.find("81", start, end)==0:
            JP_list.append(number)
            continue
        if number.find('886', start, end)==0:
            TW_list.append(number)
            continue
        if number.find('65', start, end)==0:
            SG_list.append(number)
            continue
        else:
            UA_list.append(number)
    dict = {'UA':UA_list, 'JP':JP_list, 'TW':TW_list, 'SG':SG_list}
    return dict  
 


print(get_phone_numbers_for_countries(['065-875-94-11', '(81)8765347', '8867658976', '657658976', '(65)765-89-77']))

