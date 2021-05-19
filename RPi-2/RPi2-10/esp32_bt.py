import machine
import time

uart1 = machine.UART(1, baudrate=9600, tx=33 , rx=32 )

led = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

uart1.write("Hello from esp32!\n")

msg_b = b''

while True:
    if uart1.any() > 0:
        c = uart1.read(1)
        print("c=",c)
        if c == b'\n':
            if msg_b == b'on':
                led.value(1)
            else:
                led.value(0)
                
            msg_b=b'' # clear buffer
            
        elif c == b'\r':
            pass
        
        else:
            msg_b += c
            print("msg_b=",msg_b)