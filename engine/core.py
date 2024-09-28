# engine/core.py
import pygame
from .ecs import EntityManager
from .input import InputSystem
from .graphics import RenderSystem
from .physics import PhysicsSystem
from .audio import AudioSystem
from .resources import ResourceManager
from .settings import Settings

class GameEngine:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.title)
        self.clock = pygame.time.Clock()
        self.is_running = False

        # Initialize subsystems
        self.resource_manager = ResourceManager()
        self.entity_manager = EntityManager()
        self.input_system = InputSystem()
        self.physics_system = PhysicsSystem()
        self.render_system = RenderSystem(self.screen)
        self.audio_system = AudioSystem()

    def load_resources(self):
        self.resource_manager.load_resources()

    def initialize(self):
        self.load_resources()
        # Setup initial game state, load levels, entities, etc.
        pass

    def run(self):
        self.is_running = True
        while self.is_running:
            dt = self.clock.tick(self.settings.fps) / 1000  # Delta time in seconds
            self.handle_events()
            self.update(dt)
            self.render()
        self.cleanup()

    def handle_events(self):
        self.input_system.handle_events()
        if self.input_system.quit:
            self.is_running = False

    def update(self, dt):
        self.entity_manager.update(dt)
        self.physics_system.update(self.entity_manager.entities, dt)
        # Update other systems as needed

    def render(self):
        self.render_system.render(self.entity_manager.entities)
        pygame.display.flip()

    def cleanup(self):
        pygame.quit()
