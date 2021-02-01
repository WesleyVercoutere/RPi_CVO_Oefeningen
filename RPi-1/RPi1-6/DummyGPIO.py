BCM = "bcm"
OUT= "out"
IN = "in"
HIGH = "high"
LOW = "low"
PUD_DOWN = "Pull down"

def setwarnings(warning):
    print("warnings off")

def setmode(BCM):
    pass

def setup(pin, typeInOut, pull_up_down=""):
    print(f"setup = {pin} {typeInOut} {pull_up_down}")

def output(pin, output):
    print(f"output pin number {pin} {output}")

def input(pin):
    print(f"input pin number {pin}")