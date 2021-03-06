import serial
import time
import datetime

from service.observer.Observer import Observer


class BluetoothInterface(Observer):

    def __init__(self, conveyorManager, bluetoothController):
        self.conveyorMgr = conveyorManager
        self.conveyorMgr.addObserver(self)

        self.bluetoothCtrl = bluetoothController
        
        self.port = None
        self.msg = b""
        self.msgstr = ""

        self.setup()

    def setup(self):
        self.port = serial.Serial("/dev/ttyS0",9600)

    def readMessage(self):
        c = self.port.read()
            
        if c == b'\n':
            self.msgstr = self.msg.decode()
            self.handleInput(self.msgstr)

            self.msg=b""
            self.msgstr=""

        elif c==b'\r':
            pass
        
        else:
            self.msg +=c

    def handleInput(self, message):
        # Messages:
        # step:-1
        # step:+1
        # pos:1
        # pos:2
        # prog:prog

        try:
            message = message.split(":")
        except:
            self.conveyorMgr.broadcastMessage("Wrong input via bluetooth module")
            return

        if message[0] == "step":
            self.bluetoothCtrl.btnMoveOneStep_clicked(int(message[1]))

        elif message[0] == "pos":
            self.bluetoothCtrl.btnMoveToPosition_clicked(int(message[1]))

        elif message[0] == "prog":
            self.bluetoothCtrl.btnProgramPosition_clicked()

        else: 
            self.conveyorMgr.broadcastMessage("Wrong input via bluetooth module")

    def update(self, *args, **kwargs):
        message = kwargs["message"]
        message = f"{message}\n"
        self.port.write(message.encode())

    def loop(self):
        while self.port.inWaiting()>0:
            self.readMessage()
