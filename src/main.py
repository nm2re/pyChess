# Example file showing a circle moving on screen
import pygame
from constants import *
from pieces import *
from Pawn import *

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

    def initialize_pieces(self):
        """
        Initialize the board with all pieces in their starting positions.
        """
        # Place pawns
        for col in range(Constants.COLS):
            self.place_piece(Pawn(color='black', position=(1, col)))
            self.place_piece(Pawn(color='white', position=(6, col)))

        # Place rooks
        self.place_piece(Rook(color='black', position=(0, 0)))
        self.place_piece(Rook(color='black', position=(0, 7)))
        self.place_piece(Rook(color='white', position=(7, 0)))
        self.place_piece(Rook(color='white', position=(7, 7)))

        # Place knights
        self.place_piece(Knight(color='black', position=(0, 1)))
        self.place_piece(Knight(color='black', position=(0, 6)))
        self.place_piece(Knight(color='white', position=(7, 1)))
        self.place_piece(Knight(color='white', position=(7, 6)))

        # Place bishops
        self.place_piece(Bishop(color='black', position=(0, 2)))
        self.place_piece(Bishop(color='black', position=(0, 5)))
        self.place_piece(Bishop(color='white', position=(7, 2)))
        self.place_piece(Bishop(color='white', position=(7, 5)))

        # Place queens
        self.place_piece(Queen(color='black', position=(0, 3)))
        self.place_piece(Queen(color='white', position=(7, 3)))

        # Place kings
        self.place_piece(King(color='black', position=(0, 4)))
        self.place_piece(King(color='white', position=(7, 4)))

    # TODO: - Finish this function
    # def draw_all_pieces(self, screen, p_images):
    #     """
    #     Create and place all the piece, then draw them on the board.
    #     In the loop which builds the board, the parameters take inverted rows and columns.
    #     """
    #
    #     whitePawn_img = pygame.transform.scale(p_images["white-pawn"].convert_alpha(),(Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #     blackPawn_img = pygame.transform.scale(p_images["black-pawn"].convert_alpha(),(Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #
    #     whiteRook_img = pygame.transform.scale(p_images["white-rook"].convert_alpha(),(Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #     blackRook_img = pygame.transform.scale(p_images["black-rook"].convert_alpha(), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #
    #     blackBishop_img = pygame.transform.scale(p_images["black-bishop"].convert_alpha(), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #     whiteBishop_img = pygame.transform.scale(p_images["white-bishop"].convert_alpha(), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #
    #
    #     blackKnight_img = pygame.transform.scale(p_images["black-knight"].convert_alpha(), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #     whiteKnight_img = pygame.transform.scale(p_images["white-knight"].convert_alpha(), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
    #
    #     whiteQueen_img = pygame.transform.scale(p_images["white-queen"].convert_alpha(), (Constants.SQUARE_SIZE,Constants.SQUARE_SIZE))
    #     blackQueen_img = pygame.transform.scale(p_images["black-queen"].convert_alpha(), (Constants.SQUARE_SIZE,Constants.SQUARE_SIZE))
    #
    #     whiteKing_img = pygame.transform.scale(p_images["white-king"].convert_alpha(), (Constants.SQUARE_SIZE,Constants.SQUARE_SIZE))
    #     blackKing_img = pygame.transform.scale(p_images["black-king"].convert_alpha(), (Constants.SQUARE_SIZE,Constants.SQUARE_SIZE))
    #
    #
    #
    #     for row in range(Constants.ROWS):
    #         for col in range(Constants.COLS):
    #             screen.blit(blackPawn_img,(row*Constants.SQUARE_SIZE,1*Constants.SQUARE_SIZE))
    #             screen.blit(whitePawn_img,(row*Constants.SQUARE_SIZE,6*Constants.SQUARE_SIZE))
    #
    #             screen.blit(whiteRook_img,(0*Constants.SQUARE_SIZE,7*Constants.SQUARE_SIZE))
    #             screen.blit(whiteRook_img,(7*Constants.SQUARE_SIZE,7*Constants.SQUARE_SIZE))
    #             screen.blit(blackRook_img,(0*Constants.SQUARE_SIZE,0*Constants.SQUARE_SIZE))
    #             screen.blit(blackRook_img,(7*Constants.SQUARE_SIZE,0*Constants.SQUARE_SIZE))
    #
    #             screen.blit(whiteBishop_img, (2 * Constants.SQUARE_SIZE, 7 * Constants.SQUARE_SIZE))
    #             screen.blit(whiteBishop_img, (5 * Constants.SQUARE_SIZE, 7 * Constants.SQUARE_SIZE))
    #             screen.blit(blackBishop_img, (5 * Constants.SQUARE_SIZE, 0 * Constants.SQUARE_SIZE))
    #             screen.blit(blackBishop_img, (2 * Constants.SQUARE_SIZE, 0 * Constants.SQUARE_SIZE))
    #
    #
    #             screen.blit(whiteKnight_img, (1 * Constants.SQUARE_SIZE, 7 * Constants.SQUARE_SIZE))
    #             screen.blit(whiteKnight_img, (6 * Constants.SQUARE_SIZE, 7 * Constants.SQUARE_SIZE))
    #             screen.blit(blackKnight_img, (6 * Constants.SQUARE_SIZE, 0 * Constants.SQUARE_SIZE))
    #             screen.blit(blackKnight_img, (1 * Constants.SQUARE_SIZE, 0 * Constants.SQUARE_SIZE))
    #
    #             # Queen
    #             screen.blit(whiteQueen_img, (3 * Constants.SQUARE_SIZE, 7 * Constants.SQUARE_SIZE))
    #             screen.blit(blackQueen_img, (3 * Constants.SQUARE_SIZE, 0 * Constants.SQUARE_SIZE))
    #
    #             # King
    #             screen.blit(whiteKing_img, (4 * Constants.SQUARE_SIZE, 7 * Constants.SQUARE_SIZE))
    #             screen.blit(blackKing_img, (4 * Constants.SQUARE_SIZE, 0 * Constants.SQUARE_SIZE))




    def remove_piece(self, position):
        """
        Remove a piece from the board notably when captured or promoted
        :param position:
        :return:
        """
        if position in self.grid:
            return self.grid.pop(position) # Remove piece in the position provided
        else:
            return None



    def make_board(self):
        """
        Makes board along with pieces
        :return:
        """

        colors = ['white','black']
        colors[0] = pygame.Color(118,149,88)
        colors[1] = pygame.Color(239,237,111)

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

        self.draw_all_pieces(self.screen,piece_images)
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




