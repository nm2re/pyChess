# Example file showing a circle moving on screen
import pygame
from constants import *
from pieces import *
from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King

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
        if piece.position in self.grid:
            raise ValueError(f"Piece {piece.position} already placed")
        self.grid[piece.position] = piece



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



    def draw_all_pieces(self, screen, p_images):

        """
        Draw all the pieces on the board based on the positions on the grid
        :param screen: Screen to draw on
        :param p_images: Dictionary of images to draw
        :return:
        """

        for (row,col), piece in self.grid.items():
            piece_type = f"{piece.color}-{piece.__class__.__name__.lower()}"
            # print(piece_type)

            if piece_type in p_images:
                piece_img = pygame.transform.scale(p_images[piece_type].convert_alpha(), (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))
                screen.blit(piece_img, (col * Constants.SQUARE_SIZE, row * Constants.SQUARE_SIZE))



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


        # assigning colors for the board
        for row in range(Constants.ROWS):
            for col in range(Constants.COLS):
                pygame.draw.rect(self.screen,colors[(row+col) % 2],(Constants.SQUARE_SIZE*row,Constants.SQUARE_SIZE*col, Constants.SQUARE_SIZE,Constants.SQUARE_SIZE))

       # Draw pieces
        self.draw_all_pieces(self.screen,piece_images)
        # Displays board
        pygame.display.flip()



    def play(self):
        """
        Runs the entire game
        """

        self.initialize_pieces()
        selected_piece = None  # Track the currently selected piece
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the mouse click
                    x, y = pygame.mouse.get_pos()
                    row = y // Constants.SQUARE_SIZE
                    col = x // Constants.SQUARE_SIZE

                    print(row,col)

                    if (row,col) in self.grid:
                        selected_piece = self.grid[(row,col)]


                        ############### DEBUGGING ##############
                        if isinstance(selected_piece, Pawn):  # Check if the selected piece is a pawn

                            print(f"Pawn at {selected_piece.position} has moved: {selected_piece.has_moved()}")
                            print(f"Pawn can capture: {selected_piece.can_capture()}")
                            print(f"Pawn possible moves: {selected_piece.possible_moves(self)}")
                        ############### DEBUGGING ##############



                    # if selected_piece is None:
                    #     # Select a piece if one exists at the clicked position
                    #     if (row, col) in self.grid:
                    #         selected_piece = self.grid[(row, col)]
                    # else:
                    #     # Move the selected piece to the new position
                    #     if (row, col) in selected_piece.possible_moves(self):
                    #         self.remove_piece(selected_piece.position)
                    #         selected_piece.move((row, col), self)
                    #         self.place_piece(selected_piece)
                    #     selected_piece = None  # Deselect the piece
                    print(selected_piece)

            # Redraw the board and pieces



            self.make_board()
            pygame.display.flip()



if __name__ == "__main__":
    renderBoard = Board()
    renderBoard.play()




