class Route:

    def __init__(self, route, handler) -> None:
        self.__route = route
        self.__handler = handler

    @property
    def route(self):
        return self.__route

    @property
    def handler(self):
        return self.__handler
