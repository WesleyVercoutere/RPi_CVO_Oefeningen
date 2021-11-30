from app.service.dto.ToDoDto import ToDoDto
from app.domain.ToDo import ToDo
from app.service.mapper.AbstractMapper import AbstractMapper


class ToDoMapper(AbstractMapper):

    def map_to_object(self, dto: ToDoDto):
        if dto is None or not isinstance(dto, ToDoDto):
            return None

        toDo = ToDo()
        toDo.id = dto.id
        toDo.title = dto.title
        toDo.carried_out_by = dto.carried_out_by
        toDo.start = dto.start
        toDo.end = dto.end

    def map_to_dto(self, obj: ToDo):
        if obj is None or not isinstance(obj, ToDo):
            return None

        dto = ToDoDto()
        dto.id = obj.id
        dto.title = obj.title
        dto.carried_out_by = obj.carried_out_by
        dto.start = obj.start
        dto.end = obj.end
