import serial
import time
import datetime

time_stamp = datetime.datetime.now().strftime('%S')

#port = serial.Serial("/dev/ttyS0",115200)
port = serial.Serial("/dev/ttyAMA0",9600)
c=0
# msg=[]  dan komen alle bytes in een list
msg=b""
msgstr=""

while 1:
    if datetime.datetime.now().strftime('%S') != time_stamp:
        time_stamp = datetime.datetime.now().strftime('%S')
        port.write("testje op RP\n".encode())
        
    while port.inWaiting()>0:
        c=port.read()  # komt binnen als byte
        print("c=",c)
        if c==b'\n':
            #print("message=",msg)
            msgstr=msg.decode()
            print("messagestr=",msgstr)
            #key, value= analyse(msgstr)
            msg=b""
            msgstr=""
        elif c==b'\r':
            pass
        else:
            #msg+=str(c)  # add string aan string
            msg +=c  # add byte aan byte string
            #print("msg=",msg)
            #print(type(msg))

