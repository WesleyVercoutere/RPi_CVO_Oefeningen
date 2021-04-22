import smbus
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)

bus = smbus.SMBus(1)

addressPCF8574 = 0x20

def interrupt(pin):

    byte_gelezen = bus.read_byte(addressPCF8574)
    print(byte_gelezen)

GPIO.add_event_detect(18, GPIO.FALLING, callback=interrupt)

bus.write_byte(addressPCF8574, 0b11111111)

byte_gelezen = 0 

while 1:

    pass
