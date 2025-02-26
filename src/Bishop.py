from Pieces import Piece

class Bishop(Piece):
    def __init__(self, color, position, image_path):
        super().__init__(color, position, image_path)

        self.starting_position = position

    def possible_moves(self,board):
        """
        Moves for Bishop
        - Bishop moves diagonally across the board
        :param board:
        :return:
        """
        moves = []

        x,y = self.position

        # directions will only be the 4 diagonals


        return moves




    def can_capture(self, board):
        """
        Returns a list of positions that the bishop can capture
        :param board:
        :return:
        """
        pass


