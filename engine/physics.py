import pygame

class PhysicsSystem:
    def __init__(self):
        self.gravity = pygame.math.Vector2(0, 9.8)

    def update(self, entities, dt):
        for entity in entities:
            physics = entity.get_component('PhysicsComponent')
            transform = entity.get_component('TransformComponent')
            if physics and transform:
                # Apply gravity
                physics.velocity += self.gravity * dt
                # Update position
                transform.position += physics.velocity * dt
                # Handle collisions (to be implemented)
