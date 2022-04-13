import pygame
from pygame.sprite import Sprite
from random import randint

class Enemy:
    def __init__(self, game):
        self.window = game.window
        self.window_rect = self.window.get_rect()
        self.settings = game.settings
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.starting_point_x = (self.settings.window_w + self.rect.width)
        self.x = float(self.starting_point_x)
        self.y = randint(0, (self.settings.window_h - self.rect.height))

    def update(self):
        self.x -= self.settings.enemy_velocity
        self.rect.x = self.x

    def blit(self):
        
        self.window.blit(self.image, (self.rect.x, self.y))