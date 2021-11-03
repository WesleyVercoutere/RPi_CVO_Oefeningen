from app.repository.AbstractRepository import AbstractRepository
from app.domain.Led import Led


class LedRepository(AbstractRepository):

    def __init__(self) -> None:
        self._leds = list()

    def create(self, obj):
        if not isinstance(obj, Led):
            return None

        self._leds.append(obj)

    def read_by_id(self, id):
        
        for led in self._leds:

            if led.id == int(id):
                return led
        
        return None

        # return next((led for led in self._leds if led.id == id), None)

    def read_all(self):
        return self._leds

    def update(self, obj: object):
        raise NotImplementedError()

    def update_all(self, obj: list()):
        raise NotImplementedError()

    def delete(self, obj):
        raise NotImplementedError()

    def delete_by_id(self, id):
        raise NotImplementedError()

    def delete_all(self, obj: list()):
        raise NotImplementedError()
