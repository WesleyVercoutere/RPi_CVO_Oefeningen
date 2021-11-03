from webserver.service.IResourceState import IResourceState


class HTMLState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self):
        file = open(f"{self._req}", "r")
        content = file.read()

        return content.encode("UTF-8")

    def get_header(self):
        return b"Content-Type: text/html\r\n"

    def get_cache(self):
        return b"Cache-Control: no-cache, no-store\r\n"
