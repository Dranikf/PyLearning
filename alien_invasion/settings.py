class Settings():
    #""" класс для хранения настроек """

    def __init__(self):
        #""" инициализируем настройки игры """
        #параметры экрана
        self.screen_width = 1200;
        self.screen_height = 800;
        self.bg_color = (150 , 150 , 255);

        # скорость перемещения корабля
        self.ship_speed_factor = 1.5;

        # настройки пули
        self.bullet_speed_factor = 1;
        self.bullet_width = 3;
        self.bullet_height = 15;
        self.bullet_color = (60 , 60 , 60);
        self.bullets_allowed = 3;
