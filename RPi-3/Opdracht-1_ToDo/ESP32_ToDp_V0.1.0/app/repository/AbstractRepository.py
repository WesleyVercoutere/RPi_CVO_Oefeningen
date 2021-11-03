class AbstractRepository:

    def __init__(self) -> None:
        pass

    def create(self, obj):
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
