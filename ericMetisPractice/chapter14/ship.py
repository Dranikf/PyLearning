import pygame;
from pygame.transform import rotate;

class Ship():
    def __init__(self, ai_settings, screen):

        self.ai_settings = ai_settings;
        self.screen = screen;

        self.image = rotate(pygame.image.load('images/ship.bmp'), -90);
        self.rect = self.image.get_rect();
        self.screen_rect = self.screen.get_rect();

        self.set_default_pos();

        self.moving_up = False;
        self.moving_down = False;
        
        
    def blitme(self):
        self.screen.blit(self.image, self.rect);


    def set_default_pos(self):
        self.rect.left = self.screen_rect.left;
        self.rect.centery= self.screen_rect.centery;

        self.centery = float(self.rect.centery);


    def update(self):

        if self.moving_up and self.rect.top != self.screen_rect.top:
            self.centery -= self.ai_settings.sheep_speed;
        if self.moving_down and self.rect.bottom != self.screen_rect.bottom:
            self.centery += self.ai_settings.sheep_speed;

        self.rect.centery = self.centery;
