import pygame

class Player:
    def __init__(self, game):
        self.window = game.window
        self.window_rect = game.window.get_rect()
        self.image = pygame.image.load("assets/rocket.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.window_rect.midleft

    def blit(self):
        self.window.blit(self.image, self.rect)
        print(self.rect)    
