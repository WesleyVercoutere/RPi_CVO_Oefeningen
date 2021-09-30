from enum import Enum

from service.IResourceState import IResourceState
from service.ResourceState.HTMLState import HTMLState
from service.ResourceState.JPGState import JPGState


class Resource(Enum):

    HTML = ("html", HTMLState())
    JPG = ("jpg", JPGState())

    def __init__(self, type: str, state: IResourceState) -> None:
        self._type = type
        self._state = state

    def get_type(self) -> str:
        return self._type

    def get_state(self) -> IResourceState:
        return self._state
