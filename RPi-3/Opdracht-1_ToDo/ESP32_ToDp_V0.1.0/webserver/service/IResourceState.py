from webserver.domain.RequestObject import RequestObject
from webserver.domain.StateObject import StateObject


class IResourceState:

    def __init__(self) -> None:
        self._state = None

    def set_state(self, state: StateObject = None, req = None):
        self._state = state
        self._req = req
    
    def get_content(self):
        raise NotImplementedError

    def get_header(self):
        raise NotImplementedError

    def get_cache(self):
        raise NotImplementedError