import pygame
from pygame.sprite import Sprite
from random import randint

class Enemy(Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.window = game.window
        self.window_rect = self.window.get_rect()
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.window_rect.right
        self.rect.y = randint(0, 800 - self.rect.height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        self.x -= self.settings.enemy_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def blit_enemy(self):
        self.window.blit(self.image, self.rect)    
