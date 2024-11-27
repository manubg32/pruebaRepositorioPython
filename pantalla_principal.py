import pygame
from pantalla_juego import *


class pantalla_principal:


    def __init__(self, config):

        self.config = config

        self.activo = True

        # Cargar imágenes en Pygame
        self.IMG_FONDO = pygame.image.load("src/pantallaPrincipal.png")
        self.IMG_HIGH = pygame.image.load("src/high.png")
        self.IMG_HIGH_PULSADO = pygame.image.load("src/highP.png")
        self.IMG_MID = pygame.image.load("src/mid.png")
        self.IMG_MID_PULSADO = pygame.image.load("src/midP.png")
        self.IMG_LOW = pygame.image.load("src/low.png")
        self.IMG_LOW_PULSADO = pygame.image.load("src/lowP.png")
        self.pos = 1  # Posición inicial

    def gestion_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if self.pos < 3:
                        self.pos += 1
                elif event.key == pygame.K_UP:
                    if self.pos > 1:
                        self.pos -= 1
                elif event.key == pygame.K_SPACE:
                    if self.pos == 1:
                        self.config.dificultad = 600
                        self.activo = False
                    elif self.pos == 2:
                        self.config.dificultad = 500
                        self.activo = False
                    elif self.pos == 3:
                        self.config.dificultad = 400
                        self.activo = False


    def dibujar(self, pantalla):
        pantalla.blit(self.IMG_FONDO, (0, 0))  # Fondo

        # Mostrar imágenes según la posición
        if self.pos == 1:
            pantalla.blit(self.IMG_HIGH_PULSADO, (0, 0))
            pantalla.blit(self.IMG_MID, (0, 0))
            pantalla.blit(self.IMG_LOW, (0, 0))
        elif self.pos == 2:
            pantalla.blit(self.IMG_HIGH, (0, 0))
            pantalla.blit(self.IMG_MID_PULSADO, (0, 0))
            pantalla.blit(self.IMG_LOW, (0, 0))
        elif self.pos == 3:
            pantalla.blit(self.IMG_HIGH, (0, 0))
            pantalla.blit(self.IMG_MID, (0, 0))
            pantalla.blit(self.IMG_LOW_PULSADO, (0, 0))

        # Actualizar la pantalla
        pygame.display.flip()

        if self.activo:
            return 0
        else:
            self.activo = True
            return 2
