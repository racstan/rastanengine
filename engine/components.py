# engine/components.py
import pygame

class Component:
    def update(self, dt):
        pass

class TransformComponent(Component):
    def __init__(self, position=(0, 0)):
        self.position = pygame.math.Vector2(position)
        self.rotation = 0.0
        self.scale = pygame.math.Vector2(1, 1)

    def update(self, dt):
        pass

class PhysicsComponent(Component):
    def __init__(self):
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)

    def update(self, dt):
        self.velocity += self.acceleration * dt

class ColliderComponent(Component):
    def __init__(self, rect):
        self.rect = rect

    def update(self, dt):
        pass

class ShapeComponent(Component):
    def __init__(self, shape_type, color, size):
        self.shape_type = shape_type  # 'circle', 'rect', etc.
        self.color = color
        self.size = size  # For circle: radius; For rect: (width, height)

    def update(self, dt):
        pass

# If you had a SpriteComponent already, you can keep it for other games.
class SpriteComponent(Component):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def update(self, dt):
        pass
