from business.Settings import Settings

class Thermostat:

    def __init__(self):
        self.status = False
        self.currentTemp = 0
        self.settings = Settings()
        self.setRoomTemp = False
