from webserver.service.IResourceState import IResourceState


class CSSState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self):
        file = f"resources{self.request_obj.filename}"
        file = open(file, "r")
        content = file.read()

        return content.encode("UTF-8")

    def get_header(self):
        return b"Content-Type: text/css\r\n"

    def get_cache(self):
        return b"Cache-Control: max-age=3600\r\n"

