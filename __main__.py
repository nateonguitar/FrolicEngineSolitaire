from frolic import Game
from pynput import keyboard

from levels.level import Level

class Solitaire(Game):
    def __init__(self):
        from levels.launch import LaunchLevel
        super().__init__()
        self.set_on_keydown(self.keydown)
        self.show_debug_info = True
        self.level: Level = None
        self.set_level(LaunchLevel)
        self.debug_info['Space Pressed'] = False

    def update(self, deltatime: float):
        self.level.update(deltatime)

    def draw(self):
        self.level.draw(self.screen)
        super().draw()

    def set_level(self, LevelClass: type):
        self.level: Level = LevelClass()

    def keydown(self, key: keyboard.Key):
        if key == keyboard.Key.esc:
            self.end_game()
            return
        self.level.keydown(key)


game = Solitaire()
game.run()
