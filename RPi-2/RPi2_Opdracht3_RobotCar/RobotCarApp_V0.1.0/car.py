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

#Start program
enablePin.off()
pwmM1.on()
pwmM2.on()
pwmM3.on()
pwmM4.on()

motorloop = [[0,0,0,0,0,0,0,1],  # M4 - vooruit
             [0,0,0,0,0,0,1,0],  # M2 - achteruit
             [0,0,0,0,0,1,0,0],  # M1 - vooruit
             [0,0,0,0,1,0,0,0],  # M1 - achteruit
             [0,0,0,1,0,0,0,0],  # M2 - vooruit
             [0,0,1,0,0,0,0,0],  # M3 - achteruit
             [0,1,0,0,0,0,0,0],  # M4 - achteruit
             [1,0,0,0,0,0,0,0]]  # M3 - vooruit

carMoveForward =  [1,0,0,1,0,1,0,1]
carMoveBackward = [0,1,1,0,1,0,1,0]
carTurnLeft =  [1,0,0,0,1,0,1,1]
carTurnRight = [0,1,1,1,0,1,0,0]
carOff = [0,0,0,0,0,0,0,0]

def writeToShield():
    latchPin.on()
    time.sleep(0.001)
    latchPin.off()
    
def move(direction):
    for i in range(8):
        messagePin.value(direction[i])
        clockPin.on()
        time.sleep(0.001)
        clockPin.off()
        writeToShield()

move(carMoveForward)
time.sleep(5)
move(carOff)
time.sleep(0.5)

move(carMoveBackward)
time.sleep(5)
move(carOff)
time.sleep(0.5)

move(carTurnLeft)
time.sleep(5)
move(carOff)
time.sleep(0.5)
    
move(carTurnRight)
time.sleep(5)
move(carOff)


while True:
    
    ledOnBoard.on()
    time.sleep(0.25)
    ledOnBoard.off()
    time.sleep(0.25)
    
    
    
    '''
    for i in range(8):
        print(i)
        
        for j in range(8):
            messagePin.value(motorloop[i][j])
            clockPin.on()
            time.sleep(0.001)
            clockPin.off()
        
        latchPin.on()
        time.sleep(0.001)
        latchPin.off()
        time.sleep(5)
    '''        
    