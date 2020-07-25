import pygame;
import sys;
from arrayVis import calcMode;
from arrayVis import showArray;
from random import randint;
from pygame.time import Clock;

array = list(range(1,1000, 3) );
print(len(array));


def bubleSort(array):
    result = True;

    for i in range(0 , len(array) - 1):
        if array[i+1] < array[i]:
            swap(array, i , i + 1);
            result = False;
        
    return result;

def swap(array, ind1, ind2):
    temp = array[ind1];
    array[ind1] = array[ind2];
    array[ind2] = temp;


def run_vis():

    pygame.init();
    screen = pygame.display.set_mode(calcMode(array));
    stateFlag = 0; # 0 - nothing, 1 - mixing, 2 - sorting
    clock = Clock();
    tempTime = 0;

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if stateFlag != 1:
                        stateFlag = 1;
                    else:
                        stateFlag = 0;

                if event.key == pygame.K_s:
                    if stateFlag != 2:
                        stateFlag = 2;
                        tempTime = pygame.time.get_ticks()
                    else:
                        stateFlag = 0;
                    
        
        if stateFlag == 1:
            swap(array, randint(0, len(array)-1), randint(0, len(array)-1));

        if stateFlag == 2:
            if bubleSort(array) == True:
                stateFlag = 0;
                print((pygame.time.get_ticks() - tempTime)/1000);
        
        screen.fill((20, 20, 20));

        showArray(array, screen);

        pygame.display.flip();
        


run_vis();
