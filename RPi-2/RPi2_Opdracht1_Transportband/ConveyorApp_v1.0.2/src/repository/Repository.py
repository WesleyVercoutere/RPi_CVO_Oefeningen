import abc


class Repository(metaclass=abc.ABCMeta):

    # Default CRUD methods
    @abc.abstractmethod
    def create(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def readById(self, idOfObj):
        raise NotImplementedError

    @abc.abstractmethod
    def readByIndex(self, indexOfObj):
        raise NotImplementedError

    @abc.abstractmethod
    def readAll(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, obj):
        raise NotImplementedError
