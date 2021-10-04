import socket
import network


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.ifconfig(('192.168.0.20', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        sta_if.connect('SSID', 'KEY')

        while not sta_if.isconnected():
            pass
        
    print('network config:', sta_if.ifconfig())  #network config: ('192.168.0.110', '255.255.255.0', '192.168.0.1', '42.2.24.0')
    
do_connect()
