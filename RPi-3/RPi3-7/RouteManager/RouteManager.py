import re

from Route import Route
from RouteException import RouteException


class RouteManager:

    def __init__(self) -> None:
        self._routes = list()

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

        route_obj = Route(route=route, base_route=base_route, handler=f, parameters=parameters)
        self._add_route(route_obj)

    def get_all_routes(self) -> set:
        return self._routes

    def find_route(self, url) -> Route:
        # "/test"
        # "/test/nogtest"
        # "/test/{id}"
        # "/test/{id}/{name}"
        # "/test/{name}"

        found = None
        url_split = url.split("/")

        for r in self._routes:
            route_split = r.route.split("/")

            if len(url_split) != len(route_split):
                continue
            
            # if len(url_split) == 2:
            #     print("index page")
            #     found = r
            #     break

            if url_split[1] != route_split[1]:
                continue
            
            if url == r.route:
                found = r
                break
            
            parameters = []

            for i in range(2, len(url_split)):
                
                if url_split[i] != route_split[i]:
                    parameters.append(url_split[i])

            found = Route(route=url, base_route=r.base_route, handler=r.handler, parameters=parameters)

        return found

    def _add_route(self, route):
        exists = False

        for r in self._routes:
            if route.__eq__(r):
                exists = True
                raise RouteException(f"Route {route.route} already assigned with other parameters!")

        if not exists:
            self._routes.append(route)
