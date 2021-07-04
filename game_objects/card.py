import colorama
from frolic import GameObject, Matrix, MatrixBorder

class Card(GameObject):
    def __init__(self, value: str, suit: str):
        if not value:
            raise Exception('value must be a string and must not be empty')
        if not suit:
            raise Exception('suit must be a string and must not be empty')
        self.value = value
        self.suit = suit
        self.color = colorama.Fore.RED if suit == '♥' or suit == '♦' else colorama.Fore.GREEN
        matrix = Matrix.empty_sized(rows=4, columns=4, value=' ')
        border = MatrixBorder()
        matrix = matrix.with_border(border)
        matrix[1][1] = self.value
        matrix[1][2] = f'{colorama.Style.BRIGHT}{self.color}{self.suit}{colorama.Style.RESET_ALL}'
        super().__init__(matrix=matrix)
