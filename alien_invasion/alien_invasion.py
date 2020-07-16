import pygame;
from settings import Settings;
from ship import Ship;
import game_functions as gf;
from pygame.sprite import Group;


def run_game():
    # инициализирует игру и создаёт объект экрана.
    pygame.init();
    ai_settigs = Settings();
    screen = pygame.display.set_mode((
        ai_settigs.screen_width, ai_settigs.screen_height));
    pygame.display.set_caption('Alien Invasion');

    # создание корабля
    ship = Ship(ai_settigs, screen); 

    # создание групы пуль
    bullets = Group();

    while True:
        gf.check_events(ai_settigs, screen, ship, bullets);
        ship.update();
        
        gf.update_bullets(bullets);
        gf.update_screen(ai_settigs, screen, ship, bullets); 

run_game();
