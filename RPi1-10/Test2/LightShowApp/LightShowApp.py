import RPi.GPIO as GPIO

class LightShowApp:

    def __init__(self):
        self.initIO()
        self.initCallbacks()

    def initIO(self):
        # GPIO general
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        # Inputs
        self.pinBtn1 = 20
        self.pinBtn2 = 21
        
        inputs = (self.pinBtn1, self.pinBtn2)
        GPIO.setup(inputs, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def initCallbacks(self):
        GPIO.add_event_detect(self.pinBtn1, GPIO.RISING, callback=self.toggleShow1, bouncetime=50)
        GPIO.add_event_detect(self.pinBtn2, GPIO.RISING, callback=self.toggleShow2, bouncetime=50)

    def toggleShow1(self, channel):
        print('Show 1')

    def toggleShow1(self, channel):
        print('Show 2')

    def run(self):
        pass



if __name__ == '__main__':
    lsa = LightShowApp()
    lsa.run()
    