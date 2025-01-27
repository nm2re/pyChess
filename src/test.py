import pygame

class Constants:
    ROWS = 8
    COLS = 8
    SQUARE_SIZE = 50  # Size of each square

# Initialize Pygame
pygame.init()

# Constants
WIDTH = Constants.COLS * Constants.SQUARE_SIZE
HEIGHT = Constants.ROWS * Constants.SQUARE_SIZE
colors = [(255, 255, 255), (0, 0, 0)]  # Alternating white and black squares

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard with Row and Column Numbers")

# Set up font
font = pygame.font.Font(None, 24)  # Default font, size 24

# Draw the board
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw squares and add text
    for row in range(Constants.ROWS):
        for col in range(Constants.COLS):
            # Draw the square
            rect = pygame.Rect(
                Constants.SQUARE_SIZE * col,
                Constants.SQUARE_SIZE * row,
                Constants.SQUARE_SIZE,
                Constants.SQUARE_SIZE
            )
            pygame.draw.rect(screen, colors[(row + col) % 2], rect)

            # Render the row and col text
            text = font.render(f"{row},{col}", True, (255, 0, 0))  # Red text
            text_rect = text.get_rect(center=rect.center)  # Center text in the square
            screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
