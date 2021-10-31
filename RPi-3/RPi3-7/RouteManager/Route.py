class Route:

    def __init__(self, base_route, handler, parameters=None) -> None:
        self.__base_route = base_route
        self.__handler = handler
        self.__parameters = None

        self._set_parameters(parameters)

    @property
    def base_route(self):
        return self.__base_route

    @property
    def handler(self):
        return self.__handler

    @property
    def parameters(self):
        return self.__parameters

    def _set_parameters(self, parameters):
        if parameters is None:
            return

        if len(parameters) == 0:
            return

        self.__parameters = list()

        for par in parameters:
            self.__parameters.append(par)

    def __eq__(self, o: object) -> bool:
        if o == None:
            return False

        if not isinstance(o, Route):
            return False

        if o.base_route != self.base_route:
            return False

        if o.parameters is None and self.parameters is None:
            return True

        if (o.parameters is None and self.parameters is not None) or (o.parameters is not None and self.parameters is None):
            return False

        if len(o.parameters) != len(self.parameters):
            return False

        for i in range(len(self.parameters)):
            if self.parameters[i] != o.parameters[i]:
                print(self.parameters[i], o.parameters[i])
                return False
        
        return True

    def __hash__(self) -> int:
        to_hash = self.base_route

        if self.parameters is not None:
            for par in self.parameters:
                to_hash += str(par)

        return hash(to_hash)
        