import pygame;
from pygame.sprite import Sprite;
from pygame.rect import Rect;

class Star(Sprite):
    def __init__(self, size, texture, screen, position): 
        """конструктор - просто инициализирует"""
        super(Star , self).__init__();
        self.screen = screen;

        #загружаем изобрвжение звезды
        self.image = pygame.image.load(texture);

        # размеры и позиция
        self.rect = Rect(0, 0, 10, 10);
        self.rect.centerx = position[0];
        self.rect.centery = position[1];
        self.image = pygame.transform.scale(self.image, (size, size));

    def blitme(self):
        self.screen.blit(self.image, self.rect); 
