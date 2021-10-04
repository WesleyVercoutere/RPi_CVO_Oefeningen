from service.IResourceState import IResourceState
from domain.RequestObject import RequestObject
from service.LedService import LedService

class JPGState(IResourceState):

    def __init__(self, led_service: LedService) -> None:
        super().__init__(led_service)

    def get_content(self, request_obj: RequestObject):
        file = f"/resources/{request_obj.filename}"
        file = open(file, "rb")

        content = file.read()
        return content

    def get_header(self):
        return b"Content-Type: imgage/jpg\r\n"
