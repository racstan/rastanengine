# games/flappy.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.core import GameEngine
from engine.components import TransformComponent, PhysicsComponent, ShapeComponent, ColliderComponent
import pygame
import random

class FlappyBirdGame(GameEngine):
    def __init__(self):
        super().__init__()
        self.settings.title = "Flappy Bird Clone"
        self.settings.background_color = (135, 206, 235)  # Sky blue

        # Game variables
        self.gravity = 500  # Pixels per second squared
        self.bird_start_x = 100
        self.pipe_gap = 150
        self.pipe_width = 80
        self.pipe_velocity = -200  # Pixels per second
        self.pipe_spawn_timer = 0
        self.pipe_spawn_interval = 1.5  # Seconds
        self.score = 0
        self.high_score = 0
        self.game_active = True

        # Entity groups
        self.pipes = []
        self.all_entities = self.entity_manager.entities

    def initialize(self):
        self.load_resources()
        self.create_player()

    def load_resources(self):
        # Since we're not using external assets, no resources to load
        pass

    def create_player(self):
        # Create the bird entity
        self.player = self.entity_manager.create_entity()
        self.player.add_component(TransformComponent(position=(self.bird_start_x, self.settings.screen_height / 2)))
        self.player.add_component(PhysicsComponent())
        self.player.add_component(ShapeComponent('circle', (255, 0, 0), 15))  # Red circle with radius 15
        self.player.add_component(ColliderComponent(pygame.Rect(0, 0, 30, 30)))  # Collider size matches the circle diameter

    def handle_events(self):
        super().handle_events()
        if self.input_system.keys_pressed[pygame.K_SPACE]:
            if self.game_active:
                # Make the bird "jump"
                physics = self.player.get_component('PhysicsComponent')
                physics.velocity.y = -300  # Upward velocity
            else:
                # Restart the game
                self.reset_game()

    def update(self, dt):
        if self.game_active:
            super().update(dt)
            self.apply_gravity(dt)
            self.spawn_pipes(dt)
            self.move_pipes(dt)
            self.check_collisions()
            self.update_score(dt)
        else:
            pass  # Game over state

    def apply_gravity(self, dt):
        physics = self.player.get_component('PhysicsComponent')
        physics.velocity.y += self.gravity * dt

    def spawn_pipes(self, dt):
        self.pipe_spawn_timer += dt
        if self.pipe_spawn_timer >= self.pipe_spawn_interval:
            self.pipe_spawn_timer = 0
            self.create_pipe_pair()

    def create_pipe_pair(self):
        gap_y = random.randint(100, self.settings.screen_height - 100)
        top_pipe_height = gap_y - self.pipe_gap / 2
        bottom_pipe_y = gap_y + self.pipe_gap / 2

        # Top pipe
        top_pipe = self.entity_manager.create_entity()
        top_pipe.add_component(TransformComponent(position=(self.settings.screen_width, 0)))
        top_pipe.add_component(PhysicsComponent())
        top_pipe.add_component(ShapeComponent('rect', (0, 200, 0), (self.pipe_width, top_pipe_height)))
        top_pipe.add_component(ColliderComponent(pygame.Rect(0, 0, self.pipe_width, top_pipe_height)))
        self.pipes.append(top_pipe)

        # Bottom pipe
        bottom_pipe_height = self.settings.screen_height - bottom_pipe_y
        bottom_pipe = self.entity_manager.create_entity()
        bottom_pipe.add_component(TransformComponent(position=(self.settings.screen_width, bottom_pipe_y)))
        bottom_pipe.add_component(PhysicsComponent())
        bottom_pipe.add_component(ShapeComponent('rect', (0, 200, 0), (self.pipe_width, bottom_pipe_height)))
        bottom_pipe.add_component(ColliderComponent(pygame.Rect(0, 0, self.pipe_width, bottom_pipe_height)))
        self.pipes.append(bottom_pipe)

    def move_pipes(self, dt):
        for pipe in self.pipes:
            physics = pipe.get_component('PhysicsComponent')
            transform = pipe.get_component('TransformComponent')
            physics.velocity.x = self.pipe_velocity
            transform.position.x += physics.velocity.x * dt

        # Remove pipes that are off-screen
        self.pipes = [pipe for pipe in self.pipes if pipe.get_component('TransformComponent').position.x + self.pipe_width > 0]

    def check_collisions(self):
        # Check collision with pipes
        player_collider = self.player.get_component('ColliderComponent')
        player_transform = self.player.get_component('TransformComponent')

        # Update player's collider position
        player_collider.rect.center = (player_transform.position.x, player_transform.position.y)

        for pipe in self.pipes:
            pipe_collider = pipe.get_component('ColliderComponent')
            pipe_transform = pipe.get_component('TransformComponent')
            pipe_shape = pipe.get_component('ShapeComponent')

            # Update pipe's collider position
            pipe_collider.rect.topleft = (pipe_transform.position.x, pipe_transform.position.y)
            pipe_collider.rect.size = pipe_shape.size

            if player_collider.rect.colliderect(pipe_collider.rect):
                self.game_active = False

        # Check collision with top and bottom of the screen
        if player_transform.position.y - 15 <= 0 or player_transform.position.y + 15 >= self.settings.screen_height:
            self.game_active = False

    def update_score(self, dt):
        self.score += dt

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score

        # Reset variables
        self.score = 0
        self.game_active = True
        self.pipe_spawn_timer = 0

        # Reset player position and velocity
        player_transform = self.player.get_component('TransformComponent')
        player_physics = self.player.get_component('PhysicsComponent')
        player_transform.position = pygame.math.Vector2(self.bird_start_x, self.settings.screen_height / 2)
        player_physics.velocity = pygame.math.Vector2(0, 0)

        # Remove all pipes
        for pipe in self.pipes:
            self.entity_manager.remove_entity(pipe)
        self.pipes.clear()

    def render(self):
        self.render_system.settings = self.settings  # Ensure settings are updated
        super().render()

        # Display score
        font = pygame.font.SysFont(None, 40)
        score_surface = font.render(f'Score: {int(self.score)}', True, (0, 0, 0))
        self.screen.blit(score_surface, (10, 10))

        if not self.game_active:
            # Game over text
            game_over_surface = font.render('Game Over!', True, (0, 0, 0))
            restart_surface = font.render('Press SPACE to restart', True, (0, 0, 0))
            high_score_surface = font.render(f'High Score: {int(self.high_score)}', True, (0, 0, 0))

            self.screen.blit(game_over_surface, (self.settings.screen_width // 2 - game_over_surface.get_width() // 2, self.settings.screen_height // 2 - 60))
            self.screen.blit(high_score_surface, (self.settings.screen_width // 2 - high_score_surface.get_width() // 2, self.settings.screen_height // 2 - 20))
            self.screen.blit(restart_surface, (self.settings.screen_width // 2 - restart_surface.get_width() // 2, self.settings.screen_height // 2 + 20))

if __name__ == "__main__":
    game = FlappyBirdGame()
    game.initialize()
    game.run()
