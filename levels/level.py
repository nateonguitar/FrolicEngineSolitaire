from frolic import GameObject, Screen
from pynput import keyboard

class Level(GameObject):
    def __init__(self):
        super().__init__()
    
    def update(self, deltatime: float):
        pass

    def draw(self, screen: Screen):
        pass

    def keydown(self, key: keyboard.Key):
        pass