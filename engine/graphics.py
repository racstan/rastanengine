import pygame

class RenderSystem:
    def __init__(self, screen):
        self.screen = screen
        self.settings = None  # Will be set later

    def render(self, entities):
        self.screen.fill(self.settings.background_color)
        for entity in entities:
            sprite = entity.get_component('SpriteComponent')
            transform = entity.get_component('TransformComponent')
            if sprite and transform:
                sprite.rect.center = transform.position
                self.screen.blit(sprite.image, sprite.rect)
