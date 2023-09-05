import socket

message = {'2023-04-20, 10:14:10': {'username': 'vad', 'message': '1'}}


def client_program():
    host = '127.0.0.1'
    port = 8000
    server = host, port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = str(message).encode()
    sock.sendto(bytes(data), server)
    print('ok')
    sock.close()


if __name__ == '__main__':
    client_program()
