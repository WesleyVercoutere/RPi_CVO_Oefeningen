'''
-	Bluetooth module
    o	RX : UARTO TX
    o	TX : UARTO RX
'''


class CommunicationManager:

    def __init__(self, conveyorManager):
        self.conveyorMgr = conveyorManager


    def loop(self):
        while True:
            pass