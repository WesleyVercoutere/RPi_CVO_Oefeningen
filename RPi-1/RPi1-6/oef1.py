#############################################################
##  Wesley Vercoutere                                      ## 
##  CVO Focus                                              ## 
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Les 6 - Oef 1                                          ##  
#############################################################

'''
Oef 1 
Stuur met een GUI een led verbonden met GPIO 25. 
Plaats een knop ON en een knop OFF op je GUI

Oef2 
Stuur met een GUI een led verbonden met GPIO 25. 
Plaats een knop TOGGLE op je GUI

Oef3 
Herhaal oef 1 en 2 en toon in de GUI de status van een LED ( 0 of 1) in een label

Oef4
Gebruik een slider om de knippersnelheid van je LED in te stellen tussen 1 en 10 keer per seconde

Oef5
Gebruik een slider om de tijdsduur van je LED in te stellen tussen 1 en 100 seconden.
Met een knop met opschrift “LICHT” start je de led met de ingestelde tijd.
Uitbreiding : Geef feedback over de status met kleuren of met afbeeldingen ( zelf opzoeken hoe dat moet)

Oef6 schrijf de toestand aan een RP-pin 1 of 0 in een label!

Of7 Verander de kleur van een label van groen naar rood indien input van gesloten naar open verandert! 

Oef8 toon een open of gesloten schakelaar in je GUI die de toestand van je schakelaar aan een pin volgt.

'''

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



