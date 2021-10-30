import re

from webserver.domain.Route import Route


class RouteManager:

    def __init__(self) -> None:
        self._routes = set()

    def register_route(self, route, f) -> None:
        param = re.search("{.*}", route)

        if param:
            param = param.group(0)

        route_obj = Route(route=route, handler=f, parameter=param)
        self._routes.add(route_obj)

    def get_all_routes(self) -> set:
        return self._routes

    def get_route(self, route) -> Route:
        found = None

        for r in self._routes:

            if route == r.route:
                found = r

        return found
