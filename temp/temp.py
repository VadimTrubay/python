def formatted_numbers():
    a = ["|{0:^10}|{1:^10}|{2:^10}|".format('decimal', 'hex', 'binary')]
    for i in range(16):
        s = "|{0:^10d}|{0:^10x}|{0:^10b}|".format(i)
        a.append(s)
    return a

for el in formatted_numbers():
    print(el)

