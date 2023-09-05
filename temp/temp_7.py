# import logging
# logging.info('Hello')

# from threading import Thread, RLock
# from time import sleep
#
# lock = RLock()
#
#
# def run_tr(lock, n):
#     lock.acquire()
#     print(f'start{n}')
#     sleep(1)
#     lock.release()
#     print(f'finish {n}')
#
#
# if __name__ == '__main__':
#     threads = []
#     thread1 = Thread(target=run_tr, args=(lock, 1))
#     thread2 = Thread(target=run_tr, args=(lock, 2))
#     thread1.start()
#     thread2.start()


# from threading import Thread, RLock, Semaphore
# from time import sleep
#
#
# def run_tr(n, pool):
#     with pool:
#         print(f'start{n}')
#         sleep(1)
#         print(f'finish {n}')
#
#
# if __name__ == '__main__':
#     pool = Semaphore(3)
#     for i in range(10):
#         thread1 = Thread(target=run_tr, args=(i, pool))
#         thread1.start()
#     print('game over')

# from threading import Thread, RLock, Semaphore, Condition
# from time import sleep
#
#
# def main(condition):
#     with condition:
#         print('start main')
#         sleep(2)
#         condition.notify_all()
#
# def worker(condition):
#     with condition:
#         condition.wait()
#         print('start work')
#
#
# if __name__ == '__main__':
#     condition = Condition()
#     main = Thread(target=main, args=(condition, ))
#     worker = Thread(target=worker, args=(condition, ))
#     worker.start()
#     main.start()
#     print('game over')

# s = '1234567789'
# print(s[1:6:1])

# from jinja2 import Template

# name = 'vad'
# age = 29
# tm = Template("my name is {{name}} and my age is {{age}}")
# msg = tm.render(name=name, age=age)
# print(msg)
#
# persons = [
#     {'name': 'Andrej', 'age': 34},
#     {'name': 'Mark', 'age': 17},
#     {'name': 'Thomas', 'age': 44},
#     {'name': 'Lucy', 'age': 14},
#     {'name': 'Robert', 'age': 23},
#     {'name': 'Dragomir', 'age': 54}
# ]
#
# rows_tmp = Template("""{% for person in persons -%}
#     {{ person.name }} {{ person.age }}
# {% endfor %}""")
#
# print(rows_tmp.render(persons=persons))

# from http.server import BaseHTTPRequestHandler, HTTPServer
# import threading
# from time import sleep
# class Test(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         self.wfile.write(b"hello vad")
#
#     def do_POST(self):
#         pass
#
# server = HTTPServer(('127.0.0.1', 8000), Test)
# server_thread = threading.Thread(target=server.serve_forever())
# server_thread.start()
# sleep(1)
#
# from http import client
# c = client.HTTPConnection('localhost', 8000)
# c.request('GET', '/')
# res = c.getresponse()
# print(res.status, res.reason)
# data = res.read()
# print(data)
# httpd.shutdown()

# from datetime import datetime
# d = datetime.now()
#
# print(d)

# import threading
# import socket
# import pickle

# data_response = {'2023-04-20, 10:14:10': {'username': 'vad', 'message': '1'}}
#
# def send_response():
#     host = '127.0.0.1'
#     port = 5000
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.connect((host, port))
#     sock.send(bytes(f"{data_response.keys()}", encoding='UTF-8'))
#     sock.close()

#
# def run_socket():
#     host = '127.0.0.1'
#     port = 5000
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.bind((host, port))
#     try:
#         while True:
#             data = sock.recv(1024)
#             with open('storage/data.json', 'ab') as f:
#                 pickle.dump(data, f)
#             if not data:
#                 break
#     except KeyboardInterrupt:
#         print(f'Destroy server')
#     finally:
#         sock.close()
#
#
# if __name__ == '__main__':
#     send_response()
#     run_socket()
#     server = threading.Thread(target=send_response, )
#     client = threading.Thread(target=run_socket, )
#     server.start()
#     server.join()
#     client.start()
#     client.join()

# def my_sort(arr):
#     temp = []
#     for i in range(len(arr)):
#         if arr[i] == arr[-1]:
#             break
#         if arr[i] > arr[-1]:
#             temp.insert(0, arr[i])
#         else:
#             temp.insert(-1, arr[i])
#
#     return temp
#
#
# a = [5, 8, 4, 7, 4, 1, 3, 9]
# print(my_sort(a))
# print(sorted(a))








