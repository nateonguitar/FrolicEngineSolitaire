from frolic import Screen, Vector2

from .level import Level

class LaunchLevel(Level):
    def __init__(self):
        super().__init__()
        self.time_to_wait = 0.5
        self.time_waited = 0

    def update(self, deltatime: float):
        self.time_waited += deltatime
        if self.time_waited >= self.time_to_wait:
            from .table import TableLevel
            self.game_instance.set_level(TableLevel)

    def draw(self, screen: Screen):
        screen.draw_string('Solitaire', Vector2(1, 1))
