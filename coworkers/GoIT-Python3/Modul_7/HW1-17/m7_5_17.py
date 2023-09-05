'''Очень часто люди в своих сообщениях не ставят заглавные буквы, особенно это стало массовым явлением
в эру мобильных устройств. Разработайте функцию capital_text, которая будет принимать на вход строку c текстом
 и возвращать строку с восстановленными заглавными буквами.

Функция должна:

сделать заглавной первую букву в строке, несмотря на пробелы
сделать заглавной первую букву после точки, несмотря на пробелы
сделать заглавной первую букву после восклицательного знака, несмотря на пробелы
сделать заглавной первую букву после вопросительного знака, несмотря на пробелы'''

# s = 'alert. boss! oh'
def capital_text(s:str):
    sign = True
    result_string = ''
    for ch in s:
        if ch in "!?.":
            result_string = result_string + ch
            sign = True
            continue
        if ch not in "!?. " and sign == True:
            result_string = result_string + ch.title()
            sign = False
        else:
            result_string = result_string + ch
    return result_string






print(capital_text('alert. boss! oh'))
print(capital_text('hello world! awesome? yes'))