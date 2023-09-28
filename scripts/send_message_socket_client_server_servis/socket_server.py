import socket
import json


def run_socket():
    host = '127.0.0.1'
    port = 8000
    print('Server is running, please, press ctrl+c to stop')
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server = host, port
        sock.bind(server)
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
    run_socket()