import abc


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError
