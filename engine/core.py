import pygame
from .input import InputHandler
from .graphics import GraphicsEngine
from .resources import ResourceManager

class GameEngine:
    def __init__(self, title, width, height, fps=60):
        pygame.init()
        self.title = title
        self.width = width
        self.height = height
        self.fps = fps
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.is_running = False

        # Initialize subsystems
        self.input_handler = InputHandler()
        self.graphics_engine = GraphicsEngine(self.screen)
        self.resource_manager = ResourceManager()
        self.entities = pygame.sprite.Group()

    def load_resources(self):
        # Load images, sounds, etc.
        self.resource_manager.load_resources()

    def add_entity(self, entity):
        self.entities.add(entity)

    def run(self):
        self.is_running = True
        while self.is_running:
            dt = self.clock.tick(self.fps) / 1000  # Delta time in seconds
            self.handle_events()
            self.update(dt)
            self.render()
        pygame.quit()

    def handle_events(self):
        self.input_handler.handle_events()
        if self.input_handler.quit:
            self.is_running = False

    def update(self, dt):
        self.entities.update(dt)

    def render(self):
        self.graphics_engine.clear_screen()
        self.entities.draw(self.screen)
        self.graphics_engine.update_display()
