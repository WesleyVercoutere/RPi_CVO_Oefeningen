from app.domain.Led import Led
from app.service.dto.LedDto import LedDto
from app.service.mapper.AbstractMapper import AbstractMapper


class LedMapper(AbstractMapper):

    def map_to_object(self, dto) -> Led:
        
        if dto is None:
            return None
        
        if not isinstance(dto, LedDto):
            return None

        led = Led()
        led.id = dto.id
        led.pin_nr = dto.pin_nr
        led.color = dto.color
        led.state = dto.state

        return led

    def map_to_dto(self, obj) -> LedDto:
        
        if obj is None:
            return None

        if not isinstance(obj, Led):
            return None

        dto = LedDto(obj.id, obj.pin_nr, obj.color, obj.state)
        return dto
