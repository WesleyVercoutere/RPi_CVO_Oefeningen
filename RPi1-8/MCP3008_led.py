import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

led = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

mcp3008_channel_0 = MCP3008(channel=0, device=0)

p = GPIO.PWM(led, 50)  # channel=14  frequency=50Hz
p.start(0)

dc = 0
prevDc = 0

def scale(value):
    global dc

    inputMin = 1
    inputMax = 1023
    outputMin = 0
    outputMax = 100

    dc = int((value - inputMin)*(outputMax-outputMin)/(inputMax-inputMin)+outputMin)

while True:
    # print(mcp3008_channel_0.value)
    # print(mcp3008_channel_0.raw_value)

    scale(mcp3008_channel_0.raw_value)
    if dc != prevDc:
        print(dc)
        prevDc = dc

    p.ChangeDutyCycle(dc)
    