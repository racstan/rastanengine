import pygame

class InputHandler:
    def __init__(self):
        self.quit = False
        self.keys_pressed = {}

    def handle_events(self):
        self.keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
