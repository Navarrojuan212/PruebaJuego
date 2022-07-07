import pygame, sys
from pygame.locals import *

# Inicializamos
pygame.init()

# Creamos la ventana del juego y especificamos las dimensiones
PANTALLA = pygame.display.set_mode((500,400))
pygame.display.set_caption('Mi primer Juego xD')

# Este bucle es necesario para que la ventana se mantenga abierta

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
