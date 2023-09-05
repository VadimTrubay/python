
def encode(data):
    a = []
    count = 1
    b = data[0]
    while True:
        if len(data) == 1:
            a.append(b)
            a.append(count)
            return a
        else:
            if data[0] == data[1]:
                count += 1
                b = data[1]
                data.remove(data[0])
            else:
                a.append(b)
                a.append(count)
                return a + encode(data[1:])

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))
