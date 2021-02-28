from service.observer.Observable import Observable


class ConveyorManager(Observable):

    def __init__(self, conveyor,
                 inputManager,
                 ledManager,
                 motorManager,
                 displayManager,
                 positionManager,
                 settingsManager):
        super(ConveyorManager, self).__init__()

        self.conveyor = conveyor
        self.inputMgr = inputManager
        self.ledMgr = ledManager
        self.motorMgr = motorManager
        self.displayMgr = displayManager
        self.positionMgr = positionManager
        self.settingsMgr = settingsManager

    def loop(self):
        while True:
            self.inputMgr.loop()
            self.ledMgr.loop()
            self.motorMgr.loop()
            self.displayMgr.loop()
