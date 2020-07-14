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
