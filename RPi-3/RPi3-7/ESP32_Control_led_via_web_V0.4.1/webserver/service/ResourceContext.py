from webserver.domain.StateObject import StateObject
from webserver.service.IResourceState import IResourceState
from webserver.service.resourcestate.APIState import APIState
from webserver.service.resourcestate.HTMLState import HTMLState
from webserver.service.resourcestate.JPGState import JPGState
from webserver.service.resourcestate.JSState import JSState
from webserver.service.resourcestate.CSSState import CSSState
from webserver.service.resourcestate.GZState import GZState
from webserver.service.resourcestate.ICOState import ICOState
from webserver.util.RequestType import RequestType


class ResourceContext:

    def __init__(self) -> None:
        self._state: IResourceState = None

    def set_state(self, state_obj: StateObject = None, type = None) -> None:

        if type is not None:
            self._set_route_state(type=type)

        if state_obj is not None:
            self._set_resource_state(state_obj=state_obj)

    def _set_route_state(self, type: RequestType) -> None:

        if type == RequestType.NORMAL:
            self._state = HTMLState()

        elif type == RequestType.REST:
            self._state = APIState()

        else:
            self._state = None
    
    def _set_resource_state(self, state_obj: StateObject) -> None:

        if state_obj.file_extension.lower() == "jpg":
            self._state = JPGState()

        elif state_obj.file_extension.lower() == "js":
            self._state = JSState()

        elif state_obj.file_extension.lower() == "css":
            self._state = CSSState()

        elif state_obj.file_extension.lower() == "gz":
            self._state = GZState()

        elif state_obj.file_extension.lower() == "ico":
            self._state = ICOState()

        else:
            self._state = None
        
    def get_state(self) -> IResourceState:
        return self._state
