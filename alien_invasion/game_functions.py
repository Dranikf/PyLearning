import sys;
import pygame;
from bullet import Bullet;

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # обработка нажатия клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True;
    elif event.key == pygame.K_UP:
        ship.moving_up = True;
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True;
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets);
            
def fire_bullet(ai_settings, screen , ship , bullets):
    """выпускает новую пулю, если максимум еще не достигнут """
    # создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship);
        bullets.add(new_bullet);

    

def check_keyup_events(event, ai_settings, screen, ship, bullets):
    # обработка отпускания клавиш
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False;
    elif event.key == pygame.K_UP:
        ship.moving_up = False;
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False;
 

def check_events(ai_settings, screen, ship, bullets):
    # обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets); 

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets);

def update_screen(ai_settigs, screen, ship, bullets):
    # обновляет изображение на экране и отображает новый экран
    screen.fill(ai_settigs.bg_color);
    
    for bullet in bullets.sprites():
        bullet.draw_bullet();

    ship.blitme();

    pygame.display.flip();

def update_bullets(bullets):
    """обновление позиций пуль и уничтожает старые пули."""
    # обновление позиций пуль
    bullets.update();

    # удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet);
    print(len(bullets));


