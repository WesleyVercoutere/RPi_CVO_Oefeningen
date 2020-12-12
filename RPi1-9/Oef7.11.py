#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 9 - Oef 7.11                                       ##
#############################################################

'''
7.11) Stuur je servo-motor van links naar rechts met je potentiometer.
'''

try:
    import RPi.GPIO as GPIO
    from gpiozero import MCP3008
except:
    # from dummygpio.DummyGPIO import DummyGPIO
    # GPIO = DummyGPIO(True)
    print("No Raspberry Pi found")


# GPIO general
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

mcp3008_channel_0 = MCP3008(channel=0, device=0)

GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18, 50)  # channel=14  frequency=50Hz
p.start(0)

dc = 0
prevDc = 0

def scale(value):
    global dc

    inputMin = 1
    inputMax = 1023
    outputMin = 2
    outputMax = 10

    dc = int((value - inputMin)*(outputMax-outputMin)/(inputMax-inputMin)+outputMin)

while True:
    # print(mcp3008_channel_0.value)
    # print(mcp3008_channel_0.raw_value)

    scale(mcp3008_channel_0.raw_value)
    if dc != prevDc:
        print(dc)
        prevDc = dc

    p.ChangeDutyCycle(dc)