import pygame;

class Alien():
    def __init__(self, ai_settings, screen):

        self.ai_settings = ai_settings;

        self.image = pygame.image.load('images/alien.bmp');
        self.rect = self.image.get_rect();

        self.screen_rect = screen.get_rect();
        self.screen = screen;

        self.rect.right = self.screen_rect.right;
        self.rect.top = self.screen_rect.top;

        self.centery = float(self.rect.centery);

    def blitme(self): 
        self.screen.blit(self.image, self.rect);

    
    def update(self):
        self.centery += self.ai_settings.alien_speed*self.ai_settings.alien_dir; 
        self.rect.centery = self.centery;

        if (self.rect.top == self.screen_rect.top  or 
                self.rect.bottom == self.screen_rect.bottom):
            self.ai_settings.alien_dir *= -1;
