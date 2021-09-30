import os

from domain.ResponseObject import ResponseObject
from domain.RequestObject import RequestObject
from service.ResourceHelper import ResourceHelper


class ResponseHandler:

    def __init__(self) -> None:
        self._resource_helper = ResourceHelper()

    def get_response(self, request_obj: RequestObject) -> ResponseObject:
        response = ResponseObject()

        try:
            file = self._resource_helper.get_resource(request_obj)
            content = file.read()
            content_length = len(content)

            response.header_1 = b"HTTP/1.1 200 OK\r\n"

            if request_obj.filetype == "html":
                response.header_2 = b"Content-Type: text/html\r\n"
            
            elif request_obj.filetype == "jpg":
                response.header_2 = b"Content-Type: imgage/jpg\r\n"
            
            elif request_obj.filetype == "png":
                response.header_2 = b"Content-Type: image/png\r\n"
            
            elif request_obj.filetype == "favicon":
                response.header_2 = b"Content-Type: image/ico\r\n"
            
            else:
                raise Exception("No filetype in ResponseHandler.get_response()")

            response.content_length = (f"Content-Length:{str(content_length)}\r\n\r\n").encode("UTF-8")

            if request_obj.filetype == "html":
                response.content = content.encode("UTF-8")
            else:
                response.content = content

        except:
            print("file not found")
            response.header_1 = b"HTTP/1.1 404 Not Found\r\n"

        finally:
            return response
         