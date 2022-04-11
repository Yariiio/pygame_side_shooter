import pygame, sys
from settings import Settings
from player import Player

class Game:
    def __init__(self):
        self.FPS = 240
        self.clock = pygame.time.Clock()
        pygame.init()
        self.settings = Settings()
        self.window = pygame.display.set_mode((self.settings.window_w, self.settings.window_h))
        self.player = Player(self)
        pygame.display.set_caption("side_shooter")

    def run(self):
        while True:
            self._check_events()
            self.player.update()
            self._update_window()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydowns(event)             
            elif event.type == pygame.KEYUP:
                self._check_keyups(event)


    def _check_keydowns(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
             self.player.moving_down = True  
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyups(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False          

    
    def _update_window(self):
        self.window.fill(self.settings.bg_color)
        self.player.blit()
        pygame.display.flip()
        self.clock.tick(self.FPS)

if __name__ == "__main__":
    new_game = Game()
    new_game.run()