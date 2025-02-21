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