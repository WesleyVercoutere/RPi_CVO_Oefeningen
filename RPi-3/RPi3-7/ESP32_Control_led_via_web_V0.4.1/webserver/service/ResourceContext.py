from webserver.domain.StateObject import StateObject
from webserver.service.IResourceState import IResourceState
from webserver.service.ResourceState.JPGState import JPGState
from webserver.service.ResourceState.JSState import JSState
from webserver.service.ResourceState.CSSState import CSSState
from webserver.service.ResourceState.GZState import GZState
from webserver.service.ResourceState.ICOState import ICOState


class ResourceContext:

    def __init__(self) -> None:
        self._state: IResourceState = None

    def set_state(self, state_obj: StateObject) -> None:

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
