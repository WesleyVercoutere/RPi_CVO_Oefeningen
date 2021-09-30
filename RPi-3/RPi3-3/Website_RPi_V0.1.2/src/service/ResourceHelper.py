import os

from domain.RequestObject import RequestObject


class ResourceHelper:

    def __init__(self) -> None:
        pass

    def get_resource(self, request_obj: RequestObject):
        file = self._get_path(request_obj.filename)

        if request_obj.filetype == "html":
            file = open(file, "r")

        elif request_obj.filetype == "jpg" or request_obj.filetype == "favicon" or request_obj.filetype == "png" :
            file = open(file, "rb")
        
        return file

    def _get_path(self, filename):
        return os.path.join(os.getcwd(), "src", "resources", filename)
