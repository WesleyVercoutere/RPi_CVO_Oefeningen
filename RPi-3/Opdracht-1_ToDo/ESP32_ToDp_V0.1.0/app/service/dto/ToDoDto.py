class ToDoDto:

    def __init__(self, id=0, title="", carried_out_by="", start="", end="") -> None:
        self.id = id
        self.title = title
        self.carried_out_by = carried_out_by
        self.start = start
        self.end = end
