class Settings():
    """ класс для хранения настроек """

    def __init__(self):
        """ инициализируем настройки игры """
        #параметры экрана
        self.screen_width = 1200;
        self.screen_height = 800;
        self.bg_color = (10 , 10 , 10);

        # перемещение пришельцев
        self.fleet_drop_speed = 10; # велицина смещения пришельцев вниз

        # настройки пули
        self.bullet_width = 3;
        self.bullet_height = 15;
        self.bullet_color = (200 ,250  ,200);
        self.bullets_allowed = 3;
        self.super_bullet = False;

        # настройки генерации звезд 
        self.stars_count = 100;
        self.max_stars_size = 50;
        self.min_stars_size = 10;

        self.ship_limit = 3; # количество доступных жизней

        # темп ускорения игры
        self.speedup_scale = 1.1;

        # темп роста стоимоти пришельцев 
        self.score_scale = 1.5;

        self.initialize_dynamic_settings();

    def initialize_dynamic_settings(self):
        """инициализирует настройки, изменяющиеся в ходе игры """
        self.ship_speed_factor = 2.5;# корабль
        self.bullet_speed_factor = 3;
        self.alien_speed_factor = 2; # пришельцы

        self.fleet_direction = 1; # направление движения флота
        self.alien_points = 50;

    def increase_speed(self):
        """увеличивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale;
        self.bullet_speed_factor *= self.speedup_scale;
        self.alien_speed_factor *= self.speedup_scale;

        self.alien_points = int(self.alien_points * self.score_scale);
