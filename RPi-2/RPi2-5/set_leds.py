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

S5=5
S6=6
S7=7
S8=8

S5_6_7_8={5:0b00010000,6:0b00100000,7:0b01000000,8:0b10000000} 
 
  
def read(schak_nr):
    status = bus.read_byte(addressPCF8574)
    if status & S5_6_7_8[schak_nr]:
        print("S", schak_nr , "= 1")
    else:
        print("S", schak_nr , "= 0")        
    time.sleep(0.5)

    
while 1:
    read(S5)
    read(S6)  
    read(S7)
    read(S8)
    print()
