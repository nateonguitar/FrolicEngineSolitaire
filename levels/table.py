from frolic import Screen, Vector2
from pynput import keyboard

from .level import Level

class TableLevel(Level):
    def __init__(self):
        super().__init__()

    def update(self, deltatime: float):
        pass

    def draw(self, screen: Screen):
        pass

    def keydown(self, key: keyboard.Key):
        pass