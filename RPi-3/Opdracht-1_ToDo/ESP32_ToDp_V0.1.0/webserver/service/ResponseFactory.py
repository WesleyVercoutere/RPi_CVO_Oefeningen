from webserver.domain.ResponseObject import ResponseObject
from webserver.domain.RequestObject import RequestObject
from webserver.service.IResponseHandler import IResponseHandler
from webserver.service.handler.ErrorResponseHandler import ErrorResponseHandler
from webserver.service.handler.ResourceResponseHandler import ResourceResponseHandler
from webserver.service.handler.RouteResponseHandler import RouteResponseHandler
from webserver.util.ResponseType import ResponseType


class ResponseFactory:

    def __init__(self,) -> None:
        pass

    def get_response(self, request: RequestObject) -> ResponseObject:
        handler: IResponseHandler = ErrorResponseHandler(request=request)

        if request.response_type == ResponseType.ROUTE:
            handler = RouteResponseHandler(request=request)

        elif request.response_type == ResponseType.RESOURCE:
            handler = ResourceResponseHandler(request=request)

        else:
            handler = ErrorResponseHandler(request=request)
            
        return handler.get_response()
