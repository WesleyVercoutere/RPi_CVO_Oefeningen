from domain.RequestObject import RequestObject


class RequestHandler:

    def __init__(self) -> None:
        pass

    def get_request(self, request) -> RequestObject:
        req = self._filter_request(request)

        obj = RequestObject()

        if req == "/":
            obj.filename = "html/led_off.html"
            obj.filetype = "html"
        else:
            obj.filename = req[1:]
            obj.filetype = req.split(".")[1]

        return obj

    def _filter_request(self, request) -> str:
        req = request.decode("utf-8")
        req = req.split('\r\n')[0]
        req = req.split(' ')[1]

        return req
  