import sys;
import pygame;

def check_keydown_events(event, ship):
    # обработка нажатия клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True;

def check_keyup_events(event, ship):
    # обработка отпускания клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False;

def check_events(ship):
    # обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event , ship); 

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship);

def update_screen(ai_settigs, screen, ship):
    # обновляет изображение на экране и отображает новый экран
    screen.fill(ai_settigs.bg_color);
    ship.blitme();

    pygame.display.flip();
