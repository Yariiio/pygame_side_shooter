from time import sleep
import pygame, sys
from settings import Settings
from player import Player
from bullet import Bullet
from enemy import Enemy
from gamestats import GameStats
from scoreboard import ScoreBoard
from button import Button

class Game:
    def __init__(self):
        self.FPS = 240
        self.clock = pygame.time.Clock()
        pygame.init()
        self.settings = Settings()
        self.window = pygame.display.set_mode((self.settings.window_w, self.settings.window_h))
        self.window_rect = self.window.get_rect()
        self.stats = GameStats(self)
        self.scoreboard = ScoreBoard(self)
        self.window = pygame.display.set_mode((self.settings.window_w, self.settings.window_h))
        self.player = Player(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.play_button = Button(self, "Press 'p' To Play")
        pygame.display.set_caption("side_shooter")
 
    def run(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.player.update()
                self._bullets_update()
                self._handle_enemies()
            self._update_window()
      
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydowns(event)             
            elif event.type == pygame.KEYUP:
                self._check_keyups(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() 
                self._check_play_button(mouse_pos)   


    def _check_keydowns(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = True
        elif event.key == pygame.K_DOWN:
             self.player.moving_down = True  
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
             self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()     

    def _check_keyups(self, event):
        if event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False   

    def _fire_bullet(self):
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)       

    def _bullets_update(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.x > self.window_rect.right:
                self.bullets.remove(bullet)  

        collide = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)        

    def _handle_enemies(self):
        new_enemy = Enemy(self)
        if len(self.enemies) < 1:
            self.enemies.add(new_enemy)
        self.enemies.update()

        for enemy in self.enemies:
            if enemy.x < 0 - enemy.rect.width:
                self.enemies.remove(enemy)
                self.enemies.add(new_enemy) 

        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self._player_hit()

    def _player_hit(self):
        if self.settings.life_limit > 0:
            self.settings.life_limit -= 1
            self.enemies.empty()
            self.bullets.empty()
            self.player.center_pos()
            print(self.settings.life_limit)
            sleep(1.0)
        else:
            pygame.mouse.set_visible(True)
            self.stats.game_active = False   

    def _start_game(self):
        if not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True   
            self.enemies.empty()
            self.bullets.empty()
            self.player.center_pos()        

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True   
            self.enemies.empty()
            self.bullets.empty()
            self.player.center_pos()    
            pygame.mouse.set_visible(False)
        print(button_clicked)     
                
    def _update_window(self):
        self.window.fill(self.settings.bg_color)
        self.player.blit()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet() 
        for enemy in self.enemies.sprites():
            enemy.blit_enemy()   
        self.scoreboard.show_score()    
        if not self.stats.game_active:
            self.play_button.draw_button()        
        pygame.display.flip()
        self.clock.tick(self.FPS)

if __name__ == "__main__":
    new_game = Game()
    new_game.run()