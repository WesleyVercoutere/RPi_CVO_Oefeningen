# Enable I2C bus op je Raspberry Pi
# ls /dev/*i2c* in terminal 
#Zoekresultaten The OSError: [Errno 121] Remote I/O error indicates that an I2C device is not connected to the bus.
# use i2cdetect -y 1 in terminal to scan I2C bus
# datasheet
#IOL LOW-level output current VOL = 1 V; VDD =5V 10 25 - mA
#IOH HIGH-level output current VOH = VSS 30 - 300 A
#The pull up resistors are necessary. The Pi's SDA and SCL lines have physical resistors on the board to pull up to 3.3V.

import smbus
import time 

bus = smbus.SMBus(1)

addressPCF8574 = 0x20

bus.write_byte(addressPCF8574, 0xFF)# put all pins as inputs
 
while True:
    print("{0:b}".format(bus.read_byte(addressPCF8574))) # print("{0:b}".format(a))
    time.sleep(0.5)