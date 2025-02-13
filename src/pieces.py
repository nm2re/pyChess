import pygame

class Piece:
    """
    Base class for all pieces
    """

    def __init__(self,color,):
        pass



    def possible_moves(self,board):
        """
        Where the piece can move preferably a list
        :return:
        """


    def can_capture(self):

        """
        If a piece can capture another piece
        :return:
        """


    def move(self, current_position, new_position):
        """
        Where the move is made
        :return:
        """




# class Pawn(Piece):
#     """
#     State of the pawn.
#     Movement description of Pawns
#     """
#
#     def __init__(self, color, position):
#         super().__init__(color, position)
#         self.start_position = position # Storing initial position of the Pawn
#
#
#     def has_moved(self):
#         """
#         Shows whether the pawn has moved initially
#         """
#         return self.position != self.start_position
#
#
#     def possible_moves(self,board):
#         """
#         Return all possible moves for the pawn
#         :return:
#         """
#
#         moves = []
#
#         # Black pawn or white pawn movement
#         direction = 1 if self.color == 'black' else -1
#
#         # Normal movement
#         next_position = (self.position[0] + direction, self.position[1])
#         if board.is_empty(next_position): moves.append(next_position)
#
#         # Double movement
#         if not self.has_moved():
#             double_step = (self.position[0] + (direction*2), self.position[1])
#             if board.is_empty(double_step): moves.append(double_step)
#
#         # Capture
#         # if piece in diagonals capture it
#
#
#
#         return moves
#
#
#
#     def move(self, new_position):
#         """
#         Move the pawn to new position
#         :return:
#         """
#         super().move(new_position)
#         # test




class Knight(Piece):
    """
    State of the knight.
    """


class King(Piece):
    """
    State of the king.
    """


class Queen(Piece):
    """
    State of the queen.
    """

class Bishop(Piece):
    """
    State of the bishop.
    """

class Rook(Piece):
    """
    State of the rook.
    """





