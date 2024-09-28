# engine/resources.py
import pygame
import os

class ResourceManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.base_path = os.path.join(os.getcwd(), 'assets')

    def load_resources(self):
        self.load_images()
        self.load_sounds()

    def load_images(self):
        images_path = os.path.join(self.base_path, 'images')
        for filename in os.listdir(images_path):
            if filename.endswith('.png'):
                path = os.path.join(images_path, filename)
                image = pygame.image.load(path).convert_alpha()
                self.images[filename[:-4]] = image  # Remove .png extension

    def load_sounds(self):
        sounds_path = os.path.join(self.base_path, 'sounds')
        for filename in os.listdir(sounds_path):
            if filename.endswith('.wav'):
                path = os.path.join(sounds_path, filename)
                sound = pygame.mixer.Sound(path)
                self.sounds[filename[:-4]] = sound
