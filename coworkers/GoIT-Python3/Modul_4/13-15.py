message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ch in "abcdefghijklmnopqrstuvwxyz":
        pos = (ord(ch) + offset - ord('a')) % 26 
        encoded_message += chr(pos + ord("a"))
    elif ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        pos = (ord(ch) + offset - ord('A')) % 26
        encoded_message += chr(pos + ord("A"))
    else:
        encoded_message += ch
    

print(encoded_message)
    