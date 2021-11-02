from Route import Route


class RouteTest:

    def __init__(self) -> None:
        route1 = Route("/Test", self.dummy)
        route2 = Route("/Test", self.dummy)
        route3 = Route("/Test", self.dummy, ["id"])
        route4 = Route("/Test", self.dummy, ["id"])
        route5 = Route("/Test", self.dummy, ["name"])
        route6 = Route("/Test", self.dummy, ("id", "name"))
        route7 = Route("/Test", self.dummy, ("id", "name"))
        route8 = Route("/Test", self.dummy, ("1", "2"))

        self.test_route_equals(route1, route2, True)
        self.test_route_equals(route3, route4, True)
        self.test_route_equals(route1, route4, False)
        self.test_route_equals(route1, route5, False)
        self.test_route_equals(route3, route5, True)
        self.test_route_equals(route6, route7, True)
        self.test_route_equals(route6, route8, True)

    def dummy(self):
        pass

    def test_route_equals(self, r1, r2, equals):
        result = r1.__eq__(r2)

        print(result == equals)


if __name__ == "__main__":
    RouteTest()