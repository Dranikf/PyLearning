class GameStats():
    """Отслеживание статистии для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """инициализирует статитику."""
        self.ai_settings = ai_settings;
        self.game_active = False;
        self.reset_stat();


    def reset_stat(self):
        """инициализурует статистику изменяющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit;