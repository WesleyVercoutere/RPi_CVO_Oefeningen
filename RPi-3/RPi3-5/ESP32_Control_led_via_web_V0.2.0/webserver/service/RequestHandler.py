from webserver.service.RouteManager import RouteManager


class RequestHandler:

    def __init__(self, routeManager: RouteManager) -> None:
        self._routeMgr = routeManager

    def handle_request(self, request):
        
        print(request.decode("utf-8"))
        print()

        route = self._filter_request(request)
        route = self._routeMgr.get_route(route)
        
        if route is not None:
            html = route.handler()

            print(html)

        # try load resource

        # return 404


    def _filter_request(self, request) -> str:
        req = request.decode("utf-8")
        req = req.split('\r\n')[0]
        req = req.split(' ')[1]

        return req
  