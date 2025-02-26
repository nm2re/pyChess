from Pieces import Piece

class Queen(Piece):
    def __init__(self, color, position, image_path):
        super().__init__(color, position, image_path)

        self.starting_position = position

