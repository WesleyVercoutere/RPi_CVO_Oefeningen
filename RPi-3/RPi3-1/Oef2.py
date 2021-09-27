from machine import Pin
import time
import socket

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True) # ESP acts as a station and connects to an acces point
        sta_if.connect('telenet-69249', '5E40nQkE42tk') # use your 
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())  #network config: ('192.168.0.110', '255.255.255.0', '192.168.0.1', '42.2.24.0')
    
do_connect()

addr_info = socket.getaddrinfo("192.168.0.251", 7808)

addr = addr_info[0][-1]
print(addr_info)
print(addr)

#Using the IP address we can make a socket and connect to the server:
s = socket.socket()
s.connect(addr)


led = Pin(13, Pin.OUT)
btn = Pin(5, Pin.IN, Pin.PULL_UP)

def callback(pin):
    global s
    s.sendall("toggle")
    time.sleep(0.1)
    
btn.irq(trigger=Pin.IRQ_FALLING, handler=callback)






