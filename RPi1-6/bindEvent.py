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

try:
    import RPi.GPIO as GPIO
except:
    import DummyGPIO as GPIO

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


root = Tk()
root.title("Oefening 1")
root.geometry("800x400")


click1 = Button(root, text="Blauwe led")
click2 = Button(root, text="Rode led")
click3 = Button(root, text="Gele led")
click4 = Button(root, text="Groene led")

click1.bind("<ButtonPress-1>", )

click1.place(x=10, y=10)
click2.place(x=10, y=60)
click3.place(x=10, y=110)
click4.place(x=10, y=160)

def mouseDown(event):
    print("mouse down")

def btnRelease(event):
    print("mouse up")

click1.bind("<ButtonPress-1>", mouseDown)
click1.bind("<ButtonRelease-1>", btnRelease)

while True:
    for index in range(len(buttons)):
        pass
        #if clicked[index]:
        #    GPIO.output(leds[index], GPIO.input(buttons[index]) or clicked[index])

    root.update()




#if __name__ == "__main__":
#     pass



