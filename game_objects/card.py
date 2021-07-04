import colorama
from frolic import GameObject, Matrix, MatrixBorder, Screen, Vector2

face_down_matrix = Matrix([
    [' ', ' ', ' ',' ', ' '],
    [' ', '#', '#','#', ' '],
    [' ', '#', '#','#', ' '],
    [' ', ' ', ' ',' ', ' ']
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
        matrix = Matrix.empty_sized(rows=4, columns=5, value=' ')
        border = MatrixBorder()
        matrix = matrix.with_border(border)
        if self.value == 1:
            display_value = 'A'
        elif self.value == 11:
            display_value = 'J'
        elif self.value == 12:
            display_value = 'Q'
        elif self.value == 13:
            display_value = 'K'
        else:
            display_value = str(self.value)

        if value == 10:
            matrix[1][1] = '1'
            matrix[1][2] = '0'
        else:
            matrix[1][1] = display_value
        
        matrix[1][3] = f'{colorama.Style.BRIGHT}{self.color}{self.suit}{colorama.Style.RESET_ALL}'
        super().__init__(matrix=matrix)

    def flip(self):
        self.face_down = not self.face_down

    def draw(self, screen: Screen, position: Vector2):
        if self.face_down:
            screen.draw_matrix(face_down_matrix, position)
        else:
            screen.draw_matrix(self.matrix, position)
