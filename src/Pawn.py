from Pieces import Piece

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color,position)
        self.starting_position = position


    def has_moved(self):
        """
        To check if the pawn has moved for two conditions
         -> Pawn can move two squares if it has not moved before
         -> To allow for enpassant captures which requires the pawns to not have moved initially
        """
        return self.starting_position != self.position


    # def can_capture(self):
    #     """
    #     Will return boolean if the piece can capture a piece or not
    #     """



    def possible_moves(self, board):
        """
        Possible moves that pawn can move.
        Includes a list of normal moves and capture moves
        :return: List of possible moves
        """
        moves = []  # List of moves that pawn can make
        x, y = self.position

        # Determine direction based on color
        forward = -1 if self.color == 'white' else 1  # White moves up (-1), Black moves down (+1)

        one_step = (x + forward, y)
        two_step = (x + forward * 2, y)

        if one_step not in board.grid:
            moves.append(one_step)
            if not self.has_moved() and two_step not in board.grid:
                moves.append(two_step)

        # Diagonal movement for captures only

        print(board.grid[self.position].color)
        for dx in [-1, 1]: # checking diagonals left and right
            diagonal = (x + forward, y + dx)

            if (diagonal in board.grid) and board.grid[diagonal].color != self.color:  # board.grid[diagonal] --> Piece on that coordinate
                moves.append(diagonal)

        return moves




