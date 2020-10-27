import RPi.GPIO as GPIO
import time

class DigitalOutput():

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.setOutput(False)

    def setOutput(self, state):
        GPIO.output(self.pin, state)


class Lamp(DigitalOutput):

    def __init__(self, pin, timeOn):
        super().__init__(pin)
        self.timeOn = timeOn


class TimeLights():

    def __init__(self, redExtraOn, orangeOn, greenOn):
        self.redExtraOn = redExtraOn
        self.redTime = (2 * redExtraOn) + orangeOn + greenOn
        self.orangeTime = orangeOn
        self.greenTime = greenOn


class TrafficLight():

    def __init__(self, pinRed, pinOronge, pinGreen, startState, timeLights):
        self.timeLights = timeLights
        self.red = Lamp(pinRed, timeLights.redTime)
        self.orange = Lamp(pinOronge, timeLights.orangeTime)
        self.green = Lamp(pinGreen, timeLights.greenTime)
        self.state = startState
        self.lights = (self.red, self.orange, self.green)
        self.currentLightTimeOn = 0
        self.startTimeLightOn = 0


class TrafficLightManager():

    def __init__(self, trafficLights):
        self.trafficLights = trafficLights
        self.start()

    def allLightsOut(self, tl):
        for light in tl.lights:
            light.setOutput(False)

    def updateState(self, tl):
        self.allLightsOut(tl)

        if tl.state == "red":
            tl.green.setOutput(True)
            tl.state = "green"
            tl.currentLightTimeOn = tl.green.timeOn
            
        elif tl.state == "orange":
            tl.red.setOutput(True)
            tl.state = "red"
            tl.currentLightTimeOn = tl.red.timeOn
        
        elif tl.state == "green":
            tl.orange.setOutput(True)
            tl.state = "orange"
            tl.currentLightTimeOn = tl.orange.timeOn
        
        tl.startTimeLightOn = self.getCurrentTimeInSeconds()

    def runLights(self):
        currentTime = self.getCurrentTimeInSeconds()

        for tl in self.trafficLights:
            if (currentTime - tl.startTimeLightOn) >= tl.currentLightTimeOn:
                self.updateState(tl)

    def start(self):
        for tl in self.trafficLights:
            self.allLightsOut(tl)
            tl.startTimeLightOn = self.getCurrentTimeInSeconds()

            if tl.state == "red":
                tl.currentLightTimeOn = tl.red.timeOn
                tl.startTimeLightOn += tl.timeLights.redExtraOn
                tl.red.setOutput(True)
            elif tl.state == "orange":
                tl.currentLightTimeOn = tl.orange.timeOn
                tl.orange.setOutput(True)
            elif tl.state == "green":
                tl.currentLightTimeOn = tl.green.timeOn
                tl.green.setOutput(True)
            else:
                raise Exception("Oeps, er ging iets mis!")

    def getCurrentTimeInSeconds(self):
        return time.time_ns() // 1000000000


class Setup():

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)


class TrafficLightsApp():

    def __init__(self):
        Setup()
        timeLights = TimeLights(2, 2, 5)
        tl1 = TrafficLight(16, 20, 21, "green", timeLights)
        tl2 = TrafficLight(13, 19, 26, "red", timeLights)

        trafficLights = [tl1, tl2]
        self.tlManager = TrafficLightManager(trafficLights)

    def run(self):
        while True:
            self.tlManager.runLights()


if __name__ == "__main__":
    tl = TrafficLightsApp()
    tl.run()
