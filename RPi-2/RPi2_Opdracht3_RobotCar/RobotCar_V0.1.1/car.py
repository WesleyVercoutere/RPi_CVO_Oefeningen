from machine import *
import time


# Setup ESP 32
ledOnBoard = Pin(2, Pin.OUT)

bt = UART(1, baudrate=9600, tx=33 , rx=32)

enablePin = Pin(21, Pin.OUT)
messagePin = Pin(22, Pin.OUT)
clockPin = Pin(19, Pin.OUT)
latchPin = Pin(23, Pin.OUT)

pwmM1 = Pin(18, Pin.OUT)
pwmM2 = Pin(5, Pin.OUT)

pwmM3 = Pin(17, Pin.OUT)
pwmM4 = Pin(16, Pin.OUT)

# Motor direction settings and methods
carMoveForward =  [1,0,0,1,0,1,0,1]
carMoveBackward = [0,1,1,0,1,0,1,0]
carTurnLeft =  [1,0,0,0,1,0,1,1]
carTurnRight = [0,1,1,1,0,1,0,0]
carOff = [0,0,0,0,0,0,0,0]

def writeToShield():
    latchPin.on()
    time.sleep_us(10)
    latchPin.off()
    
def move(direction):
    for i in range(8):
        messagePin.value(direction[i])
        clockPin.on()
        time.sleep_us(10)
        clockPin.off()
        writeToShield()

# Setup Bluetooth
uart1 = UART(1, baudrate=9600, tx=33 , rx=32 )
uart1.write("Hello from esp32!\n")

bluetoothMessage = b''

def handleBluetoothMessage(message):
    if message == b'forward':
        move(carMoveForward)
        
    elif message == b'backward':
        move(carMoveBackward)
        
    elif message == b'turnLeft':
        move(carTurnLeft)
        
    elif message == b'turnRight':
        move(carTurnRight)
       
    elif message == b'stop':
        move(carOff)
        
    else:
        uart1.write("Wrong command to car!\n")
    
#Start program
enablePin.off()
pwmM1.on()
pwmM2.on()
pwmM3.on()
pwmM4.on()

while True:
    
    if uart1.any() > 0:
        c = uart1.read(1)
        
        if c == b'\n':
            handleBluetoothMessage(bluetoothMessage)
            bluetoothMessage = b'' # clear buffer
            
        elif c == b'\r':
            pass
        
        else:
            bluetoothMessage += c
    