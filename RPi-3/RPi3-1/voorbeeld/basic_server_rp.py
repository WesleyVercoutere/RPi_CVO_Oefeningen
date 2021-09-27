'''
RP3-L4  Socket TCP server , test met Hercules!

'''
import socket
  
PORT=7808
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(5)

request=b""
conn = None

# trukje om IP-adres van je RP te dedecteren
def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 print("s.getsockname()=",s.getsockname())
 ip_address = s.getsockname()[0]
 print("ip_address=",ip_address)
 s.close()
 return ip_address

try:
    while True:

        print("Server is waiting for a connection at",get_ip_address(), "and port", PORT)
        conn, addr = s.accept()
        print('Server got a connection from' , addr)
        while True:
            request = conn.recv(2048)
            if len(request)> 0:
                print("len request =",len(request))
                print("message from client=",request.decode("UTF-8"))
            else:
	    print(“client disconnected”)
                break

except Exception as e:
    print("Except>" , e)

finally:
    print("Finished!")