from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import mimetypes
import pathlib
from datetime import datetime
import socket


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        if pr_url.path == '/':
            self.send_html_file('index.html')
        elif pr_url.path == '/message':
            self.send_html_file('message.html')
        else:
            if pathlib.Path().joinpath(pr_url.path[1:]).exists():
                self.send_static()
            else:
                self.send_html_file('error.html', 404)

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        data_parse = urllib.parse.unquote_plus(data.decode())
        data_dict = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}
        time = datetime.now()
        str_time = time.strftime('%Y-%m-%d, %H:%M:%S')
        data_response = {str_time: data_dict}
        print(data_response)
        self.save_to_json(data_response)
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def save_to_json(self, data_response):
        host = '127.0.0.1'
        port = 8000
        server = host, port
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data = str(data_response).encode()
        sock.sendto(bytes(data), server)
        print('ok')
        sock.close()

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", 'text/plain')
        self.end_headers()
        with open(f'.{self.path}', 'rb') as file:
            self.wfile.write(file.read())


def run_http(host, port, server_class=HTTPServer, handler_class=HttpHandler):
    print('Server is running, please, press ctrl+c to stop')
    server_address = (host, port)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT1 = 3000
    run_http(HOST, PORT1)


