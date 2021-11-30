from app.domain.ToDo import ToDo
from app.repository.AbstractRepository import AbstractRepository


class ToDoRepository(AbstractRepository):

    def __init__(self) -> None:
        file = r"resources\data\data.txt"
        file = open(file, "a")
        file.close()

    def create(self, obj: ToDo):
        raise NotImplementedError()

    def read_by_id(self, id):
        raise NotImplementedError()

    def read_all(self):
        raise NotImplementedError()

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
