import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

naar_pin_in1 = 22
naar_pin_in2 = 27
naar_pin_in3 = 17
naar_pin_in4 = 4

GPIO.setwarnings(False)
GPIO.setup(naar_pin_in1, GPIO.OUT)
GPIO.setup(naar_pin_in2, GPIO.OUT)
GPIO.setup(naar_pin_in3, GPIO.OUT)
GPIO.setup(naar_pin_in4, GPIO.OUT)

links= [[1,0,0,0],[0,0,0,1],[0,0,1,0],[0,1,0,0]]
rechts=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def stuur_spoelen(pins):
    GPIO.output(naar_pin_in1,pins[0])
    GPIO.output(naar_pin_in2,pins[1])
    GPIO.output(naar_pin_in3,pins[2])
    GPIO.output(naar_pin_in4,pins[3])

def map_value(incoming_value, min_incoming , max_incoming , min_outgoing , max_outgoing):
    return min_outgoing + (max_outgoing - min_outgoing) * ((incoming_value - min_incoming) / (max_incoming - min_incoming))     

def draailinks(wacht):
    for step in range (0,4):
        stuur_spoelen(links[step])
        time.sleep(wacht/1000)
        
def draairechts(wacht):
    for step in range (0,4):
        stuur_spoelen(rechts[step])
        time.sleep(wacht/1000)
    
while True:
    for steps in range(509):
        draairechts(2)
        
    time.sleep(1)
        
    for steps in range(509):
        draailinks(2)
        
    time.sleep(1)    
       

