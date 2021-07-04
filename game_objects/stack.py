from frolic import GameObject, Screen, Vector2

from .card import Card, face_down_matrix

class Stack(GameObject):
    def __init__(self):
        super().__init__()
        self._cards: list[Card] = []

    def __getitem__(self, index):
        self._cards[index]

    def __setitem__(self, index, data):
        self._cards[index] = data

    def __len__(self):
        return len(self._cards)

    def pop(self):
        return self._cards.pop()

    def append(self, card: Card):
        self._cards.append(card)

    def draw(self, screen: Screen):
        pass


class TableStack(Stack):
    def draw(self, screen: Screen):
        for i in range(len(self._cards)):
            card = self._cards[i]
            position = Vector2(self.position.x, self.position.y + (i*2))
            if card.face_down:
                screen.draw_matrix(face_down_matrix, position)
            else:
                screen.draw_matrix(card.matrix, position)
