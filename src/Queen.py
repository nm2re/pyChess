from Pieces import Piece
from constants import *
class Queen(Piece):
    def __init__(self, color, position, image_path):
        super().__init__(color, position, image_path)

        self.starting_position = position


    def possible_moves(self, board):
        moves = []
        x,y = self.position
        # Queen is a combination of bishop and rook thus

        directions = [ # will include all 8 directions
            (1, 0),  # Down
            (-1, 0),  # Up
            (0, 1),  # Right
            (0, -1),  # Left
            (-1, -1),  # top left
            (-1, 1),  # top right
            (1, -1),  # bottom left
            (1, 1)  # bottom right

        ]

        for dx,dy in directions:
            current_x, current_y = x + dx, y + dy

            while 0 <= current_x < Constants.ROWS and 0 <= current_y < Constants.COLS:
                if (current_x, current_y) in board.grid:
                    piece = board.grid[(current_x, current_y)] # Piece in position
                    # check if enemy piece
                    if piece.color != self.color:
                        moves.append((current_x, current_y))
                    break # it only identifies first piece in position
                moves.append((current_x, current_y))
                current_x, current_y = current_x + dx, current_y + dy
        return moves


    def can_capture(self, board):
        """
        Pieces which the Queen can capture on the board
        :param board:
        :return:
        """

        capture_moves = []
        x,y = self.position
        directions = [  # will include all 8 directions
            (1, 0),  # Down
            (-1, 0),  # Up
            (0, 1),  # Right
            (0, -1),  # Left
            (-1, -1),  # top left
            (-1, 1),  # top right
            (1, -1),  # bottom left
            (1, 1)  # bottom right

        ]

        for dx, dy in directions:
            current_x, current_y = x + dx, y + dy

            while 0 <= current_x < Constants.ROWS and 0 <= current_y < Constants.COLS:
                if (current_x, current_y) in board.grid:
                    piece = board.grid[(current_x, current_y)]  # Piece in position
                    # check if enemy piece
                    if piece.color != self.color:
                        capture_moves.append((current_x, current_y))
                    break  # it only identifies first piece in position

                current_x, current_y = current_x + dx, current_y + dy
        return capture_moves

