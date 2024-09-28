import pygame

class AudioSystem:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

    def load_sound(self, name, filepath):
        self.sounds[name] = pygame.mixer.Sound(filepath)
