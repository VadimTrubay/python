with open('data.txt', 'wb+') as fh:
    byte_str = 'some text'.encode()
    fh.write(byte_str)

with open('data.txt') as f:
    for i in f:
        print(i)
