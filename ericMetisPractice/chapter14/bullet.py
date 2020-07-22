import pygame;
from pygame.sprite import Sprite;

class Bullet(Sprite):
    
    def __init__(self, st_pos_rect, ai_settings, screen):

        self.ai_settings = ai_settings;

        super(Bullet, self).__init__();
        self.active = False;   

        self.rect = pygame.Rect(0, 0, 15, 3);
        self.rect.right = st_pos_rect.right;
        self.rect.centery = st_pos_rect.centery;
        
        self.centerx = float(self.rect.centerx);
        self.screen = screen;

        self.color = (15, 150, 15); 

    def update(self):
        self.centerx += self.ai_settings.bul_speed;
        self.rect.centerx = self.centerx;


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect);
