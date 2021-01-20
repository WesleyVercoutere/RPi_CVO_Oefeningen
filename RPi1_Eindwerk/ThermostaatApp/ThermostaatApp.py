#############################################################
##  Wesley Vercoutere                                      ##
##  CVO Focus                                              ##
##  Deel 1: Basis programmeren in Python met RaspberryPi   ##
##  Eindopdracht: Thermostaat applicatie                   ##
#############################################################

import service.DigitalInput

class ThermostaatApp:

    def __init__(self):
        print("Hello World")

        self.initIO()

        

    def initIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.btn1 = DigitalInput(21)
        self.btn2 = DigitalInput(16)
        self.btnRot = DigitalInput(20)
        self.rotA = DigitalInput(26)
        self.rotB = DigitalInput(19)

    def run(self):
        pass


if __name__ == '__main__':
    ta = ThermostaatApp()
    ta.run()
