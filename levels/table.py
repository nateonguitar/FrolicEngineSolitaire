from frolic import GameObject, Screen, Vector2
from pynput import keyboard


from .level import Level
from game_objects.card import Card

class TableLevel(Level):
    def __init__(self):
        super().__init__()
        self.deck = GameObject()
        self.deck.position = Vector2(1, 1)
        self.deck.cards = []
        self.deck.cards.append(Card(value='2', suit='X'))
        self.deck.cards.append(Card(value='3', suit='♤'))
        self.deck.cards.append(Card(value='4', suit='O'))
        self.deck.cards.append(Card(value='5', suit='♤'))

    def update(self, deltatime: float):
        self.deck.position.x += 1

    def draw(self, screen: Screen):
        for i in range(len(self.deck.cards)):
            card: Card = self.deck.cards[i]
            position = Vector2(self.deck.position.x, self.deck.position.y + (i*2))
            screen.draw_matrix(card.matrix, position)

    def keydown(self, key: keyboard.Key):
        pass