import pygame
from pygame.sprite import Sprite;

class Bullet(Sprite): # наследуемся от sprite (непонятно зачем)
    # класс для управления пулями выпущенными кораблем
    def __init__(self, ai_settings, screen , ship):
        super(Bullet, self).__init__();

        self.screen = screen;

        # пуля старутет там, где на момент ее создания находиться корабль
        self.rect = pygame.Rect(0 , 0 , ai_settings.bullet_width , ai_settings.bullet_height);

        self.rect.centerx = ship.rect.centerx;
        self.rect.top = ship.rect.top;

        # сохраняем позицию пули в вещественном формате
        self.y = float(self.rect.y);

        self.color = ai_settings.bullet_color;
        self.speed_factor = ai_settings.bullet_speed_factor;

        self.ai_settings = ai_settings;

    def update(self, timerVal):
        # обновление положения пули (перемещение вверx)
        self.y -= self.speed_factor;
        self.rect.y = self.y;

    def draw_bullet(self):
        pygame.draw.rect(self.screen , self.color , self.rect);

