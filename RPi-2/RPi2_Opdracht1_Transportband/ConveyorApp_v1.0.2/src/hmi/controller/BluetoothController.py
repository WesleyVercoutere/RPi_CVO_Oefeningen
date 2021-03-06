from hmi.controller.BaseController import BaseController


class BluetoothController(BaseController):

    def __init__(self, conveyorManager):
        super(BluetoothController, self).__init__(conveyorManager)
