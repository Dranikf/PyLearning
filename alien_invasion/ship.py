import pygame;
from settings import Settings;

class Ship():

    def __init__(self ,ai_settings , screen):
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

    def update(self):
        # если флаг активен перемещаем корабль
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor;

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor;

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor; 

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor;

        #обновляем позицию корабля на основаниее self.center
        self.rect.centerx = self.center;
        self.rect.centery = self.centery;

    def blitme(self):
        self.screen.blit(self.image, self.rect);
