from webserver.service.IResourceState import IResourceState
from webserver.domain.RequestObject import RequestObject


class CSSState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self, request_obj: RequestObject):
        file = f"/resources/{request_obj.file}"
        file = open(request_obj.file, "r")
        content = file.read()

        return content.encode("UTF-8")

    def get_header(self):
        return b"Content-Type: text/css\r\n"

