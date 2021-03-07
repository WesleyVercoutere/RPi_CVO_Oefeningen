from hmi.controller.BaseController import BaseController


class DesktopController(BaseController):

    def __init__(self, conveyorManager):
        super(DesktopController, self).__init__(conveyorManager)
