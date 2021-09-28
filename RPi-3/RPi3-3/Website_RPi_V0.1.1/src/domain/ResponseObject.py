class ResponseObject:

    def __init__(self):
        self.__header_1 = b""
        self.__header_2 = b""
        self.__content_length = b""
        self.__content = b""

    @property
    def header_1(self):
        return self.__header_1

    @header_1.setter
    def header_1(self, value):
        self.__header_1 = value

    @property
    def header_2(self):
        return self.__header_2

    @header_2.setter
    def header_2(self, value):
        self.__header_2 = value

    @property
    def content_length(self):
        return self.__content_length

    @content_length.setter
    def content_length(self, value):
        self.__content_length = value

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value
