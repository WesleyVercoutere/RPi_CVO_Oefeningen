from service.IResourceState import IResourceState


class ResourceContext:

    def __init__(self) -> None:
        self._state: IResourceState = None

    def set_state(self, state: IResourceState) -> None:
        self._state = state
        
    def get_state(self) -> IResourceState:
        return self._state
