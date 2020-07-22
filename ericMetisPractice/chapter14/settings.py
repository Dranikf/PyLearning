class Settings():
    def __init__(self):
        # параметры экрана
        self.scr_width = 800;
        self.scr_height = 600;
        self.bg_color = (10, 10, 10);

        # параметры корабля
        self.sheep_speed = 1.5;

        # параметры инопланетянина
        self.alien_speed = 1;
        self.alien_dir = 1;
       
        self.bul_speed = 3;
        self.max_shoots = 100;

        self.game_active = False;
