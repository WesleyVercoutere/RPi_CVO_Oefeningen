# from machine import Pin


class LedManager:

    def __init__(self) -> None:
        # self.ledOnBoard = Pin(14, Pin.OUT)
        self.led_off()

    def led_on(self):
        print("led on")
        # self.ledOnBoard.on()

    def led_off(self):
        print("led off")
        # self.ledOnBoard.off()

    def led_toggle(self):
        print("led toggle")
        # self.ledOnBoard.value(not self.ledOnBoard.value())
