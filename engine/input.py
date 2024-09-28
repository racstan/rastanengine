import pygame

class InputSystem:
    def __init__(self):
        self.quit = False
        self.keys_pressed = {}
        self.mouse_buttons = {}
        self.mouse_position = (0, 0)

    def handle_events(self):
        self.keys_pressed = pygame.key.get_pressed()
        self.mouse_buttons = pygame.mouse.get_pressed()
        self.mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            # Handle other events like keydown, mouse clicks, etc.
