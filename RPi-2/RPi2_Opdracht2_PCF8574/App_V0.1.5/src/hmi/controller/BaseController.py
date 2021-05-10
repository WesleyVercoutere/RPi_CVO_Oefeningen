import abc


class BaseController(metaclass=abc.ABCMeta):

    def __init__(self, logicManager):
        self.logicMgr = logicManager

    def btnToggleLed_clicked(self, btnId):
        pass