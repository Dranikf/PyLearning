import pygame;
import sys;
from arrayVis import calcMode;


array = list(range(1,50));


def run_vis():

    pygame.init();
    screen = pygame.display.set_mode(calcMode(array));

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();


run_vis();
