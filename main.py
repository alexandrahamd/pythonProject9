import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    data_file = 'file.json'

    def get_file(self):
        with open(self.data_file, 'w', encoding='utf8') as f:
            return json.load(f)

    def do_GET(self):
        result = json.dumps(self.get_file())

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.end_headers()
        self.wfile.write(bytes(result, 'utf8'))


if __name__ == '__main__':
    webServer = HTTPServer((hostName, serverPort), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()


