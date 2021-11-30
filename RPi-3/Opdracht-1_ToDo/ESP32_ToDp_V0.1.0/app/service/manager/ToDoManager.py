from app.repository.ToDoRepository import ToDoRepository
from app.service.dto.ToDoDto import ToDoDto
from app.service.mapper.ToDoMapper import ToDoMapper


class ToDoManager:

    def __init__(self, todo_repo: ToDoRepository, todo_mapper: ToDoMapper) -> None:
        self._repo = todo_repo
        self._mapper = todo_mapper
        
    def add(self, dto: ToDoDto) -> None:
        todo = self._mapper.map_to_object(dto)
        self._repo.create(todo)
