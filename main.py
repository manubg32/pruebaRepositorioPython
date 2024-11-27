import pygame

from config import config
from pantalla_juego import pantalla_juego
from pantalla_principal import pantalla_principal

if __name__ == "__main__":
    # Inicializar Pygame
    pygame.init()

    config = config()

    # Configuración de la pantalla y los colores
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

        pantalla_actual = pp

        running = True

        while running:

            # Captura de eventos
            pantalla_actual.gestion_eventos(pygame.event.get())

            # Dibujar en la pantalla
            nueva = pantalla_actual.dibujar(pantalla)

            if nueva == 1:
                pantalla_actual = pantalla_principal(config)
            elif nueva == 2:
                pantalla_actual = pantalla_juego(config)

            # Controlar FPS
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
