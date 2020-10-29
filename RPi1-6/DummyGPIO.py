BCM = "bcm"
OUT= "out"
HIGH = "high"
LOW = "low"

def setwarnings(warning):
    print("warnings off")

def setmode(BCM):
    pass

def setup(pin, typeInOut):
    print(f"setup = {pin} {typeInOut}")

def output(pin, output):
    print(f"output pin number {pin} {output}")