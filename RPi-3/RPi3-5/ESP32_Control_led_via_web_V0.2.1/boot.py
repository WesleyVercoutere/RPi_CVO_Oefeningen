import socket
import network


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.active(True)
        wlan.ifconfig(('192.168.0.20', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        # wlan.connect('SSID', 'KEY')
        print("Add SSID en passwd!!!")

        while not wlan.isconnected():
            pass
        
    print('network config:', wlan.ifconfig())
    
do_connect()
