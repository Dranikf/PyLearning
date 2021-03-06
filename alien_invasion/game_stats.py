class GameStats():
    """Отслеживание статистии для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """инициализирует статитику."""
        self.ai_settings = ai_settings;
        self.game_active = False;
        try:
            f_obj = open('hight_score', 'rb');
            self.high_score = int.from_bytes(f_obj.read(4), 'little');
            f_obj.close();
        except FileNotFoundError:
            self.high_score = 0;
        self.reset_stat();


    def reset_stat(self):
        """инициализурует статистику изменяющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit;
        self.level = 1;
        self.score = 0;
