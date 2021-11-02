from webserver.service.IResourceState import IResourceState


class APIState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self):
        
        if self._req is not None:
            return self._req.encode("utf-8")

        return None

    def get_header(self):
        return b"Content-Type: application/json\r\n"

    def get_cache(self):
        return b"Cache-Control: no-cache, no-store\r\n"
