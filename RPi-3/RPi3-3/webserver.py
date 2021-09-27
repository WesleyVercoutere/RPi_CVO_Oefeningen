'''httpserver met juiste Content-Length header en html bericht uit file! 
'''
import socket
import sys

PORT=7806

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', PORT))
s.listen(1)

print(socket.gethostbyname(socket.gethostname()))
request=b""

def antwoord_browser(bestands_naam, type_bestand):
    try:
        if type_bestand=="html":
            f=open(bestands_naam,"r") # default "rt" not needed to specify   b for binary ...
        elif type_bestand=="jpg" or type_bestand=="favicon" or type_bestand=="png" :
            f=open(bestands_naam,"rb") # default "rt" not needed to specify   b for binary ...
        else:
            print("else, why?")
            
        response=f.read()
        length_response=len(response)
        print("\nDe respons heeft een lengte=", length_response, "bytes")
        
        conn.send(b"HTTP/1.1 200 OK\r\n")
        
        if type_bestand=="html":
            conn.sendall(b"Content-Type: text/html\r\n")
        elif type_bestand=="jpg":
            conn.sendall(b"Content-Type: imgage/jpg\r\n")
        elif type_bestand=="png":
            conn.sendall(b"Content-Type: image/png\r\n")
        elif type_bestand=="favicon":
            conn.sendall(b"Content-Type: image/ico\r\n")
        else:
            print("no type found!")
            
        content_length_header="Content-Length:"+str(length_response)+"\r\n\r\n"
        conn.sendall(content_length_header.encode("UTF-8"))  # we beginnen te tellen NA de lege lijn!
        if type_bestand=="html":
            conn.sendall(response.encode("UTF-8")) # zet string om naar bytes
        else:
            conn.sendall(response) # 
        conn.close()
    except:
        e=sys.exc_info()[0]
        print("Except in antwoord_browser !!", e)
        conn.close()      

try:
    while True:
        print("Server is waiting for a connection at",socket.gethostbyname(socket.gethostname()), "and port", PORT)
        conn, addr = s.accept()
        print('Server got a connection from' , addr)
        
        request = conn.recv(2048)
        #print("message from client=",request)
        print("len request =",len(request))
        print("message from client=",request.decode("UTF-8"))
        
        if len(request) > 0:                  
           
            if b"GET / HTTP" in request or b"GET /index.html" in request:                
                antwoord_browser("index.html","html")                
                
            elif b"GET /my_data.html" in request:
                 antwoord_browser("my_data.html","html")                  
            elif b"GET /my_hobbies.html" in request:
                antwoord_browser("my_hobbies.html","html")                   
            elif b"GET /my_work.html" in request:            
                antwoord_browser("my_work.html","html")             
                
            elif b"GET /favicon.ico" in request:
                antwoord_browser("favicon.ico","favicon")   
                
            elif b"wim.jpg" in request:
                antwoord_browser("wim.jpg","jpg")
                
            elif b"pianoles.jpg" in request:
                antwoord_browser("pianoles.jpg","jpg")
                
            elif b"iotsolutions.png" in request:
                antwoord_browser("iotsolutions.png","png")
                
            elif b"cvofocus.jpg" in request:
                antwoord_browser("cvofocus.jpg","jpg")
                
            elif b"piano.png" in request:
                antwoord_browser("piano.png","png")
                
            elif b"programmeren.jpg" in request:
                antwoord_browser("programmeren.jpg","jpg")
                
            elif b"joggen.jpg" in request:
                antwoord_browser("joggen.jpg","jpg")
                
            elif b"hiking2.jpg" in request:
                antwoord_browser("hiking2.jpg","jpg")
                
            elif b"schaken.jpg" in request:
                antwoord_browser("schaken.jpg","jpg")
                
            elif b"gegevens.jpg" in request:
                antwoord_browser("gegevens.jpg","jpg")
                                           
                
            print("\nServer closed connection!")

except:
    e=sys.exc_info()[0]
    print("Except in main!!", e)
          

        
        
        






