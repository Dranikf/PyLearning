import pygame;
from settings import Settings;
from ship import Ship;
from star import Star;
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

    while True:
        gf.check_events(ai_settings, screen, ship, bullets);
        ship.update();
        
        gf.update_bullets(bullets, aliens);
        gf.update_aliens(aliens, ai_settings);
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stars); 

run_game();
