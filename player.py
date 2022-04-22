import pygame

class Player:
    def __init__(self, game):
        self.window = game.window
        self.settings = game.settings
        self.window_rect = game.window_rect
        self.image = pygame.image.load("assets/rocket.png")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.window_rect.midleft
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)

    def blit(self):
        self.window.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.player_velocity
        if self.moving_down and self.rect.bottom < self.window_rect.bottom:
            self.y += self.settings.player_velocity  
            
        self.rect.y = self.y    

    def center_pos(self):
        self.rect.midleft = self.window_rect.midleft
        self.y = self.rect.y
            

           

