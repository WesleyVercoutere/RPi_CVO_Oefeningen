'''httpserver met juiste Content-Length header en html bericht uit file! 
'''
from RequestObject import RequestObject
import socket
import sys

class WebServer:

    def __init__(self) -> None:
        self.PORT = 8080
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('0.0.0.0', self.PORT))
        self.socket.listen(1)

        self.conn = None

    def run(self) -> None:
        try:
            while True:
                print("Server is waiting for a connection at",self._get_ip_address(), "and port", self.PORT)
                print()
                self.conn, addr = self.socket.accept()
                request = self.conn.recv(2048)
                
                if len(request) > 0:                  
                    self._handle_request(request)
                                                
                else:
                    print("client disconnected")
                    break

        except Exception as ex:
            e=sys.exc_info()[0]
            print("Except in main!!", ex)

    def _get_ip_address(self) -> str:
        ip_address = ''
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        print("s.getsockname()=",s.getsockname())
        ip_address = s.getsockname()[0]
        print("ip_address=",ip_address)
        print()
        s.close()
        return ip_address

    def _handle_request(self, request) -> None:
        request_obj = self._filter_request(request)
        self._respond(request_obj)
        
    def _filter_request(self, request) -> RequestObject:
        r = request.decode("utf-8")
        r = r.split('\n')[0]
        print(r)
        r = r.split(' ')[1]
        print(r)

        obj = RequestObject()

        if r == "/":
            obj.filename = "index.html"
            obj.filetype = "html"
        else:
            obj.filename = r[1:]
            obj.filetype = r.split(".")[1]

        return obj
        
    def _respond(self, request_obj: RequestObject):
        try:
            path = "/home/weve/Documents/RPi_CVO_Oefeningen/RPi-3/RPi3-3/src/resources/"

            if request_obj.filetype == "html":
                f = open(f"{path}html/{request_obj.filename}", "r")

            elif request_obj.filetype == "jpg" or request_obj.filetype == "favicon" or request_obj.filetype == "png" :
                f =open(f"{path}images/{request_obj.filename}", "rb")
            
            else:
                print("else, why?")
                
            response = f.read()
            length_response = len(response)
            
            self.conn.send(b"HTTP/1.1 200 OK\r\n")
            
            if request_obj.filetype=="html":
                self.conn.sendall(b"Content-Type: text/html\r\n")
            elif request_obj.filetype=="jpg":
                self.conn.sendall(b"Content-Type: imgage/jpg\r\n")
            elif request_obj.filetype=="png":
                self.conn.sendall(b"Content-Type: image/png\r\n")
            elif request_obj.filetype=="favicon":
                self.conn.sendall(b"Content-Type: image/ico\r\n")
            else:
                print("no type found!")
                
            content_length_header="Content-Length:"+str(length_response)+"\r\n\r\n"
            self.conn.sendall(content_length_header.encode("UTF-8"))

            if request_obj.filetype == "html":
                self.conn.sendall(response.encode("UTF-8"))
            else:
                self.conn.sendall(response)
            self.conn.close()
        
        except Exception as ex:
            e=sys.exc_info()[0]
            print("Except in antwoord_browser !!", ex)
            self.conn.close()      
        
if __name__ == "__main__":
    app = WebServer()
    app.run()
