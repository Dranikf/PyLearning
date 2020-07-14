import pygame;
from settings import Settings;
from ship import Ship;
import game_functions as gf;


def run_game():
    # инициализирует игру и создаёт объект экрана.
    pygame.init();
    ai_settigs = Settings();
    screen = pygame.display.set_mode((
        ai_settigs.screen_width, ai_settigs.screen_height));
    pygame.display.set_caption('Alien Invasion');

    # создание корабля
    ship = Ship(ai_settigs, screen); 

    while True:
        gf.check_events(ship);
        ship.update();
        gf.update_screen(ai_settigs, screen, ship); 

run_game();
