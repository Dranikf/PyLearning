import pygame;
from settings import Settings;
from pygame.sprite import Sprite;

class Ship(Sprite):

    def __init__(self ,ai_settings , screen):

        super(Ship, self).__init__();
        # инициализирует корабль и задает его начальную позицию
        self.screen = screen;
        self.ai_settings = ai_settings;

        # загрузка изображения корабля
        self.image = pygame.image.load('images/ship.bmp');
        self.rect = self.image.get_rect();
        self.screen_rect = screen.get_rect();
        
        # каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx;
        self.rect.bottom = self.screen_rect.bottom;

        # сохранение вещественной координаты центра корабля
        self.center = float(self.rect.centerx);
        self.centery = float(self.rect.centery);

        # флаги указывающие на состояние движения корабля
        self.moving_right = False;
        self.moving_left = False;
        self.moving_up = False;
        self.moving_down = False;

    def update(self, timerVal):

        movValue = self.ai_settings.ship_speed_factor; 

        # если флаг активен перемещаем корабль
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += movValue;

        if self.moving_left and self.rect.left > 0:
            self.center -= movValue;

        if self.moving_up and self.rect.top > 0:
            self.centery -= movValue; 

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += movValue;

        #обновляем позицию корабля на основаниее self.center
        self.rect.centerx = self.center;
        self.rect.centery = self.centery;

    def blitme(self):
        self.screen.blit(self.image, self.rect);

    def center_ship(self):
        """размещает корабль в центре нижней стороны."""
        self.center = self.screen_rect.centerx;
