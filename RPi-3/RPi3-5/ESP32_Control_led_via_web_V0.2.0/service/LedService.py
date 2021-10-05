from machine import Pin

class LedService:

    def __init__(self) -> None:
        self.ledOnBoard = Pin(2, Pin.OUT)
        self.ledOnBoard.off()

    def led_on(self):
        self.ledOnBoard.on()

    def led_off(self):
        self.ledOnBoard.off()
