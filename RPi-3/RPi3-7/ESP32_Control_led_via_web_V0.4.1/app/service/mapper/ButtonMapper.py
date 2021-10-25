from app.domain.Button import Button
from app.service.dto.ButtonDto import ButtonDto
from app.service.mapper.AbstractMapper import AbstractMapper


class ButtonMapper(AbstractMapper):

    def map_to_object(self, dto) -> Button:
        
        if dto is None:
            return None
        
        if not isinstance(dto, ButtonDto):
            return None

        led = Button()
        led.id = dto.id
        led.pin_nr = dto.pin_nr
        led.color = dto.color
        led.state = dto.state

        return led

    def map_to_dto(self, obj) -> ButtonDto:
        
        if obj is None:
            return None

        if not isinstance(obj, Button):
            return None

        dto = ButtonDto(obj.id, obj.pin_nr, obj.state)
        return dto
