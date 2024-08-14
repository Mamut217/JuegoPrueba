import pygame, sys
from pygame import *

pygame.init()
Pantalla = pygame.display.set_mode((500,400))
pygame.display.set_caption("El pequeño Mammut")

#Definir colores 
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED   = (255,0,0)
BLUE  = (0,0,255)

C6A3008 = (106,48,8)
CE8BF04 = (232,191,4)

Pantalla.fill(WHITE)

Rectangulo = pygame.draw.rect(Pantalla, GREEN, (100,100,80,80))
Linea = pygame.draw.line(Pantalla, BLUE, [0,100], [100,100],5)
Circulo = pygame.draw.circle(Pantalla, RED, (200,200), 20)
Elipse = pygame.draw.ellipse(Pantalla, CE8BF04, (275,200,40,80),5)

Puntos = [(100,300),(150,100),(300,100)]
pygame.draw.polygon(Pantalla,C6A3008,Puntos,5)
#Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
