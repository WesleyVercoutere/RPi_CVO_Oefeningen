from webserver.domain.RequestObject import RequestObject
from webserver.service.IResourceState import IResourceState
from webserver.service.ResourceState.APIState import APIState
from webserver.service.ResourceState.HTMLState import HTMLState
from webserver.service.ResourceState.JPGState import JPGState
from webserver.service.ResourceState.JSState import JSState
from webserver.service.ResourceState.CSSState import CSSState
from webserver.service.ResourceState.GZState import GZState
from webserver.service.ResourceState.ICOState import ICOState


class ResourceContext:

    def __init__(self) -> None:
        self._state: IResourceState = None

    def set_state(self, req_obj: RequestObject) -> None:
        if req_obj.response_type.lower() == "html":
            self._state = HTMLState()

        if req_obj.response_type.lower() == "api":
            self._state = APIState()

        if req_obj.response_type.lower() == "resource" and req_obj.file_extension.lower() == "jpg":
            self._state = JPGState()

        if req_obj.response_type.lower() == "resource" and req_obj.file_extension.lower() == "js":
            self._state = JSState()

        if req_obj.response_type.lower() == "resource" and req_obj.file_extension.lower() == "css":
            self._state = CSSState()

        if req_obj.response_type.lower() == "resource" and req_obj.file_extension.lower() == "gz":
            self._state = GZState()

        if req_obj.response_type.lower() == "resource" and req_obj.file_extension.lower() == "ico":
            self._state = ICOState()
        
    def get_state(self) -> IResourceState:
        return self._state
