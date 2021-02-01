import serial  # check je devices met ls -lh /dev/*
import time


port = serial.Serial("/dev/ttyS0",9600) # vergeet niet de serial console te disabelen in het configuratischerm

c=0
# msg=[]  dan komen alle bytes in een list  bij msg=b"" komen alle bytes in een byte string
msg=b""
msgstr=""

while 1:

    # check incoming serial data
    if port.inWaiting()>0:
        c=port.read()  # komt binnen als byte
        print("c=",c)
        if c==b'\n':
            #print("message=",msg)
            msgstr=msg.decode()  # 
            print("messagestr=",msgstr)
            msg=b""
            msgstr=""
        elif c==b'\r':
            pass
        else:
            #msg+=str(c)  # add string aan string
            msg +=c  # add byte aan byte string
            #print("msg=",msg)
            #print(type(msg))
