import pygame

class TransformComponent:
    def __init__(self, position=(0, 0)):
        self.position = pygame.math.Vector2(position)
        self.rotation = 0.0
        self.scale = pygame.math.Vector2(1, 1)

    def update(self, dt):
        pass  # Typically updated by physics or movement components

class SpriteComponent:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def update(self, dt):
        pass

class PhysicsComponent:
    def __init__(self):
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)

    def update(self, dt):
        self.velocity += self.acceleration * dt
