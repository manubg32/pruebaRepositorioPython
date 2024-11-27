import pygame

from config import config
from pantalla_juego import pantalla_juego
from pantalla_principal import pantalla_principal

if __name__ == "__main__":
    # Inicializar Pygame
    pygame.init()
    pygame.mixer.init()

    config = config()

    # Configuración de la pantalla y los iconos
    ANCHO, ALTO = 600, 400
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Python")
    logo = pygame.image.load("src/logo.png")
    pygame.display.set_icon(logo)

    # Reloj para controlar FPS
    clock = pygame.time.Clock()


    # Creamos objeto pantalla principal
    pp = pantalla_principal(config)


    # Función principal del juego
    def menu():

        #Iniciamos la pantalla al menu principal
        pantalla_actual = pp

        #Ponemos la condicion que corra el juego
        running = True

        while running:

            # Captura de eventos
            pantalla_actual.gestion_eventos(pygame.event.get())

            # Dibujar en la pantalla a través del metodo que contiene cada una de las pantallas que tenemos
            nueva = pantalla_actual.dibujar(pantalla)

            #Siempre que la pantalla esté activa con un booleano que contiene la clase se estará dibujando esa pantalla, si hay alguna condicion que deba cambiar la pantalla activa sera false y se pondrá la siguiente pantalla
            if nueva == 1:
                pantalla_actual = pantalla_principal(config) #Si lo que se retorna es 1 pintamos el menu
            elif nueva == 2:
                pantalla_actual = pantalla_juego(config) #Si lo que se retorna es 2 pintamos la pantalla del juego

            # Controlamos los FPS según la dificultad establecida (velocidad de la serpiente)
            if config.dificultad == 400:
                FPS = 6
            elif config.dificultad == 500:
                FPS = 10
            else:
                FPS = 15

            clock.tick(FPS)

        pygame.quit()


    # Ejecutar el juego
    menu()
