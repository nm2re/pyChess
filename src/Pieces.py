class Piece:
    """
    Base class for all pieces
    """

    def __init__(self,color, position):
        self.color = color
        self.position = position # Position of each piece is passed as a tuple (x,y)




    def possible_moves(self,board):
        """
         -- Class to be inherited by the individual pieces --

        Where the piece can move preferably a list
        """


    def can_capture(self):
        """
        If a piece can capture another piece

        Class to be inherited by the individual pieces
        :return:
        """


    def move_piece(self, new_position, board):
        """
        Method to move a piece from initial coordinate to new_position
        """
        if new_position not in self.possible_moves(board):
            raise ValueError('Invalid move for this piece')

            # Remove the piece from its current position
        board.remove_piece(self.position)

        self.position = new_position
        board.place_piece(self)


    def is_enemy_piece(self, position,color):
        """
        Checks if a piece at the given position is an enemy piece.
        :param position: Tuple (x, y) - The position to check.
        :param color: The color of the current piece ('white' or 'black').
        :return: True if the position contains an enemy piece, False otherwise.
        """


    @staticmethod
    def remove_piece(self,position, board):
        """
        Used to remove a piece from its initial position on the board.

        -> Captures of Pieces
        -> Movement of normal pieces from one position to another
        """

        return board.grid.pop(position, None)

