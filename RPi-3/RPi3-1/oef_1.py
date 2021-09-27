import RPi.GPIO as GPIO
import time 
import socket

LED_RED = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_RED, GPIO.OUT, initial=GPIO.HIGH)

def led_on():
    GPIO.output(LED_RED, GPIO.HIGH)

def led_off():
    GPIO.output(LED_RED, GPIO.LOW)

def led_toggle():
    GPIO.output(LED_RED, not GPIO.input(LED_RED))

  
PORT=7808
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(5)

request=b""
conn = None

# trukje om IP-adres van je RP te dedecteren
def get_ip_address():
    ip_address = ''
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
                message = request.decode("UTF-8")

                if message == "on":
                    led_on()

                if message == "off":
                    led_off()

                if message == "toggle":
                    led_toggle()

                print("len request =",len(request))
                print("message from client=",request.decode("UTF-8"))
            
            else:
                print("client disconnected")
                break

                
except Exception as e:
    print("Except>" , e)

finally:
    print("Finished!")
