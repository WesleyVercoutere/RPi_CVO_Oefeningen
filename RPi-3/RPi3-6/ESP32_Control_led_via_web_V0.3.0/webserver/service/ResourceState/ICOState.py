from webserver.service.IResourceState import IResourceState


class ICOState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self):
        file = f"resources/favicon/favicon.png"
        file = open(file, "rb")

        content = file.read()
        return content

    def get_header(self):
        return b"Content-Type: imgage/png\r\n"

    def get_cache(self):
        return b"Cache-Control: public, max-age=3600\r\n"
