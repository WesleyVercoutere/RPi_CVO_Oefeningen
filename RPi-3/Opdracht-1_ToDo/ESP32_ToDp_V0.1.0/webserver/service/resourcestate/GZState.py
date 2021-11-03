from webserver.service.IResourceState import IResourceState


class GZState(IResourceState):

    def __init__(self) -> None:
        super().__init__()

    def get_content(self):
        file = f"resources{self._state.file_name}"
        file = open(file, "rb")
        content = file.read()

        return content

    def get_header(self):
        extension = self._state.file_extension
        header = b""

        if extension == "css":
            header = b"Content-Type: text/css\r\n"

        if extension == "js":
            header = b"Content-Type: application/javascript\r\n"

        header += b"Content-Encoding: gzip\r\n"

        return header

    def get_cache(self):
        return b"Cache-Control: max-age=3600\r\n"
