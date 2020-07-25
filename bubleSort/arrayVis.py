import pygame;

def calcMode(array):

    length = len(array);

    width = length * 5;
    height = max(array) + 5;

    return (width, height);

def showArray(array, screen):
    posX = 0;
    for n in array:
        rect = pygame.Rect(posX, 0, 3, n);
        rect.bottom = max(array) + 3;
        screen.fill((255, 255, 255), rect);
        posX += 5;
