import pygame
from pantalla_juego import *


class pantalla_principal:

    #Metodo constructor de la pantalla principal
    def __init__(self, config):

        #Creamos un config para obtener la dificultad
        self.config = config

        #Variable que mantendrá la pantalla pintándose
        self.activo = True

        #Cargamos la musica del menú principal
        pygame.mixer.music.load("src/menu.mp3")
        pygame.mixer.music.play(loops=-1)

        #Cargamos las imágenes necesarios en Pygame
        self.IMG_FONDO = pygame.image.load("src/pantallaPrincipal.png")
        self.IMG_HIGH = pygame.image.load("src/high.png")
        self.IMG_HIGH_PULSADO = pygame.image.load("src/highP.png")
        self.IMG_MID = pygame.image.load("src/mid.png")
        self.IMG_MID_PULSADO = pygame.image.load("src/midP.png")
        self.IMG_LOW = pygame.image.load("src/low.png")
        self.IMG_LOW_PULSADO = pygame.image.load("src/lowP.png")


        self.pos = 1  # Posición inicial

    #Gestionamos los eventos
    def gestion_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.QUIT: #Cerramos el juego
                pygame.quit()
            elif event.type == pygame.KEYDOWN: #Si se pulsa una tecla, cambiamos la posicion siempre que sea 1, 2 o 3 para elegir dificultad
                if event.key == pygame.K_DOWN:
                    if self.pos < 3:
                        self.pos += 1
                elif event.key == pygame.K_UP:
                    if self.pos > 1:
                        self.pos -= 1
                elif event.key == pygame.K_SPACE: #Al pulsar el espacio elegimos la opcion de la dificultad y lo mandamos al config, tambien cambiamos el activo para que se cambie la pantalla
                    if self.pos == 1:
                        self.config.dificultad = 600
                        self.activo = False
                    elif self.pos == 2:
                        self.config.dificultad = 500
                        self.activo = False
                    elif self.pos == 3:
                        self.config.dificultad = 400
                        self.activo = False

    #Dibujamos la pantalla
    def dibujar(self, pantalla):
        #Todas las imagenes son de 600x400, lo mismo que la ventana por lo que se coloca en el 0,0
        pantalla.blit(self.IMG_FONDO, (0, 0))  # Fondo

        #Mostramos las imágenes según la posición
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

        #Actualizar la pantalla
        pygame.display.flip()

        #Siempre que se desactive la pantalla se le manda la opcion correspondiente para que se active la pantalla contraria
        if self.activo:
            return 0
        else:
            self.activo = True
            return 2
