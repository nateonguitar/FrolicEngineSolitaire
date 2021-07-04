import random

from frolic import Screen, Vector2
from pynput import keyboard


from .level import Level
from game_objects.card import Card
from game_objects.stack import TableStack

class TableLevel(Level):
    def __init__(self):
        super().__init__()
        deck: list[Card] = []
        for suit in ['♥', '♦', '♠', '♣']:
            for i in range(1, 14):
                deck.append(Card(suit=suit, value=i))
        random.shuffle(deck)

        self.table_stacks: list[TableStack] = []
        for i in range(7):
            stack = TableStack()
            stack.position = Vector2(i*6, 1)
            for j in range(i+1):
                card = deck.pop()
                stack.append(card)
                if j == i:
                    card.flip()
            self.table_stacks.append(stack)

    def update(self, deltatime: float):
        pass

    def draw(self, screen: Screen):
        for table_stack in self.table_stacks:
            table_stack.draw(screen)

    def keydown(self, key: keyboard.Key):
        pass
