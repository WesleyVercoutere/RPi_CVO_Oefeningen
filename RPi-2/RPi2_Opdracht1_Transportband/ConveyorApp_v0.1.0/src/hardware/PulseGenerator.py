import time


class PulseGenerator:

    def __init__(self, pulseTime):
        self.pulseTime = pulseTime
        self.startTime = time.time()
        self.Q = False

    def generate(self):
        self.Q = False

        if time.time() >= (self.startTime + self.pulseTime):
            self.startTime = time.time()
            self.Q = True
