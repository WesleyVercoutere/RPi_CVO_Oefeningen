class RequestHandler:

    def __init__(self) -> None:
        self._routes = dict()

    def route(self, *routes):
        def wrapper(f):
            for route in routes:
                print(f"Register route: {route}")

                self._routes[route] = f
        
        return wrapper

    def handle_request(self, request):
        pass
