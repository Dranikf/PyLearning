import sys;
import pygame;
from bullet import Bullet;
from alien import Alien;
from star import Star;
from random import randint;
from time import sleep;

def save_leave(stats):
    """function save hight score, and calls sys.exit()"""
    file_obj = open("hight_score", 'wb');
    file_obj.write(stats.high_score.to_bytes(4, 'little'));
    file_obj.close();
    sys.exit();


def check_keydown_events(event, ai_settings, stats, screen, ship, bullets
                                , aliens, sb ):
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
    elif event.key == pygame.K_q:
        save_leave(stats);
    elif event.key == pygame.K_p:
        start_game(ai_settings, screen, ship, aliens, stats, bullets, sb);
            
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
 

def check_events(ai_settings, screen, stats, play_button, ship, 
                        bullets, aliens, sb):
    # обрабатывает нажатия клавиш и события мыши
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_leave();

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship,
                     bullets, aliens, sb); 

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets);

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos();
            check_play_button(ai_settings, screen, stats, play_button
                                , ship, aliens, bullets, mouse_x, mouse_y, sb);


def update_screen(ai_settigs, stats, sb, screen, ship, bullets, aliens, stars,
        play_button):
    # обновляет изображение на экране и отображает новый экран
    screen.fill(ai_settigs.bg_color);
   
    stars.draw(screen);

    for bullet in bullets.sprites():
        bullet.draw_bullet();

    ship.blitme();
    aliens.draw(screen);

    sb.show_score();

    # Кнопка Play отображается только в том случае, если игра неактивна.
    if not stats.game_active:
        play_button.draw_button();

    pygame.display.flip();


def update_bullets(ai_settings, stats, sb, screen, ship, bullets, 
                        aliens, timerVal):
    """обновление позиций пуль и уничтожает старые пули."""
    # обновление позиций пуль
    bullets.update(timerVal);

    # удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet);
    print(len(bullets));

    # проверка попадания пули в пришельца.
    # при обнаружении попадания удалить пулю и пришельца.
    #collisions = pygame.sprite.groupcollide(bullets, aliens, True, True);
    collisions = pygame.sprite.groupcollide(bullets, aliens, not ai_settings.super_bullet, True);

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points*len(aliens);
        sb.prep_score();
        check_high_score(stats, sb);


    if len(aliens) == 0:
        # уничтожение старых пуль и создание новых
        bullets.empty();
        ai_settings.increase_speed();
        create_fleet(ai_settings, screen, ship, aliens);

        stats.level += 1;
        sb.prep_level();


def get_number_aliens_x(ai_settings, alien_width):
    """вычислит количесво пришельцев в ряду."""
    available_space_x = ai_settings.screen_width - 2 * alien_width;
    number_aliens_x = int(available_space_x / (2 * alien_width));
    return number_aliens_x;


def get_number_rows(ai_settings, ship_height, alien_height):
    """Определяет количесво рядов, помещающихся на экране."""
    available_space_y = (ai_settings.screen_height - 
                        (3*alien_height) - ship_height);
    number_rows = int(available_space_y / (2*alien_height));
    return number_rows;


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """создает пришельца и размещает его в ряду"""
    alien = Alien(ai_settings, screen);
    alien_width = alien.rect.width;
    alien.x = alien_width + 2 * alien_width * alien_number;
    alien.rect.x = alien.x;
    alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number;
    aliens.add(alien);


def create_fleet(ai_settings, screen, ship, aliens):
    """ создает флот пришельцев  """
    # создание пришельца и вычисление количества пришельцев в ряду
    # изнтервал между соседними пришельцами равен одной ширине пришельца

    alien = Alien(ai_settings, screen);
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width);
    number_rows = get_number_rows(ai_settings, ship.rect.height
                                            , alien.rect.height);
    
    # создание флота пришельцев
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # создание пришельца и размещение его в ряду.
            create_alien(ai_settings, screen, aliens, alien_number, row_number);


def create_stars(ai_settings, screen, stars):
   
    for i in range(0, ai_settings.stars_count):
        x = randint(0, ai_settings.screen_width);
        y = randint(0, ai_settings.screen_height);
        size = randint(ai_settings.min_stars_size , ai_settings.max_stars_size);

        tempStar = Star(size, 'images/starImage.png', screen, [x, y]);
        stars.add(tempStar);


def update_aliens(aliens, stats, screen, ai_settings, timerVal, 
                                        ship, bullets, sb):
    """обновляет позиции всех пришельцев во флоте."""
    check_fleet_edges(ai_settings, aliens);
    aliens.update(timerVal);

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb);

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb);


def check_fleet_edges(ai_settings, aliens):
    """реагирует на достижение пришельцем края экрана."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_derection(ai_settings, aliens);
            break;

def change_fleet_derection(ai_settings, aliens):
    """опускает весь флот и меняет направление флота."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed;
    ai_settings.fleet_direction *= -1;


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """обрбатывает столкновение корабля с пришельцем."""
    if stats.ships_left > 0:
        # уменьшение ships_left
        stats.ships_left -= 1;
        sb.prep_ships();

        # очистка списков пришельцев и пуль
        aliens.empty();
        bullets.empty();

        # создание новго флота и размещение корабля в центре
        create_fleet(ai_settings, screen, ship, aliens);
        ship.center_ship();

        # пауза
        sleep(0.5);
    else:
        stats.game_active = False;


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """проверяет, добрались ли пришельцы до нижнего края экрана."""
    screen_rect = screen.get_rect();
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # происходит тоже, что и при столкновении с кораблем
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb);
            break;


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens
                            , bullets, mouse_x, mouse_y, sb):
    """запускает новую игру, при нажании кнопки play"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        start_game(ai_settings, screen, ship, aliens, stats, bullets, sb);
        
   
def start_game(ai_settings, screen, ship, aliens, stats, bullets, sb):

    ai_settings.initialize_dynamic_settings();
    # сброс игровой статистики
    stats.game_active = True;
    stats.reset_stat();
    

    # очистка пришельцев и пуль
    aliens.empty();
    bullets.empty();

    # создание нового флота
    create_fleet(ai_settings, screen, ship, aliens);
    ship.center_ship();

    sb.prep_score();
    sb.prep_ships();
    sb.prep_high_score();
    sb.prep_ships();


def check_high_score(stats, sb):
    """проверяет появился ли новый рекорд"""
    if stats.high_score < stats.score:
        stats.high_score = stats.score;
        sb.prep_high_score();
