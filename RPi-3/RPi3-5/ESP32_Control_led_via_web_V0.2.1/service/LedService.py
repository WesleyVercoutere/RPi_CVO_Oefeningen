from machine import Pin


class LedService:

    def __init__(self) -> None:
        self.ledOnBoard = Pin(2, Pin.OUT)
        self.led_off()

    def led_on(self):
        print("led on")
        self.ledOnBoard.on()

    def led_off(self):
        print("led off")
        self.ledOnBoard.off()