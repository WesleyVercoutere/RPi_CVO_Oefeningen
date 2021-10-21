from abc import ABC, abstractmethod

class AbstractMapper(ABC):

    @abstractmethod
    def map_to_object(self, dto):
        raise NotImplementedError()

    @abstractmethod
    def map_to_dto(self, obj):
        raise NotImplementedError()
