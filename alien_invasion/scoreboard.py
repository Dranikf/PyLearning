import pygame.font;

class Scoredoard():
    """класс для вывода игровой информации."""
    def __init__(self, ai_settings, screen, stats):
        """инициализирует атрибуты игровой информации"""
        self.screen = screen;
        self.ai_settings = ai_settings;
        self.screen_rect = screen.get_rect();
        self.stats = stats;

        # настройки шрифта для вывода счета
        self.text_color = (200, 200 , 200);
        self.font = pygame.font.SysFont(None, 48);
        self.prep_score();
        self.prep_high_score();


    def prep_score(self):
        """преобразует текущий счет в графическое изображение."""

        rounded_score = int(round(self.stats.score, -1));
        score_str = "{:,}".format(rounded_score);

        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color);

        self.score_rect = self.score_image.get_rect();
        self.score_rect.right = self.screen_rect.right - 20;
        self.score_rect.top = 20;

    
    def show_score(self):
        """выводит счет на экран"""
        self.screen.blit(self.score_image, self.score_rect);
        self.screen.blit(self.high_score_image, self.high_score_rect);


    def prep_high_score(self):
        """преобразует рекордный счет в графическое изображение"""
        high_score = int(round(self.stats.high_score, -1));
        high_score_str = "{:,}".format(high_score);
        self.high_score_image = self.font.render(high_score_str, 
                True, self.text_color, self.ai_settings.bg_color);

        #  рекорд выравнивается по центру верхней стороны.
        self.high_score_rect = self.high_score_image.get_rect();
        self.high_score_rect.centerx = self.screen_rect.centerx;
        self.high_score_rect.top = self.score_rect.top;


    def prep_level(self): 
        """преобразует уровень в графическое изображение."""
        self.level_image = self.font.render(str(self.stats.level), True
                                self.text_color, self.ai_settings.bg_color);

        # уровень выводиться под текущим счетом.
        self.level_rect = self.level_image.get_rect();
        self.level_rect.right = self.score_rect.right;
        self.level_rect.top = sefl.score_rect.bottom + 10;
