class AbstractMapper:

    def map_to_object(self, dto):
        raise NotImplementedError()

    def map_to_dto(self, obj):
        raise NotImplementedError()
