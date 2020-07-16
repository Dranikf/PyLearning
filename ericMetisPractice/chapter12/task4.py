import pygame;
import sys;


def run_game():
    # инициализирует игру и создаёт объект экрана.
    pygame.init();
    screen = pygame.display.set_mode((
        100, 100));
    pygame.display.set_caption('Alien Invasion');


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key);

run_game();
