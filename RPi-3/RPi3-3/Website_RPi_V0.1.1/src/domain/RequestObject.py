class RequestObject:

    def __init__(self):
        self.__filename = ""
        self.__filetype = ""

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        self.__filename = value

    @property
    def filetype(self):
        return self.__filetype

    @filetype.setter
    def filetype(self, value):
        self.__filetype = value
