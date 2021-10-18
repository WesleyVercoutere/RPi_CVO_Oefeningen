from webserver.service.IResourceState import IResourceState


class APIState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self):
        json = self.request_obj.handler()
        return json

    def get_header(self):
        return b"Content-Type: application/json\r\n"

    def get_cache(self):
        return b"Cache-Control: no-cache, no-store\r\n"
