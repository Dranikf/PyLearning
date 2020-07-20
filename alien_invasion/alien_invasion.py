import pygame;
from settings import Settings;
from ship import Ship;
from star import Star;
from game_stats import GameStats;
import game_functions as gf;
from pygame.sprite import Group;


def run_game():
    # инициализирует игру и создаёт объект экрана.
    pygame.init();
    ai_settings = Settings();
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height));
    pygame.display.set_caption('Alien Invasion');

    # создание корабля
    ship = Ship(ai_settings, screen); 

    # создание групы пуль
    bullets = Group();
    # создание флота пришельцев
    aliens = Group();
    gf.create_fleet(ai_settings, screen, ship, aliens);

    # создание звезд
    stars = Group();
    gf.create_stars(ai_settings, screen, stars);

    # таймер отсчитывающий игровое время
    clock = pygame.time.Clock();
    
    # создание экземпляра для хранение статистики
    stats = GameStats(ai_settings); 

    while True:
        clock.tick();
        timerVal = clock.get_time();
        gf.check_events(ai_settings, screen, ship, bullets);
        if stats.game_active:
            ship.update(timerVal);
            
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens, timerVal);
            gf.update_aliens(aliens, stats, screen, ai_settings, timerVal, ship, bullets);
            gf.update_screen(ai_settings, screen, ship, bullets, aliens, stars); 

run_game();
