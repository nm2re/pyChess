import pygame
from constants import *
from Pawn import Pawn
from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from King import King


class Board:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.SIZE, Constants.SIZE))
        pygame.display.set_caption("Chess - White's Turn")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.grid = {}  # Dictionary to store pieces on the board (position -> piece)
        self.current_turn = 'white'  # White starts first
        self.move_made = False  # Track if a move was made

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
        # Check if this is a valid move for the piece
        if new_position not in piece.possible_moves(self):
            raise ValueError('Invalid move for this piece')

        # Check if the move would put the king in check
        if self.move_will_put_king_in_check(piece, new_position):
            raise ValueError('This move would put your king in check')

        captured_piece = self.remove_piece(new_position)  # Remove any enemy piece at new_position

        self.remove_piece(piece.position)
        piece.position = new_position
        self.place_piece(piece)

        # Move was successful, so toggle the turn
        self.move_made = True

        return captured_piece  # Return captured piece (if any)

    def toggle_turn(self):
        """
        Switch the current turn between white and black.
        """
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        pygame.display.set_caption(f"Chess - {self.current_turn.capitalize()}'s Turn")

    def initialize_pieces(self):
        """
        Initialize the board with all pieces in their starting positions.
        """
        # Place pawns
        for col in range(Constants.COLS):
            self.place_piece(Pawn(color='black', position=(1, col), image_path="../pieces-images/black-pawn.png"))
            self.place_piece(Pawn(color='white', position=(6, col), image_path="../pieces-images/white-pawn.png"))

        # Place rooks
        self.place_piece(Rook(color='black', position=(0, 0), image_path="../pieces-images/black-rook.png"))
        self.place_piece(Rook(color='black', position=(0, 7), image_path="../pieces-images/black-rook.png"))
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

    def draw_board(self):
        """
        Draws just the chess board squares without any pieces.
        """
        colors = [pygame.Color(118, 149, 88), pygame.Color(239, 237, 111)]

        # Assigning colors for the board
        for row in range(Constants.ROWS):
            for col in range(Constants.COLS):
                pygame.draw.rect(self.screen, colors[(row + col) % 2],
                                 (col * Constants.SQUARE_SIZE, row * Constants.SQUARE_SIZE,
                                  Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))

    def draw_pieces(self, exclude_piece=None):
        """
        Draws all pieces except the specified one.
        """
        for (row, col), piece in self.grid.items():
            if piece != exclude_piece:  # Skip the excluded piece
                self.screen.blit(piece.image, (col * Constants.SQUARE_SIZE, row * Constants.SQUARE_SIZE))

    def draw_move_indicators(self, piece):
        """
        Draws indicators (dots) for all possible moves of the selected piece.
        """
        if not piece:
            return

        if isinstance(piece, King):
            basic_moves = piece.get_basic_moves(self)
        else:
            basic_moves = piece.possible_moves(self)
        valid_moves = [move for move in basic_moves if not self.move_will_put_king_in_check(piece, move)]

        for row, col in valid_moves:
            center_x = col * Constants.SQUARE_SIZE + Constants.SQUARE_SIZE // 2
            center_y = row * Constants.SQUARE_SIZE + Constants.SQUARE_SIZE // 2

            indicator_radius = Constants.SQUARE_SIZE // 6
            dot_surface = pygame.Surface((indicator_radius * 2, indicator_radius * 2), pygame.SRCALPHA)

            if (row, col) in self.grid:
                pygame.draw.circle(dot_surface, (255, 0, 0, 160), (indicator_radius, indicator_radius),
                                   indicator_radius)
            else:
                pygame.draw.circle(dot_surface, (128, 128, 128, 160), (indicator_radius, indicator_radius),
                                   indicator_radius)
            self.screen.blit(dot_surface, (center_x - indicator_radius, center_y - indicator_radius))


    ###### KING CONDITIONS #############

    def get_king(self, color):
        """
        Finds and returns the King piece for the given color.
        """
        for piece in self.grid.values():
            if isinstance(piece, King) and piece.color == color:
                return piece

        # If no king is found, print debug info and return a default king
        print(f"WARNING: No {color} king found on the board!")
        print(f"Current pieces: {[(p.color, p.__class__.__name__, p.position) for p in self.grid.values()]}")

        # Create a dummy king off the board to prevent NoneType errors
        dummy_king = King(color=color, position=(-1, -1), image_path=f"../pieces-images/{color}-king.png")
        return dummy_king

    def is_stalemate(self, color):
        """
        Checks if a player is in stalemate.
        - Stalemate occurs when the player has no legal moves, but is NOT in check.
        :param color: The player color being checked.
        :return: True if it's a stalemate, False otherwise.
        """
        king = self.get_king(color)

        # Make sure king exists
        if king.position == (-1, -1):  # This is our dummy king
            return False

        if king.is_check(self):
            return False  # Not stalemate if in check

        # Check if any piece has a valid move that doesn't put king in check
        for piece in self.grid.values():
            if piece.color == color:
                # Get all possible moves without check validation
                if isinstance(piece, King):
                    basic_moves = piece.get_basic_moves(self)
                else:
                    basic_moves = piece.possible_moves(self)

                # Check if any move is legal (doesn't put king in check)
                for move in basic_moves:
                    if not self.move_will_put_king_in_check(piece, move):
                        return False  # Found a legal move, so not stalemate

        return True  # No legal moves found, it's stalemate

    def move_will_put_king_in_check(self, piece, new_position):
        """
        Simulates a move to check if it would put the current player's King in check.
        :param piece: The piece being moved.
        :param new_position: The destination square.
        :return: True if the move results in a check, False otherwise.
        """
        king = self.get_king(piece.color)

        # Make sure king exists
        if king.position == (-1, -1):  # This is our dummy king
            return False

        original_position = piece.position
        captured_piece = self.grid.get(new_position)  # Save any piece that would be captured

        # Simulate the move
        if original_position in self.grid:
            del self.grid[original_position]  # Remove piece from original position
        self.grid[new_position] = piece  # Place piece at new position

        # Save the original position before changing it
        temp_position = piece.position
        piece.position = new_position  # Update piece position

        # Check if king is under attack
        in_check = king.is_check(self)

        # Undo the move
        if new_position in self.grid:
            del self.grid[new_position]
        if captured_piece:
            self.grid[new_position] = captured_piece  # Restore captured piece
        self.grid[original_position] = piece  # Restore the moved piece
        piece.position = temp_position  # Reset position to original

        return in_check

    def check_game_state(self):
        """
        Checks if the current player is in check, checkmate, or stalemate.
        """
        king = self.get_king(self.current_turn)

        # Make sure king exists
        if king.position == (-1, -1):  # This is our dummy king
            print(f"ERROR: {self.current_turn} king not found, cannot check game state")
            return

        if king.is_check(self):
            print(f"{self.current_turn} King is in CHECK!")

            # Check if any piece has a move that would get out of check
            has_valid_move = False
            for piece in list(self.grid.values()):
                if piece.color == self.current_turn:
                    # For each piece of the current player's color
                    if isinstance(piece, King):
                        moves = piece.get_basic_moves(self)
                    else:
                        moves = piece.possible_moves(self)

                    for move in moves:
                        if not self.move_will_put_king_in_check(piece, move):
                            has_valid_move = True
                            break

                if has_valid_move:
                    break

            if not has_valid_move:
                print(f"CHECKMATE! {self.current_turn} loses!")
                self.running = False  # End the game
                return

        # Check for stalemate (King is NOT in check, but has no legal moves)
        elif self.is_stalemate(self.current_turn):
            print(f"STALEMATE! {self.current_turn} has no legal moves. Game ends in a draw.")
            self.running = False  # End the game

    def play(self):
        """
        Runs the game loop with drag-and-drop functionality and turn-based play.
        - Prevents illegal moves that put the king in check.
        - Detects check and checkmate after each move.
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

                    # Reset previous drag state if selecting a new piece while already dragging
                    if dragging:
                        dragging = False
                        selected_piece = None
                        dragged_piece_image = None

                    if (row, col) in self.grid:
                        piece = self.grid[(row, col)]

                        # Only allow selecting pieces of the current turn's color
                        if piece.color == self.current_turn:
                            selected_piece = piece
                            dragging = True
                            drag_offset = (x - col * Constants.SQUARE_SIZE, y - row * Constants.SQUARE_SIZE)

                            # Load the image correctly
                            dragged_piece_image = pygame.transform.scale(selected_piece.image,
                                                                         (Constants.SQUARE_SIZE, Constants.SQUARE_SIZE))

                            # Debugging Info
                            print(f"{selected_piece.__class__.__name__} selected at {selected_piece.position}")
                            print(f"Possible moves: {selected_piece.possible_moves(self)}")
                            if hasattr(selected_piece, 'can_capture'):
                                print(f"Can capture: {selected_piece.can_capture(self)}")
                        else:
                            print(f"Not your turn! Current turn: {self.current_turn}")


                elif event.type == pygame.MOUSEBUTTONUP and dragging:
                    x, y = pygame.mouse.get_pos()
                    new_row, new_col = y // Constants.SQUARE_SIZE, x // Constants.SQUARE_SIZE
                    new_position = (new_row, new_col)
                    if selected_piece and new_position != selected_piece.position:
                        try:

                            # Move the piece
                            self.move_made = False  # Reset move flag
                            captured_piece = self.move_piece(new_position, selected_piece)

                            if captured_piece:
                                print(
                                    f"{captured_piece.__class__.__name__} captured at {new_position} by {selected_piece.__class__.__name__}")

                            # If move was successful, check for check/checkmate/stalemate

                            if self.move_made:
                                self.toggle_turn()
                                print(f"Turn changed to {self.current_turn}")
                                self.check_game_state()


                        except ValueError as e:
                            print(f"Invalid move: {e}")
                            # Make sure the piece stays in the grid at its original position
                            if selected_piece.position not in self.grid:
                                self.grid[selected_piece.position] = selected_piece

                    # Reset dragging state

                    selected_piece = None
                    dragging = False
                    dragged_piece_image = None

                elif event.type == pygame.MOUSEMOTION and dragging:
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Track mouse movement

            # Set a consistent frame rate to avoid flickering
            self.clock.tick(60)
            self.draw_board()  # Just draw the board squares

            # Draw move indicators if a piece is selected
            if dragging and selected_piece:
                # Draw move indicators before pieces to make them appear behind
                self.draw_move_indicators(selected_piece)
                self.draw_pieces(exclude_piece=selected_piece)  # Draw all pieces except the dragged one
                self.screen.blit(dragged_piece_image,
                                 (mouse_x - drag_offset[0], mouse_y - drag_offset[1]))  # Draw dragged piece
            else:
                self.draw_pieces()  # Draw all pieces when not dragging

            pygame.display.update()


if __name__ == "__main__":
    renderBoard = Board()
    renderBoard.play()