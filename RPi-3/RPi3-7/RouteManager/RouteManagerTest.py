from RouteManager import RouteManager

class RouteManagerTest:

    def __init__(self) -> None:
        self.mgr = None
        self.setup()

        print("**************************")
        print("** Test first character **")
        print("**************************")
        self.test_first_character_is_slash(self.url1, True)
        self.test_first_character_is_slash(self.url2, True)
        self.test_first_character_is_slash(self.url3, True) # Test nog niet afgehandeld in manager
        self.test_first_character_is_slash(self.url4, False)
        self.test_first_character_is_slash(self.url5, False)
        self.test_first_character_is_slash(self.url6, False)
        self.test_first_character_is_slash(self.url7, False)

        print()
        print("*********************")
        print("** Test base route **")
        print("*********************")
        self.test_base_route(self.url4, "/test")
        self.test_base_route(self.url5, "/test/nogtest")
        self.test_base_route(self.url6, "/test")
        self.test_base_route(self.url7, "/test")

        print()
        print("*********************")
        print("** Test find route **")
        print("*********************")
        self.test_find_route("/test", True)
        self.test_find_route("/test/nogtest", True)
        self.test_find_route("/test/1", True, ["id"])
        self.test_find_route("/test/1/weve", True, ["id", "name"])
        self.test_find_route("/test/weve", True, ["name"])
        self.test_find_route("/mispoes", False)
        self.test_find_route("/", True)

    def setup(self) -> None:
        self.url1 = "test"
        self.url2 = "{test}"
        self.url3 = "/{test}"

        self.url4 = "/test"
        self.url5 = "/test/nogtest"
        self.url6 = "/test/{id}"
        self.url7 = "/test/{id}/{name}"
        self.url8 = "/test/{name}"
        
        self.url9 = "/"
        self.url10 = "/home"

    def dummy(self) -> None:
        pass

    def test_first_character_is_slash(self, route, exception=False):
        self.mgr = RouteManager()

        CRED = '\033[91m'
        CEND = '\033[0m'
        CERR = '\033[0m'

        output = "success"

        try:
            self.mgr.register_route(route, self.dummy)
            
            if exception:
                output = "fail"
                CERR = CRED
        
        except:
            if not exception:
                output = "fail"
                CERR = CRED

        finally:
            print(CERR + f"test first character {route}: {output}" + CEND)

    def test_base_route(self, route, base_route):
        self.mgr = RouteManager()
        self.mgr.register_route(route, self.dummy)

        r = None

        for rl in self.mgr.get_all_routes():
            r = rl
            break

        CRED = '\033[91m'
        CEND = '\033[0m'
        CERR = '\033[0m'

        output = "success"

        if r.base_route != base_route:
            CERR = CRED
            output = "fail"

        print(CERR + f"test base route {route}: {output}" + CEND)

    def test_find_route(self, url, found, parameters=None):
        self.mgr = RouteManager()
        self.setup_routes()

        r = self.mgr.find_route(url)

        CRED = '\033[91m'
        CEND = '\033[0m'
        CERR = '\033[0m'

        output = "success"

        if (not found and r is not None) or (found and r is None):
            CERR = CRED
            output = "fail"
            print(CERR + f"test find route {url}: {output}" + CEND)
            return

        if r is not None and r.route != url:
            CERR = CRED
            output = "fail"

        rroute = ""

        if r is not None:
            rroute = r.route

        print(CERR + f"test find route {url} - {rroute}: {output}" + CEND)

    def setup_routes(self):
        self.mgr.register_route(self.url4, self.dummy)
        self.mgr.register_route(self.url5, self.dummy)
        self.mgr.register_route(self.url6, self.dummy)
        self.mgr.register_route(self.url7, self.dummy)
        self.mgr.register_route(self.url9, self.dummy)
        self.mgr.register_route(self.url10, self.dummy)


if __name__ == "__main__":
    RouteManagerTest()
