import abc


class Repository(metaclass=abc.ABCMeta):

    # Default CRUD methods
    
    @abc.abstractmethod
    def append(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def getById(self, idOfObj):
        raise NotImplementedError

    @abc.abstractmethod
    def getByIndex(self, indexOfObj):
        raise NotImplementedError

    @abc.abstractmethod
    def getAll(self):
        raise NotImplementedError
