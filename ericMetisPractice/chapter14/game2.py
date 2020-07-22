import pygame;
from game_controller import GameController;
from settings import Settings;

def run_game():

    ai_settings = Settings();

    pygame.init();
    screen = pygame.display.set_mode((ai_settings.scr_width, ai_settings.scr_height));
    pygame.display.set_caption("hello");

    gc = GameController(ai_settings, screen);

    while True:
        
        if ai_settings.game_active:
            gc.check_events();
            gc.frame();
        else: 
            gc.menuFrame();
        gc.update_screen();

run_game();
