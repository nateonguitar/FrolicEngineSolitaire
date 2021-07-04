import colorama
from frolic import GameObject, Matrix, MatrixBorder

face_down_matrix = Matrix([
    [' ', ' ', ' ', ' '],
    [' ', '#', '#', ' '],
    [' ', '#', '#', ' '],
    [' ', ' ', ' ', ' ']
])
face_down_matrix = face_down_matrix.with_border(MatrixBorder())

class Card(GameObject):
    def __init__(self, value: int, suit: str):
        if type(value) != int:
            raise Exception('value must be a string and must not be empty')
        if not suit:
            raise Exception('suit must be a string and must not be empty')
        self.face_down = True
        self.value = value
        self.suit = suit
        self.color = colorama.Fore.RED if suit == '♥' or suit == '♦' else colorama.Fore.GREEN
        matrix = Matrix.empty_sized(rows=4, columns=4, value=' ')
        border = MatrixBorder()
        matrix = matrix.with_border(border)
        matrix[1][1] = str(self.value)
        matrix[1][2] = f'{colorama.Style.BRIGHT}{self.color}{self.suit}{colorama.Style.RESET_ALL}'
        super().__init__(matrix=matrix)

    def flip(self):
        self.face_down = not self.face_down

