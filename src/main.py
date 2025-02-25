# Example file showing a circle moving on screen
import pygame
from constants import *
from Pieces import Piece
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


    def place_piece(self, piece):
        """
        Place a piece on the board.
        """
        if piece.position in self.grid:
            raise ValueError(f"Piece {piece.position} already placed")
        self.grid[piece.position] = piece



    def remove_piece(self, position):
        """
        Remove a piece from the board when captured or moved.
        """
        return self.grid.pop(position, None)  # Remove and return the piece if it exists



    def move_piece(self, new_position, piece):
        """
        Moves a piece from its current position to a new position.
        Includes capturing opponent pieces.
        Incorporates place_piece() and remove_piece() methods
        """

        if new_position not in piece.possible_moves(self):
            raise ValueError('Invalid move for this piece')

        captured_piece = self.remove_piece(new_position)  # Remove any enemy piece at new_position

        self.remove_piece(piece.position)
        piece.position = new_position
        self.place_piece(piece)

        return captured_piece  # Return captured piece (if any)

    def initialize_pieces(self):
        """
        Initialize the board with all pieces in their starting positions.
        """
        # Place pawns
        for col in range(Constants.COLS):
            self.place_piece(Pawn(color='black', position=(1, col),image_path="../pieces-images/black-pawn.png"))
            self.place_piece(Pawn(color='white', position=(6, col),image_path="../pieces-images/white-pawn.png"))


        # testing
        self.place_piece(Pawn(color='black', position=(5,3),image_path="../pieces-images/black-pawn.png"))

        # Place rooks
        self.place_piece(Rook(color='black', position=(0, 0), image_path="../pieces-images/black-rook.png"))
        self.place_piece(Rook(color='black', position=(0, 7),image_path="../pieces-images/black-rook.png"))
        self.place_piece(Rook(color='white', position=(7, 0), image_path="../pieces-images/white-rook.png"))
        self.place_piece(Rook(color='white', position=(7, 7), image_path="../pieces-images/white-rook.png"))

        # Place knights
        self.place_piece(Knight(color='black', position=(0, 1), image_path="../pieces-images/black-knight.png"))
        self.place_piece(Knight(color='black', position=(0, 6), image_path="../pieces-images/black-knight.png"))
        self.place_piece(Knight(color='white', position=(7, 1), image_path="../pieces-images/white-knight.png"))
        self.place_piece(Knight(color='white', position=(7, 6), image_path="../pieces-images/white-knight.png"))

        # Place bishops
        self.place_piece(Bishop(color='black', position=(0, 2), image_path="../pieces-images/black-bishop.png"))
        self.place_piece(Bishop(color='black', position=(0, 5), image_path="../pieces-images/black-bishop.png"))
        self.place_piece(Bishop(color='white', position=(7, 2), image_path="../pieces-images/white-bishop.png"))
        self.place_piece(Bishop(color='white', position=(7, 5), image_path="../pieces-images/white-bishop.png"))

        # Place queens
        self.place_piece(Queen(color='black', position=(0, 3), image_path="../pieces-images/black-queen.png"))
        self.place_piece(Queen(color='white', position=(7, 3), image_path="../pieces-images/white-queen.png"))

        # Place kings
        self.place_piece(King(color='black', position=(0, 4), image_path="../pieces-images/black-king.png"))
        self.place_piece(King(color='white', position=(7, 4), image_path="../pieces-images/white-king.png"))


    def make_board(self):
        """
        Draws the board along with all pieces, except the currently dragged one.
        """
        colors = [pygame.Color(118, 149, 88), pygame.Color(239, 237, 111)]

        # Assigning colors for the board
        for row in range(Constants.ROWS):
            for col in range(Constants.COLS):
                pygame.draw.rect(self.screen,colors[(row+col) % 2],(Constants.SQUARE_SIZE*row,Constants.SQUARE_SIZE*col, Constants.SQUARE_SIZE,Constants.SQUARE_SIZE))

        # Draw all pieces except the one being dragged
        for (row, col), piece in self.grid.items():
            # if piece != dragging_piece:  # Skip the dragged piece
                self.screen.blit(piece.image, (col * Constants.SQUARE_SIZE, row * Constants.SQUARE_SIZE))

        pygame.display.flip()

    def play(self):
        """
        Runs the game loop with drag-and-drop functionality.
        """

        self.initialize_pieces()
        selected_piece = None  # Track the currently selected piece
        dragging = False
        drag_offset = (0, 0)
        dragged_piece_image = None  # Stores the image of the dragged piece
        mouse_x, mouse_y = 0, 0  # Track mouse position

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    row, col = y // Constants.SQUARE_SIZE, x // Constants.SQUARE_SIZE

                    if (row, col) in self.grid:
                        selected_piece = self.grid[(row, col)]
                        dragging = True
                        drag_offset = (x - col * Constants.SQUARE_SIZE,y - row * Constants.SQUARE_SIZE)  # Offset for smooth dragging
                        dragged_piece_image = selected_piece.image  # Store piece image
                        # Debugging Info
                        if isinstance(selected_piece, Pawn):
                            print(f"Pawn at {selected_piece.position} has moved: {selected_piece.has_moved()}")
                            print(f"Pawn can capture: {selected_piece.can_capture(self)}")
                            print(f"Pawn possible moves: {selected_piece.possible_moves(self)}")

                        if isinstance(selected_piece, Rook):
                            print(f"Rook at {selected_piece.position} has moved: {selected_piece.has_moved()}")
                            print(f"Rook can capture: {selected_piece.can_capture(self)}")
                            print(f"Rook possible moves: {selected_piece.possible_moves(self)}")


                elif event.type == pygame.MOUSEBUTTONUP and dragging:
                    x, y = pygame.mouse.get_pos()
                    new_row, new_col = y // Constants.SQUARE_SIZE, x // Constants.SQUARE_SIZE
                    new_position = (new_row, new_col)

                    if selected_piece:
                        try:
                            captured_piece = self.move_piece(new_position, selected_piece)
                            if captured_piece:
                                print(f"{captured_piece} captured at {new_position}")  # Debugging capture event
                        except ValueError as e:
                            print(f"Invalid move: {e}")  # Debugging invalid move

                    # Reset dragging state
                    selected_piece = None
                    dragging = False
                    dragged_piece_image = None

                elif event.type == pygame.MOUSEMOTION and dragging:
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Track mouse movement

            # Redraw the board and pieces
            self.make_board()

            if dragging and dragged_piece_image:
                self.screen.blit(dragged_piece_image, (mouse_x - drag_offset[0], mouse_y - drag_offset[1]))

            pygame.display.flip()


if __name__ == "__main__":
    renderBoard = Board()
    renderBoard.play()




