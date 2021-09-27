''' https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
4.2. Sockets
Once the WiFi is set up the way to access the network is by using sockets. A socket represents an endpoint on a network device,
and when two sockets are connected together communication can proceed.
Internet protocols are built on top of sockets, such as email (SMTP), the web (HTTP), telnet, ssh, among many others.
Each of these protocols is assigned a specific port, which is just an integer.
Given an IP address and a port number you can connect to a remote device and start talking with it.

The next part of the tutorial discusses how to use sockets to do some common and useful network tasks.

'''

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

# The first thing to do is make sure we have the socket module available:
import socket

#Then get the IP address of the server:
addr_info = socket.getaddrinfo("192.168.0.170", 5555)

#The getaddrinfo function actually returns a list of addresses, and each address has more information than we need.
#We want to get just the first valid address,
#and then just the IP address and port of the server. To do this use:
addr = addr_info[0][-1] 
print(addr_info)  # [(2, 1, 0, '192.168.0.172', ('192.168.0.172', 8899))]
print(addr)  # ('192.168.0.172', 8899)

#Using the IP address we can make a socket and connect to the server:
s = socket.socket()
s.connect(addr)
#Now that we are connected we can download and display the data:
while True:
    data = s.recv(500)  # blocking code
    print(str(data, 'utf8'), end='')
