from service.IResourceState import IResourceState
from service.ResourceState.HTMLState import HTMLState
from service.ResourceState.JPGState import JPGState


class ResourceContext:

    def __init__(self) -> None:
        self._state: IResourceState = None

    def set_state(self, type: str) -> None:
        print(type)

        if type.lower() == "html":
            self._state = HTMLState()

        if type.lower() == "jpg":
            self._state = JPGState()
        
    def get_state(self) -> IResourceState:
        return self._state
