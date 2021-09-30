import abc

from domain.RequestObject import RequestObject

class IResourceState(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_content(self, request_obj: RequestObject):
        raise NotImplementedError

    @abc.abstractmethod
    def get_header(self):
        raise NotImplementedError
