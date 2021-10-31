import re

from Route import Route
from RouteException import RouteException


class RouteManager:

    def __init__(self) -> None:
        self._routes = set()

    def register_route(self, route, f) -> None:
        if route[0] != "/":
            raise RouteException(f"Route {route} doesn't start with a /")

        subs = route.split("/")[1:]
        base_route = ""
        parameters = []

        for sub in subs:
            param = re.search("{.*}", sub)

            if param:
                param = param.group(0)
                parameters.append(param)
            else:
                base_route += f"/{sub}"

        route_obj = Route(base_route=base_route, handler=f, parameters=parameters)
        self._routes.add(route_obj)

    def get_all_routes(self) -> set:
        return self._routes

    def find_route(self, url) -> Route:
        found = None

        for r in self._routes:

            if r.base_route in url:
                found = r

        return found
