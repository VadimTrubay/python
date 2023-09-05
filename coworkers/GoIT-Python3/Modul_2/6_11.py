def format_string(string, length):
    if len(string) >= length:
        return string
    elif len(string) < length:
         space = (length - len(string)) // 2
         return (space * " " + string)


print(format_string("Привет", 19))