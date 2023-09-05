import socket
import json


def server_program():
    host = '127.0.0.1'
    port = 8000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server = host, port
    sock.bind(server)
    print('Server is running, please, press ctrl+c to stop')
    data = sock.recv(1024).decode()
    try:
        with open('data.json', 'r') as f:
            js = f.read()
            data = json.loads(js) + data
        with open('data.json', 'w') as f:
            f.write(json.dumps(data + ', '))
    except Exception:
        with open('data.json', 'w') as f:
            f.write(json.dumps(data + ', '))
    sock.close()


if __name__ == '__main__':
    server_program()
