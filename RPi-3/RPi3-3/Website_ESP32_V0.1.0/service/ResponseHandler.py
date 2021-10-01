import os

from domain.ResponseObject import ResponseObject
from domain.RequestObject import RequestObject
from service.ResourceContext import ResourceContext
from service.IResourceState import IResourceState
from util.Resource import Resource


class ResponseHandler:

    def __init__(self, resource_context: ResourceContext) -> None:
        self._context = resource_context

    def get_response(self, request_obj: RequestObject) -> ResponseObject:
        file = f"resources/{request_obj.filename}"

        response = ResponseObject()

        if request_obj.filetype == "html":
            file = open(file, "r")

        elif request_obj.filetype == "jpg" or request_obj.filetype == "favicon" or request_obj.filetype == "png" :
            file = open(file, "rb")
        
        else:
            raise Exception("Couldn't open file in ResponseHandler.get_response()")

        content = file.read()
        content_length = len(content)

        response.header_1 = b"HTTP/1.1 200 OK\r\n"

        if request_obj.filetype=="html":
            response.header_2 = b"Content-Type: text/html\r\n"
        elif request_obj.filetype=="jpg":
            response.header_2 = b"Content-Type: imgage/jpg\r\n"
        elif request_obj.filetype=="png":
            response.header_2 = b"Content-Type: image/png\r\n"
        elif request_obj.filetype=="favicon":
            response.header_2 = b"Content-Type: image/ico\r\n"
        else:
            raise Exception("No filetype in ResponseHandler.get_response()")


        response.content_length = (f"Content-Length:{str(content_length)}\r\n\r\n").encode("UTF-8")

        if request_obj.filetype == "html":
            response.content = content.encode("UTF-8")
        else:
            response.content = content

        return response
