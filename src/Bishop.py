from Pieces import Piece
from constants import *

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

        directions = [
            (-1, -1), # top left
            (-1, 1),# top right
            (1, -1),# bottom left
            (1, 1)# bottom right
        ]

        for dx,dy in directions:
            current_x, current_y = x + dx, y + dy

            while 0 < current_x < Constants.ROWS and 0 < current_y < Constants.COLS:
                if (current_x, current_y) in board.grid:
                    piece = board.grid[(current_x, current_y)]

                    if piece.color != self.color:
                        moves.append((current_x, current_y))
                    break

                moves.append((current_x, current_y))
                current_x, current_y = current_x + dx, current_y + dy

        return moves


    def can_capture(self, board):
        """
        Returns a list of positions that the bishop can capture
        :param board:
        :return:
        """
        capture_moves = []

        x,y = self.position
        directions = [
            (-1, -1),  # top left
            (-1, 1),  # top right
            (1, -1),  # bottom left
            (1, 1)  # bottom right
        ]

        for dx,dy in directions:
            current_x,current_y = x + dx, y + dy

            while 0 <= current_x < Constants.ROWS and 0 <= current_y < Constants.COLS:
                if (current_x, current_y) in board.grid: # If theres a piece on the board
                    piece = board.grid[(current_x, current_y)]

                    if piece.color != self.color:
                        capture_moves.append((current_x, current_y))

                    break
                current_x, current_y = current_x + dx, current_y + dy

        return capture_moves


