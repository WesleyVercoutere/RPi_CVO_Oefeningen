from machine import Pin


class ButtonManager:

    def __init__(self, btn_mapper, btn_repository) -> None:
        self._mapper = btn_mapper
        self._repo = btn_repository

    def add_buttons(self, *btns):
        [self._repo.create(btn) for btn in btns]

    def get_all_buttons(self):
        return self._repo.read_all()

    