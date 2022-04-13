import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.window = game.window
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = game.player.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_velocity
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.window, self.color, self.rect)    

