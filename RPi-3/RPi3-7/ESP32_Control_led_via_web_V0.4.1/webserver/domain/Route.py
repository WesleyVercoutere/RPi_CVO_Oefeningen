class Route:

    def __init__(self, route, handler, parameter=None) -> None:
        self.__route = route
        self.__handler = handler
        self.__parameter = parameter

    @property
    def route(self):
        return self.__route

    @property
    def handler(self):
        return self.__handler

    @property
    def parameter(self):
        return self.__parameter

    def __eq__(self, o: object) -> bool:
        if o == None:
            return False

        if not isinstance(o, Route):
            return False

        return o.route == self.route and o.parameter == self.parameter

    def __hash__(self) -> int:
        to_hash = self.route

        if self.parameter is not None:
            to_hash += str(self.parameter)

        return hash(to_hash)
        