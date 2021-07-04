from frolic import GameObject, Matrix, Screen, Vector2

from .card import Card

empty_stack_matrix = Matrix([
    ['┌', ' ', ' ',' ', '┐'],
    [' ', ' ', ' ',' ', ' '],
    [' ', ' ', ' ',' ', ' '],
    ['└', ' ', ' ',' ', '┘']
])

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
        if len(self._cards) == 0:
            screen.draw_matrix(empty_stack_matrix, self.position)
        else:
            yoffset = 0
            for card in self._cards:
                position = Vector2(self.position.x, self.position.y + yoffset)
                card.draw(screen, position)
                if card.face_down:
                    yoffset += 1
                else:
                    yoffset += 2
