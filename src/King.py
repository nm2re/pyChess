from Pieces import Piece
from Pawn import Pawn

class King(Piece):
    """
    King moveset:
    - Can move one square in any direction
    - Cannot move into check
    - Supports castling (to be implemented later)
    - Handles check and checkmate logic
    """

    def __init__(self, color, position, image_path):
        super().__init__(color, position, image_path)

    def get_basic_moves(self, board):
        """
        Returns all basic moves for the King without check validation.
        :param board: The current board state
        :return: List of basic move positions
        """
        moves = []
        x, y = self.position

        # Possible king moves (one step in any direction)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
            (0, -1), (0, 1),  # Left, Right
            (1, -1), (1, 0), (1, 1)  # Bottom-left, Bottom, Bottom-right
        ]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < 8 and 0 <= new_y < 8:  # Stay inside the board
                if (new_x, new_y) not in board.grid or board.grid[(new_x, new_y)].color != self.color:
                    moves.append((new_x, new_y))

        return moves

    def possible_moves(self, board, check_for_check=True):
        """
        Returns all possible moves for the King.
        - The King can move one step in any direction.
        - The King cannot move into check.
        :param board: The current board state
        :param check_for_check: Whether to check if the move puts the king in check
        :return: List of valid move positions
        """
        basic_moves = self.get_basic_moves(board)

        if not check_for_check:
            return basic_moves

        # Filter out moves that would put the king in check
        valid_moves = []
        for move in basic_moves:
            if not self.will_be_in_check(move, board):
                valid_moves.append(move)

        return valid_moves

    def can_capture(self, board):
        """
        Returns a list of pieces the King can capture.
        :param board: The current board state
        :return: List of capturable enemy piece positions
        """
        captures = []
        for move in self.possible_moves(board):
            if move in board.grid and board.grid[move].color != self.color:
                captures.append(move)
        return captures

    def will_be_in_check(self, new_position, board):
        """
        Determines if moving to a new position will put the King in check.
        :param new_position: The new position to check
        :param board: The current board state
        :return: True if the move puts the King in check, False otherwise
        """
        # Create a hypothetical board state
        original_position = self.position
        original_piece_at_new_position = None
        # Save piece at new position if there is one
        if new_position in board.grid:
            original_piece_at_new_position = board.grid[new_position]
        # Temporarily update the board state
        self.position = new_position
        board.grid[new_position] = self
        if original_position in board.grid:
            del board.grid[original_position]
        # Check if any opponent piece can attack the king's new position
        in_check = False
        for piece in list(board.grid.values()):
            if piece is not self and piece.color != self.color:
                # For enemy kings, use basic moves to avoid recursion
                if isinstance(piece, King):
                    attack_moves = piece.get_basic_moves(board)
                # For pawns, calculate attack squares directly instead of using can_capture
                elif isinstance(piece, Pawn):
                    attack_moves = []
                    x, y = piece.position
                    forward = -1 if piece.color == 'white' else 1
                    # Left diagonal attack
                    left_diag = (x + forward, y - 1)
                    if 0 <= left_diag[0] < 8 and 0 <= left_diag[1] < 8:  # Ensure it's on the board
                        attack_moves.append(left_diag)
                    # Right diagonal attack
                    right_diag = (x + forward, y + 1)
                    if 0 <= right_diag[0] < 8 and 0 <= right_diag[1] < 8:  # Ensure it's on the board
                        attack_moves.append(right_diag)
                else:
                    # For other pieces, check if they can capture the king
                    # without the recursive check_for_check parameter
                    if hasattr(piece, 'possible_moves') and callable(piece.possible_moves):
                        # Handle possible differences in method signatures
                        try:
                            if 'check_for_check' in piece.possible_moves.__code__.co_varnames:
                                attack_moves = piece.possible_moves(board, check_for_check=False)
                            else:
                                attack_moves = piece.possible_moves(board)
                        except TypeError:
                            attack_moves = piece.possible_moves(board)
                    else:
                        # Fallback if piece doesn't have possible_moves method
                        attack_moves = []
                if new_position in attack_moves:
                    in_check = True
                    break
        # Restore the original board state
        self.position = original_position
        if original_position in board.grid or original_position == new_position:
            board.grid[original_position] = self
        if original_piece_at_new_position:
            board.grid[new_position] = original_piece_at_new_position
        elif new_position in board.grid and new_position != original_position:
            del board.grid[new_position]
        return in_check



    ############# CHECK BASED ON CAN CAPTURE MOVES ##############

    def is_check(self, board):
        """
        Determines if the King is currently in check.
        :param board: The current board state
        :return: True if the King is in check, False otherwise
        """
        return self.will_be_in_check(self.position, board)

    def is_checkmate(self, board):
        """
        Determines if the King is in checkmate.
        - King is in check
        - No legal moves available
        :param board: The current board state
        :return: True if the King is in checkmate, False otherwise
        """
        if not self.is_check(board):
            return False  # Not in check, so not checkmate

        # If the King has no legal moves left, it's checkmate
        return len(self.possible_moves(board)) == 0