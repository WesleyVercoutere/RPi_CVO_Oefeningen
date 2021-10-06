class RequestHandler:

    def __init__(self) -> None:
        self._routes = dict()

    def register_route(self, route, f):
        self._routes[route] = f

    def handle_request(self, request):
        pass
