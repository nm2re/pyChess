import pygame
from constants import  *
class Piece:
    """
    Base class for all pieces
    """

    def __init__(self, color, position, image_path=None):
        self.color = color
        self.position = position # Position of each piece is passed as a tuple (x,y)
        self.image = pygame.image.load(image_path)  # Load the image
        self.image = pygame.transform.scale(self.image, (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))  # Resize



    def possible_moves(self,board):
        """
         -- Class to be inherited by the individual pieces --

        Where the piece can move preferably a list
        """


    def can_capture(self, board):
        """
        If a piece can capture another piece

        Class to be inherited by the individual pieces
        :return:
        """

    #
    # def is_enemy_piece(self, position,color):
    #     """
    #     Checks if a piece at the given position is an enemy piece.
    #     :param position: Tuple (x, y) - The position to check.
    #     :param color: The color of the current piece ('white' or 'black').
    #     :return: True if the position contains an enemy piece, False otherwise.
    #     """
    #


