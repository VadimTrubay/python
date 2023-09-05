'''Разработайте функцию sanitize_file(source, output), переписывающую в текстовый файл output
содержимое текстового файла source, очищенное от цифр.

Требования:

прочтите содержимое файла source, используя менеджер контекста with и режим "r".
запишите новое очищенное от цифр содержимое файла output, используя менеджер контекста with и режим "w"
запись нового содержимого файла output должна быть единоразовая и использовать метод write'''

def sanitize_file(source, output):
    with open(source, 'r') as reader:
        with open(output, 'w') as writer:
            rh = reader.read()
            san_rh = rh.strip().replace('0', '').replace('1', '').replace('2', '').replace('3', '') \
        .replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
            writer.write(san_rh) 





