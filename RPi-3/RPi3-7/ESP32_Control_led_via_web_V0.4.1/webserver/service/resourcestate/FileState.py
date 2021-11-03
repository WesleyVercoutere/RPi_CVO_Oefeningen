from webserver.service.IResourceState import IResourceState


class FileState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self):
        file = f"resources{self._state.file_name}"
        file = open(file, "r")
        content = file.read()

        return content.encode("UTF-8")

    def get_header(self):
        return b"Content-Type: text/text\r\n"

    def get_cache(self):
        return b"Cache-Control: no-cache, no-store\r\n"
