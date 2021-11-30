

class ToDo:

    def __init__(self, id=0, title="", carried_out_by="", start="", end="") -> None:
        self._id = id
        self._title = title
        self._carried_out_by = carried_out_by
        self._start = start
        self._end = end

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def carried_out_by(self):
        return self._carried_out_by

    @carried_out_by.setter
    def carried_out_by(self, value):
        self._carried_out_by = value

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end

    @end.setter
    def id(self, value):
        self._end = value
