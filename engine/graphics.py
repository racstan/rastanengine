# engine/graphics.py
import pygame

class RenderSystem:
    def __init__(self, screen):
        self.screen = screen
        self.settings = None  # Will be set later

    def render(self, entities):
        self.screen.fill(self.settings.background_color)
        for entity in entities:
            transform = entity.get_component('TransformComponent')
            shape = entity.get_component('ShapeComponent')
            sprite = entity.get_component('SpriteComponent')

            if shape and transform:
                self.draw_shape(shape, transform)
            elif sprite and transform:
                sprite.rect.center = transform.position
                self.screen.blit(sprite.image, sprite.rect)

    def draw_shape(self, shape_component, transform_component):
        if shape_component.shape_type == 'circle':
            pygame.draw.circle(
                self.screen,
                shape_component.color,
                (int(transform_component.position.x), int(transform_component.position.y)),
                shape_component.size
            )
        elif shape_component.shape_type == 'rect':
            rect = pygame.Rect(
                int(transform_component.position.x),
                int(transform_component.position.y),
                shape_component.size[0],
                shape_component.size[1]
            )
            pygame.draw.rect(self.screen, shape_component.color, rect)
