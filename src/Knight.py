from Pieces import Piece
from constants import *

class Knight(Piece):
    def __init__(self, color, position, image_path):
        super().__init__(color, position, image_path)

    def possible_moves(self, board):
        """
        Moves for Knight
        - Knight moves in an L-shape: 2 squares in one direction and then 1 square perpendicular
        :param board: The chess board
        :return: List of valid positions the knight can move to
        """
        moves = []
        x, y = self.position

        # Knight's L-shaped movements (all 8 possible L-shapes)
        directions = [
            (2, 1),  # 2 down, 1 right
            (2, -1),  # 2 down, 1 left
            (-2, 1),  # 2 up, 1 right
            (-2, -1),  # 2 up, 1 left
            (1, 2),  # 1 down, 2 right
            (1, -2),  # 1 down, 2 left
            (-1, 2),  # 1 up, 2 right
            (-1, -2)  # 1 up, 2 left
        ]

        for dx, dy in directions:
            current_x, current_y = x + dx, y + dy

            # Check if the position is within the board bounds
            if 0 <= current_x < Constants.ROWS and 0 <= current_y < Constants.COLS:
                # Unlike other pieces, knights can jump over pieces
                # Only need to check the destination square
                if (current_x, current_y) in board.grid:
                    piece = board.grid[(current_x, current_y)]
                    # Add the move if the destination is empty or has an enemy piece
                    if piece.color != self.color:
                        moves.append((current_x, current_y))
                else:
                    # Empty square - valid move
                    moves.append((current_x, current_y))

        return moves

    def can_capture(self, board):
        capture_moves = []
        x,y = self.position

        directions = [
            (2, 1),  # 2 down, 1 right
            (2, -1),  # 2 down, 1 left
            (-2, 1),  # 2 up, 1 right
            (-2, -1),  # 2 up, 1 left
            (1, 2),  # 1 down, 2 right
            (1, -2),  # 1 down, 2 left
            (-1, 2),  # 1 up, 2 right
            (-1, -2)  # 1 up, 2 left
        ]

        for dx, dy in directions:
            current_x, current_y = x + dx, y + dy

            # Check if the position is within the board bounds
            if 0 <= current_x < Constants.ROWS and 0 <= current_y < Constants.COLS:
                if (current_x, current_y) in board.grid:
                    piece = board.grid[(current_x, current_y)]
                    if piece.color != self.color:
                        capture_moves.append((current_x, current_y))

        return capture_moves