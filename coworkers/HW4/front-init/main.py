import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import urllib.parse
import mimetypes
import pathlib
from threading import Thread
import logging
import multiprocessing
import os
import json
class HttpSite(BaseHTTPRequestHandler):

    def do_GET(self):
        url= urllib.parse.urlparse(self.path)
        print(url.path)
        if url.path == "/":
            self.send_html("index.html")
        else:
            if pathlib.Path().joinpath(url.path[1:]).exists():
                self.send()
            else:
                self.send_html("error.html")
    

    def do_POST(self):

        length = self.headers.get('Content-Length')
        data = self.rfile.read(int(length))

        logging.info(f'data = {data} ')

        send_data_to_socket(data)
        self.send_response(302)
        self.send_html("message.html")
        self.end_headers()

    

    def send(self):
        self.send_response(200)
        typem = mimetypes.guess_type(self.path)
        if typem:
            self.send_header("Content-type", typem[0])
        else:
            self.send_header("Content-type", "text/plain")

        self.end_headers()
        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())

    def send_html(self, filename, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename,"rb") as file:
            self.wfile.write(file.read())

def save_to_json(data:str):
    data = data.decode().split("&")
    data = [lst.split("=") for lst in data]
    data = {k: v for k,v in [lst for lst in data]}
    current_date = datetime.datetime.now()
    info = {str(current_date): data}
    
    if pathlib.Path("storage/data.json").exists():
        oldjson = json.load(open(pathlib.Path("storage/data.json")))
        oldjson.update(info)
        json.dump(oldjson, open(pathlib.Path("storage/data.json"), "w"))

    else:
        with open(pathlib.Path("storage/data.json"), "w") as file:
            dump = json.dump(info, file)



def send_data_to_socket(data):
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c_socket.sendto(data,("127.0.0.1", 6000))
    c_socket.close()

def run():
    print("HTTP-SERV STARTED")
    address = ("127.0.0.1",3000)
    http = HTTPServer(address, HttpSite)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


def socket_serv():
    print("SOCKET STARTED ")
    with socket.socket() as sock:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(("127.0.0.1", 6000))
        try:
            while True:
                data, adress = sock.recvfrom(1024)
                save_to_json(data)
        except KeyboardInterrupt:
            print("Close server")
        finally:
            sock.close()

#З Потоками не працюе, запускаеться лише 1 поток чомусь а инши не
# if __name__== "__main__":
#     logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")

#     socketThread = Thread(target= socket_serv)
#     socketThread.run()

#     httpThread = Thread(target = run)
#     httpThread.run()
#     send_data_to_socket(b"hello dima")

if __name__ == "__main__":
    multiprocessing.Process(target=run).start()
    multiprocessing.Process(target=socket_serv).start()