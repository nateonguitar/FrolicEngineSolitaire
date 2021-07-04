from frolic import GameObject, Matrix, MatrixBorder

class Card(GameObject):
    def __init__(self, value: str, suit: str):
        if not value:
            raise Exception('value must be a string and must not be empty')
        if not suit:
            raise Exception('suit must be a string and must not be empty')
        self.value = value
        self.suit = suit
        matrix = Matrix.empty_sized(rows=4, columns=4, value=' ')
        border = MatrixBorder()
        matrix = matrix.with_border(border)
        matrix[1][1] = self.value
        matrix[1][2] = self.suit
        super().__init__(matrix=matrix)
