import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
NAVY_BLUE = (0, 31, 63)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)

# Custom font
font = pygame.font.SysFont("Helvetica", 24)

# Checkbox class
class Checkbox:
    def __init__(self, text, x, y):
        self.text = text
        self.rect = pygame.Rect(x, y, 20, 20)
        self.checked = False

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect, 2)
        if self.checked:
            pygame.draw.line(surface, WHITE, self.rect.topleft, self.rect.bottomright)
            pygame.draw.line(surface, WHITE, self.rect.bottomleft, self.rect.topright)
        text_surface = font.render(self.text, True, WHITE)
        surface.blit(text_surface, (self.rect.right + 10, self.rect.centery - text_surface.get_height() / 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked

# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Checkbox UI")
    clock = pygame.time.Clock()

    checkboxes = [
        Checkbox("Checkbox 1", 150, 150),
        Checkbox("Checkbox 2", 350, 150),
        Checkbox("Checkbox 3", 550, 150),
        Checkbox("Checkbox 4", 150, 300),
        Checkbox("Checkbox 5", 350, 300),
        Checkbox("Checkbox 6", 550, 300)
    ]

    # Column titles
    column_titles = ["Column 1", "Column 2", "Column 3"]
    title_x_positions = [170, 370, 570]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for checkbox in checkboxes:
                checkbox.handle_event(event)

        # Fill the background
        screen.fill(NAVY_BLUE)

        # Draw column titles
        for i, title in enumerate(column_titles):
            title_surface = font.render(title, True, WHITE)
            screen.blit(title_surface, (title_x_positions[i], 100))

        # Draw checkboxes
        for checkbox in checkboxes:
            checkbox.draw(screen)

        # Draw continue button
        pygame.draw.rect(screen, LIGHT_GRAY, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT - 80, 150, 50))
        continue_text = font.render("Continue", True, NAVY_BLUE)
        screen.blit(continue_text, (SCREEN_WIDTH // 2 - continue_text.get_width() // 2, SCREEN_HEIGHT - 70))

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
