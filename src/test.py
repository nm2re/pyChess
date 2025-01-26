import pygame

class GridWithCoordinates:
    def __init__(self, screen, rows, cols, square_size, colors):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.square_size = square_size
        self.colors = colors
        self.font = pygame.font.Font(None, 24)  # Default font, size 24

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Draw the square
                color = self.colors[(row + col) % 2]
                rect = (self.square_size * col, self.square_size * row, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, color, rect)

                # Write the coordinates inside the square
                coordinates = f"({row},{col})"
                text = self.font.render(coordinates, True, (0, 0, 0))  # Black text
                text_rect = text.get_rect(center=(self.square_size * col + self.square_size // 2,
                                                  self.square_size * row + self.square_size // 2))
                self.screen.blit(text, text_rect)

# Example usage
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Grid with Coordinates")
clock = pygame.time.Clock()

rows, cols = 8, 8
square_size = 50
colors = [(255, 255, 255), (100, 100, 100)]  # Light and dark squares

grid = GridWithCoordinates(screen, rows, cols, square_size, colors)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen with black
    grid.draw_grid()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
