from machine import Pin, PWM
import time

pwm0 = PWM(Pin(13))
pwm0.freq(1000)
pwm0.duty(200)

while True:
    for x in range(0,1024):
        pwm0.duty(x)
        time.sleep(0.01)
        