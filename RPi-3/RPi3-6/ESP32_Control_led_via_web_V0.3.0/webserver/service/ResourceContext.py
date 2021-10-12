from webserver.service.IResourceState import IResourceState
from webserver.service.ResourceState.HTMLState import HTMLState
from webserver.service.ResourceState.JPGState import JPGState
from webserver.service.ResourceState.JSState import JSState
from webserver.service.ResourceState.CSSState import CSSState
from webserver.service.ResourceState.GZState import GZState


class ResourceContext:

    def __init__(self) -> None:
        self._state: IResourceState = None

    def set_state(self, type: str) -> None:
        if type.lower() == "html":
            self._state = HTMLState()

        if type.lower() == "jpg":
            self._state = JPGState()

        if type.lower() == "js":
            self._state = JSState()

        if type.lower() == "css":
            self._state = CSSState()

        if type.lower() == "gz":
            self._state = GZState()
        
    def get_state(self) -> IResourceState:
        return self._state
