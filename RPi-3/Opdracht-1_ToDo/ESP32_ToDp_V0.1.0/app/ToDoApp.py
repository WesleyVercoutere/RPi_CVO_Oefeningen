from app.controller.Controller import Controller
from app.domain.ToDo import ToDo
from app.repository.ToDoRepository import ToDoRepository
from app.service.dto.ToDoDto import ToDoDto
from app.service.manager.ToDoManager import ToDoManager
from app.service.mapper.ToDoMapper import ToDoMapper
from webserver.WebServer import WebServer


class ToDoApp:

    def __init__(self) -> None:
        self._web_server = WebServer()

        self._todo_repo = ToDoRepository()
        self._todo_mapper = ToDoMapper()
        self._todo_mgr = ToDoManager(todo_repo=self._todo_repo, todo_mapper=self._todo_mapper)
        
        self._controller = Controller(web_server=self._web_server, todo_mgr=self._todo_mgr)

    def run(self) -> None:
        self._controller.register_routes()
        self._web_server.run()

        self._load_dummy_data()

    def _load_dummy_data(self) -> None:
        todo1 = ToDoDto(id=1, title="Grondwerken", carried_out_by="De Ridder", start="04/11/2021", end="05/11/2021")
        todo2 = ToDoDto(id=2, title="Betonplaat", carried_out_by="Van Damme", start="05/11/2021", end="05/11/2021")
        todo3 = ToDoDto(id=3, title="Metselwerken", carried_out_by="Van Damme", start="06/11/2021", end="10/11/2021")

        self._todo_mgr.add(todo1)
        self._todo_mgr.add(todo2)
        self._todo_mgr.add(todo3)
