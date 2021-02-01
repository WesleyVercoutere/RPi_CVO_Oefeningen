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
        if c==b'\n':
            #print("message=",msg)
            msgstr=msg.decode()  # 
            print("messagestr=",msgstr)

            msgList = msgstr.split("/")
            key = msgList[0]
            value = msgList[1]

            print(f"key = {key}, value = {value}")
            
            send = f"echo : {msgstr}\n"
            port.write(send.encode("utf8"))

            msg=b""
            msgstr=""
        elif c==b'\r':
            pass
        else:
            msg +=c  # add byte aan byte string
