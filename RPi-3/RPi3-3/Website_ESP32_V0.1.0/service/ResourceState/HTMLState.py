import os

from service.IResourceState import IResourceState
from domain.RequestObject import RequestObject

class HTMLState(IResourceState):

    def __init__(self) -> None:
        pass

    def get_content(self, request_obj: RequestObject):
        file =  f"/resources/{request_obj.filename}"
        file = open(file, "r")

        content = file.read()
        return content.encode("UTF-8")

    def get_header(self):
        return b"Content-Type: text/html\r\n"

