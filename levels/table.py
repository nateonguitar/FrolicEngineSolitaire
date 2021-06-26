from frolic import Screen, Vector2
from pynput import keyboard

from .level import Level

class TableLevel(Level):
    def __init__(self):
        super().__init__()

    def update(self, deltatime: float):
        pass

    def draw(self, screen: Screen):
        screen.draw_string('Table', Vector2(1, 1))

    def keydown(self, key: keyboard.Key):
        if key == keyboard.Key.space:
            self.game_instance.debug_info['Space Pressed'] = True