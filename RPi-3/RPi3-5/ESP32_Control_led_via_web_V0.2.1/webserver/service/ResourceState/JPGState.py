from webserver.service.IResourceState import IResourceState
from webserver.domain.RequestObject import RequestObject


class JPGState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self, request_obj: RequestObject):
        file = f"resources{request_obj.file}"
        file = open(file, "rb")

        content = file.read()
        return content

    def get_header(self):
        return b"Content-Type: imgage/jpg\r\n"
