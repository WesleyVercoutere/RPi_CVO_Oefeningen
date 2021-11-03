from webserver.domain.RequestObject import RequestObject
from webserver.domain.ResponseObject import ResponseObject
from webserver.domain.StateObject import StateObject
from webserver.service.IResponseHandler import IResponseHandler
from webserver.service.ResourceContext import ResourceContext


class ResourceResponseHandler(IResponseHandler):

    def __init__(self, request: RequestObject) -> None:
        super().__init__(request)

    def get_response(self) -> ResponseObject:        
        file_name = self._get_file_name()
        file_extension = self._get_file_extension()
        state = StateObject(file_name=file_name, file_extension=file_extension)

        self._context.set_state(state_obj=state)
        self._state = self._context.get_state()

        if self._state is not None:
            self._state.set_state(state=state)

        return self._create_response()

    def _get_file_name(self):
        return self._request.request_url

    def _get_file_extension(self):
        return self._request.request_url.split(".")[-1]
