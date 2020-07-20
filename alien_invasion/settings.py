class Settings():
    """ класс для хранения настроек """

    def __init__(self):
        """ инициализируем настройки игры """
        #параметры экрана
        self.screen_width = 1200;
        self.screen_height = 800;
        self.bg_color = (10 , 10 , 10);

        #speed factors 
        self.ship_speed_factor = 2.5;# корабль
        self.alien_speed_factor = 2; # пришельцы

        # перемещение пришельцев
        self.fleet_drop_speed = 10; # велицина смещения пришельцев вниз
        self.fleet_direction = 1; # направление движения флота

        # настройки пули
        self.bullet_speed_factor = 3;
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
