import pygame

class GraphicsEngine:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (255, 255, 255)  # White background

    def clear_screen(self):
        self.screen.fill(self.background_color)

    def update_display(self):
        pygame.display.flip()
