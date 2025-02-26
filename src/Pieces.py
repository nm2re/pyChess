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
        -- Class to be inherited by the individual pieces --
        Returns a list of pieces that can be captured by this piece
        :return:
        """

