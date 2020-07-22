import sys;
import pygame;
from ship import Ship;
from alien import Alien;
from bullet import Bullet;
from pygame.sprite import Group;
from label import Label;
from fuckThePython import Stat;
from button import Button;

class GameController():
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings;
        self.screen = screen;
        self.ship = Ship(self.ai_settings, self.screen);
        self.alien = Alien(ai_settings, screen); 
        self.bullets = Group();
        self.screen_rect = screen.get_rect();
        self.stat = Stat();
        self.label = Label(ai_settings, screen, 'shoots: 0' , 0);
        self.label2 = Label(ai_settings, screen, 'hits: 0', 50);
        self.button = Button(ai_settings, screen, 'Play');
        
    
    def check_quit_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit();


    def check_events(self):
        for event in pygame.event.get():
            self.check_quit_event(event);
            if event.type == pygame.KEYDOWN:
                self.check_key_down_event(event);
            if event.type == pygame.KEYUP:
                self.check_key_up_event(event);


    def create_bullet(self):
        new_bullet = Bullet(self.ship.rect, self.ai_settings, self.screen);
        self.bullets.add(new_bullet);

    
    def analise_shoots(self):
        self.stat.tot_bullets += 1;
        self.label.prep_msg('shoots: ' + str(self.stat.tot_bullets));

 
    def fire_bullet(self):
        self.create_bullet();
        self.analise_shoots();

        if self.stat.tot_bullets >= self.ai_settings.max_shoots:
            self.ai_settings.game_active = False;

       
    def check_key_down_event(self, event):
        if event.key == pygame.K_q:
            sys.exit();
        if event.key == pygame.K_UP:
            self.ship.moving_up = True;
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True;
        if event.key == pygame.K_SPACE:
            self.fire_bullet();
            


    def check_key_up_event(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False;
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False;

    def update_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.update();

            if(bullet.rect.left > self.screen_rect.right):
                self.bullets.remove(bullet);

        print(len(self.bullets));


    def update_primitivs(self):
        self.ship.update();
        self.alien.update();
        self.update_bullets();

    
    def collision_check(self): 
        # bullets and alien
        hitted_bul = pygame.sprite.spritecollide(self.alien, self.bullets, True);
        for bullet in hitted_bul:
            self.stat.damage_to_al += 1;

        self.label2.prep_msg('hits: ' + str(self.stat.damage_to_al));

    def frame(self):
        self.update_primitivs();
        self.collision_check();

        
    def draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw();


    def drawHud(self):
        self.label.draw();
        self.label2.draw();
        
        if not self.ai_settings.game_active:
            self.button.draw_button();


    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color);
        self.ship.blitme();
        self.draw_bullets();
        self.drawHud();
        self.alien.blitme();
        pygame.display.flip();


    def start_game(self):
        self.ai_settings.game_active = True;
        self.ship.set_default_pos();
        self.stat.tot_bullets = 0;
        self.stat.damage_to_al = 0;


    def check_hud_colis(self, mouse_x, mouse_y):
        if self.button.rect.collidepoint(mouse_x, mouse_y):
            self.start_game();


    def check_menu_events(self):
        for event in pygame.event.get():
            self.check_quit_event(event);
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos();
                self.check_hud_colis(mouse_x, mouse_y);


    def menuFrame(self):
        self.check_menu_events();
