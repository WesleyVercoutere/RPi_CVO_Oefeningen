from app.domain.Button import Button
from app.repository.AbstractRepository import AbstractRepository
from app.domain.Button import Button


class ButtonRepository(AbstractRepository):

    def __init__(self) -> None:
        self._btns = list()

    def create(self, obj):
        if not isinstance(obj, Button):
            return None

        self._btns.append(obj)

    def read_by_id(self, id):
        return next((btn for btn in self._btns if btn.id == id), None)

    def read_all(self):
        return self._btns

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
