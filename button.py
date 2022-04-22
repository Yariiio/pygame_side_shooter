import pygame.font

class Button:
    def __init__(self, game, text):
        self.window = game.window
        self.window_rect = self.window.get_rect()
        self.width, self.height = 258, 50
        self.button__color = (255, 0, 0)
        self.text_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.window_rect.center
        self._prep_text(text)

    def _prep_text(self, text):
        self.text_img = self.font.render(text, True, self.text_color, self.button__color)
        self.text_img_rect = self.text_img.get_rect()
        self.text_img_rect.center = self.rect.center

    def draw_button(self):
        self.window.fill(self.button__color, self.rect)    
        self.window.blit(self.text_img, self.text_img_rect)    