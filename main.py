from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "172.17.51.174"
port = 80

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("What's deeze?", "utf-8"))
        print(self.client_address)

    def do_POST(self):
        print("Ahh")
        self.send_response(200)
        print(self.client_address)


def start():
    if __name__ == "__main__":
        serverLol = HTTPServer((hostName, port), Server)
        print("Starting")
        try: 
            serverLol.serve_forever()
        except KeyboardInterrupt:
            pass
        print("End")

start()