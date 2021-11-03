class StateObject:

    def __init__(self, file_name, file_extension) -> None:
        self.__file_name = file_name
        self.__file_extension = file_extension

    @property
    def file_name(self):
        return self.__file_name

    @property
    def file_extension(self):
        return self.__file_extension
