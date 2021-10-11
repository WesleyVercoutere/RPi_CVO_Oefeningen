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

    def __eq__(self, o: object) -> bool:
        if o == None:
            return False

        if not isinstance(o, Route):
            return False

        return o.route == self.route

    def __hash__(self) -> int:
        return hash(self.__route)