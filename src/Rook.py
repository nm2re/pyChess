from Pieces import Piece
from constants import *
class Rook(Piece):
    def __init__(self, color, position, image_path):
        """
        Rook Movement is streamlined and focuses on straight horizontal and vertical lines
        :param color:
        :param position:
        :param image_path:
        """
        super().__init__(color, position, image_path)
        self.starting_position = position

    def has_moved(self):
        """
        Checking for Castling
        :return:
        """
        return self.starting_position == self.position

    def possible_moves(self, board):
        """
        Returns all valid moves for the Rook.
        The Rook can move horizontally or vertically until:
        - The board edge is reached.
        - A friendly piece blocks the path.
        - An enemy piece is encountered (it can be captured, but movement stops).
        """

        moves = []
        x, y = self.position  # Current position of the Rook

        directions = [
            (1, 0),  # Down
            (-1, 0),  # Up
            (0, 1),  # Right
            (0, -1)  # Left
        ]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            while 0 <= new_x < Constants.ROWS and 0 <= new_y < Constants.COLS:
                if (new_x, new_y) in board.grid:
                    piece = board.grid[(new_x, new_y)]

                    if piece.color != self.color:  # Enemy piece → can capture
                        moves.append((new_x, new_y))

                    break  # Stop moving after hitting any piece

                moves.append((new_x, new_y))  # Empty square → valid move
                new_x += dx
                new_y += dy
        return moves

    def can_capture(self, board):
        """
        Returns a list of enemy pieces that the Rook can capture.
        The Rook can capture an opponent piece if it is directly in its path
        (horizontally or vertically) without a friendly piece blocking it.

        :param board:
        :return:
        """

        capture_moves = []
        x, y = self.position

        directions = [
            (1, 0),  # Down
            (-1, 0),  # Up
            (0, 1),  # Right
            (0, -1)  # Left
        ]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            while 0 <= new_x < Constants.ROWS and 0 <= new_y < Constants.COLS:
                if (new_x, new_y) in board.grid:
                    piece = board.grid[(new_x, new_y)]

                    if piece.color != self.color:  # Enemy piece → Can capture
                        capture_moves.append((new_x, new_y))

                    break  # Stop checking after first piece in path

                new_x += dx
                new_y += dy

        return capture_moves





