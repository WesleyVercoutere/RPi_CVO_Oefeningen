#############################################################
##  Wesley Vercoutere                                      ## 
##  CVO Focus                                              ## 
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 6 - Oef 1                                          ##  
#############################################################

'''
Setup breadbord:

ledBlue = pin 19
ledRed = pin 20
ledYellow = pin 21
ledGreen = pin 22

button 1 = pin 23
button 2 = pin 24
button 3 = pin 25
button 4 = pin 26
'''

from tkinter import *
import RPi.GPIO as GPIO

ledBlue = 19
ledRed = 20
ledYellow = 21
ledGreen = 22

button1 = 23
button2 = 24
button3 = 25
button4 = 26

leds = (ledBlue, ledRed, ledYellow, ledGreen)
buttons = (button1, button2, button3, button4)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for led in leds:
    GPIO.setup(led, GPIO.OUT)

for btn in buttons:
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    for index in range(len(buttons)):
        GPIO.output(leds[index], GPIO.input(buttons[index]))




#if __name__ == "__main__":
#     pass
