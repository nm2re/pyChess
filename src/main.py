# Example file showing a circle moving on screen
import pygame
from constants import *
from pieces import *

class Board:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SIZE,Constants.SIZE))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.grid = {} # Dictionary to store pieces on the board (position -> piece)



    def place_piece(self,piece):

        """
        Place a piece on the board
        :return:
        """
        self.grid[piece.position] = piece


    # TODO: - Finish this function
    def draw_all_pieces(self, screen, piece_images):
        """
        Create and place all the pieces, then draw them on the board.
        """
        # Drawing all pieces on the board
        # screen.blit(img, (0,0))



        img = pygame.transform.scale(piece_images["white-pawn"].convert_alpha(),(Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))

        for row in range(Constants.ROWS):
            for col in range(Constants.COLS):
                screen.blit(img,(row*Constants.SQUARE_SIZE,col*Constants.SQUARE_SIZE))






    def remove_piece(self, piece):
        """
        Remove a piece from the board notably when captured or promoted
        :param piece:
        :return:
        """


    def is_enemy_piece(self, position,color):
        """
        Checks if a piece at the given position is an enemy piece.
        :param position: Tuple (x, y) - The position to check.
        :param color: The color of the current piece ('white' or 'black').
        :return: True if the position contains an enemy piece, False otherwise.
        """

        piece = self.grid[position]

        # returns true if piece is different color from current piece
        return piece is not None and piece.color != color


    def make_board(self):
        """
        Makes board along with pieces
        :return:
        """
        colors = ['white','black']
        piece_images = {
            'white-pawn': pygame.image.load('../pieces-images/white-pawn.png'),
            'black-pawn': pygame.image.load('../pieces-images/black-pawn.png'),
            'white-rook': pygame.image.load('../pieces-images/white-rook.png'),
            'black-rook': pygame.image.load('../pieces-images/black-rook.png'),
            'white-knight': pygame.image.load('../pieces-images/white-knight.png'),
            'black-knight': pygame.image.load('../pieces-images/black-knight.png'),
            'white-bishop': pygame.image.load('../pieces-images/white-bishop.png'),
            'black-bishop': pygame.image.load('../pieces-images/black-bishop.png'),
            'white-queen': pygame.image.load('../pieces-images/white-queen.png'),
            'black-queen': pygame.image.load('../pieces-images/black-queen.png'),
            'white-king': pygame.image.load('../pieces-images/white-king.png'),
            'black-king': pygame.image.load('../pieces-images/black-king.png'),
        }

        for row in range(Constants.ROWS):
            for col in range(Constants.COLS):
                pygame.draw.rect(self.screen,colors[(row+col) % 2],(Constants.SQUARE_SIZE*row,Constants.SQUARE_SIZE*col, Constants.SQUARE_SIZE,Constants.SQUARE_SIZE))

        # self.draw_all_pieces(self.screen,piece_images)



        # Displays board
        pygame.display.flip()



    def play(self):
        """
        Runs the entire game
        :return:
        """

        self.make_board()
        # Board creation
        while self.running:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False



if __name__ == "__main__":
    renderBoard = Board()
    renderBoard.play()




