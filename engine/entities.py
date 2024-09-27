# engine/entities.py
import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.original_image = image
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

class Player(Entity):
    def __init__(self, image, position):
        super().__init__(image, position)
        self.speed = 200  # Pixels per second

    def handle_input(self, keys_pressed):
        self.velocity.x = 0
        self.velocity.y = 0
        if keys_pressed[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        if keys_pressed[pygame.K_UP]:
            self.velocity.y = -self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.velocity.y = self.speed

class Enemy(Entity):
    def __init__(self, image, position):
        super().__init__(image, position)
        self.speed = 100
        # Additional enemy-specific attributes
