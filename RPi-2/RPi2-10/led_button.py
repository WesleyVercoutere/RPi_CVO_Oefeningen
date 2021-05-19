import machine
import time

led = machine.Pin(13, machine.Pin.OUT)
btn = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    button_value = not btn.value()
    print("button_value = ", button_value)
    led.value(button_value)
    time.sleep(0.1)
    