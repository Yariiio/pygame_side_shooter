import pygame, sys
from settings import Settings
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = pygame.display.set_mode((self.settings.window_w, self.settings.window_h))
        self.player = Player(self)
        pygame.display.set_caption("side_shooter")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.window.fill(self.settings.bg_color)
            self.player.blit()

            pygame.display.flip()

if __name__ == "__main__":
    new_game = Game()
    new_game.run()