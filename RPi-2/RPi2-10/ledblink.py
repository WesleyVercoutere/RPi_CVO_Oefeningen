import machine
import time

led = machine.Pin(13, machine.Pin.OUT)

while True:
    print("led on")
    led.on()
    time.sleep(1)
    
    print("led off")
    led.off()
    time.sleep(1)
    
    print("led value(1)")
    led.value(1)
    time.sleep(1)
    
    print("led value(0)")
    led.value(0)
    time.sleep(1)