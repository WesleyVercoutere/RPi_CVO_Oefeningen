import RPi.GPIO as GPIO

def processInputs():
    print("do stuff")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, edge=GPIO.FALLING, callback=lambda x: processInputs())

while True:
    pass