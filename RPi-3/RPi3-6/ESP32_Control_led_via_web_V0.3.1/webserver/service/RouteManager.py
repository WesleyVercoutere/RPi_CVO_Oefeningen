from webserver.domain.Route import Route


class RouteManager:

    def __init__(self) -> None:
        self._routes = set()

    def register_route(self, route, f) -> None:
        route = Route(route=route, handler=f)
        self._routes.add(route)

    def get_all_routes(self) -> set:
        return self._routes

    def get_route(self, route) -> Route:
        found = None

        for r in self._routes:

            if route == r.route:
                found = r

        return found
