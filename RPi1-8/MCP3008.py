import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

mcp3008_channel_0 = MCP3008(channel=0, device=0)

while True:
    print(mcp3008_channel_0.value)
    