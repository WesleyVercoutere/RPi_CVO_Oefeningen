BCM = ""
OUT = "output pin"
HIGH = "high"
LOW = "low"

def setwarnings(warning):
    print("Warning set to: {}".format(warning))
    print()

def setmode(mode):
    print("Mode set to: {}".format(str(mode)))
    print()

def setup(pin, mode):
    print("pin {} set to {}".format(pin, (str(mode))))
    print()

def output(pin, mode):
    print("pin {} {}".format(pin, (str(mode))))
    print()
