from hardware.DigitalInput import DigitalInput
from hardware.RotaryEncoder import RotaryEncoder

'''
-	Drukknop 1 : GPIO 18
-	Drukknop 2 : GPIO 23
-	Drukknop 3 : GPIO 25
-	Drukknop 4 : GPIO 12
-	Drukknop 5 : GPIO 16
-	Drukknop 6 : GPIO 26
-	Rotary A : GPIO 20
-	Rotary B : GPIO 21
-	Potentiometer : MCP 3008 channel 1
-	MCP3008 :
    o	CLK : GPIO 11 / SPIO SCLK
    o	Dout : GPIO 9 / SPIO MISO
    o	Din : GPIO 10 / SPIO MOSI
    o	CS/Sh : GPIO 8 / SPIO CS1

-	Led green : GPIO 5
-	Led yellow : GPIO 6
-	Led blue : GPIO 13
-	Led red : GPIO 19
-	Stepper motor
    o	In 1 : GPIO 17
    o	In 2 : GPIO 27
    o	In 3 : GPIO 22
    o	In 4 : GPIO 23
'''


class HardwareManager:

    def __init__(self):
        self.initDigitalInputs()
        self.initAnalogInputs()
        self.initDigitalOutputs()

    def initDigitalInputs(self):
        self.btn1 = DigitalInput(18)
        self.btn2 = DigitalInput(23)
        self.btn3 = DigitalInput(25)
        self.btn4 = DigitalInput(12)
        self.btn5 = DigitalInput(16)
        self.btn6 = DigitalInput(26)
        self.rotBtn = RotaryEncoder(20, 21)

    def initAnalogInputs(self):
        pass

    def initDigitalOutputs(self):
        pass

    def loop(self):
        while True:
            pass
