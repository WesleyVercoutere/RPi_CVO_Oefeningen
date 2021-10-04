from service.IResourceState import IResourceState
from service.LedService import LedService
from service.ResourceState.HTMLState import HTMLState
from service.ResourceState.JPGState import JPGState


class ResourceContext:

    def __init__(self, led_service: LedService) -> None:
        self._state: IResourceState = None
        self._led_service = led_service

    def set_state(self, type: str) -> None:
        if type.lower() == "html":
            self._state = HTMLState(self._led_service)

        if type.lower() == "jpg":
            self._state = JPGState(self._led_service)
        
    def get_state(self) -> IResourceState:
        return self._state
