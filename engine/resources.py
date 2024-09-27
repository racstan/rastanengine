import pygame
import os

class ResourceManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}

    def load_resources(self):
        # Load images
        self.images['zeus'] = pygame.image.load(os.path.join('assets', 'images', 'zeus.png')).convert_alpha()
        self.images['titan'] = pygame.image.load(os.path.join('assets', 'images', 'titan.png')).convert_alpha()
        # Load sounds
        # self.sounds['attack'] = pygame.mixer.Sound(os.path.join('assets', 'sounds', 'attack.wav'))
