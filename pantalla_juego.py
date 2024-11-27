import random
import pygame



class pantalla_juego:

    dificultad = 0

    puntuacion = 0

    ALTO = 400

    SIZE_CASILLA = 20

    CABEZA_UP = pygame.image.load("src/cabeza.png")
    CABEZA_LEFT = pygame.transform.rotate(CABEZA_UP, 90)
    CABEZA_DOWN = pygame.transform.rotate(CABEZA_UP, 180)
    CABEZA_RIGHT = pygame.transform.rotate(CABEZA_UP, -90)

    CABEZA = CABEZA_RIGHT

    CUERPO_Y = pygame.image.load("src/cuerpo.png")
    CUERPO_X = pygame.transform.rotate(CUERPO_Y, 90)

    CUERPO = CUERPO_X


    COLA_UP = pygame.image.load("src/cola.png")
    COLA_LEFT = pygame.transform.rotate(COLA_UP, 90)
    COLA_DOWN = pygame.transform.rotate(COLA_UP, 180)
    COLA_RIGHT = pygame.transform.rotate(COLA_UP, -90)

    COLA = COLA_RIGHT



    MANZANA = pygame.image.load("src/manzana.png")

    COLOR_TEXTO = (255, 255, 255)


    def __init__(self, config):

        self.bordeIzquierdo = 0
        self.bordeDerecho = 600

        self.config = config

        self.dificultad = self.config.dificultad
        if self.dificultad == 500:
            self.ANCHO = 600
            self.dificultad = 600
        else:
            self.ANCHO = self.dificultad

        self.TOTAL_CUADROS = (self.ANCHO // self.SIZE_CASILLA) * (self.ALTO // self.SIZE_CASILLA)

        # Inicializamos la serpiente
        self.serpiente = [(300, 200), (280, 200), (260, 200)]
        self.direccion = "DERECHA"
        self.cambiar_a = self.direccion

        self.activo = True

        self.IMG_FONDO = pygame.image.load("src/imagenFondo.png")

        ruta = ""

        # Mostramos el tablero segun la dificultad
        if self.dificultad == 400:
            ruta = "src/tableroPequeño.png"
            self.bordeIzquierdo = 100
            self.bordeDerecho = 500
        elif self.dificultad == 500:
            ruta = "src/tableroMediano.png"
            self.bordeIzquierdo = 50
            self.bordeDerecho = 550
        elif self.dificultad == 600:
            ruta = "src/tableroGrande.png"

        self.generador_manzana = self.generar_manzana(self.serpiente)
        self.pos_manzana = next(self.generador_manzana)

        self.tablero = pygame.image.load(ruta)

    def dibujar(self, pantalla):
        pantalla.blit(self.IMG_FONDO, (0, 0))
        pantalla.blit(self.tablero, (0, 0))

        #Dibujamos la manzana
        pantalla.blit(self.MANZANA, self.pos_manzana)

        #Dibujamos la serpiente
        for i, segmento in enumerate(self.serpiente):
            if i == 0:
                pantalla.blit(self.CABEZA, segmento)  # Cabeza de la serpiente
            elif i == len(self.serpiente) - 1:
                pantalla.blit(self.COLA, segmento)  # Cola de la serpiente
            else:
                pantalla.blit(self.CUERPO, segmento)  # Cuerpo de la serpiente

        #Mostramos la puntuacion
        fuente = pygame.font.SysFont("Arial", 20)
        txt_Puntuacion = fuente.render(f"Puntuacion: {self.puntuacion} / {self.TOTAL_CUADROS}", True, self.COLOR_TEXTO)
        pantalla.blit(txt_Puntuacion, (10, 10))

        #Actualizamos la posicion de la serpiente
        self.mover_serpiente()

        # Actualizar la pantalla
        pygame.display.flip()

        if self.activo:
            return 0
        else:
            self.activo = True
            return 1

    #Generamos posiciones aleatorias de la manzana con un generador siempre que no coincida con el cuerpo
    def generar_manzana(self, serpiente):
        while True:
            x = random.randint(self.bordeIzquierdo // self.SIZE_CASILLA, (self.bordeDerecho - self.SIZE_CASILLA) // self.SIZE_CASILLA) * self.SIZE_CASILLA
            y = random.randint(0, (self.ALTO - self.SIZE_CASILLA) // self.SIZE_CASILLA) * self.SIZE_CASILLA
            if (x, y) not in serpiente:
                yield(x, y)

    def gestion_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and self.direccion != "ABAJO":
                    self.cambiar_a = "ARRIBA"
                elif evento.key == pygame.K_DOWN and self.direccion != "ARRIBA":
                    self.cambiar_a = "ABAJO"
                elif evento.key == pygame.K_LEFT and self.direccion != "DERECHA":
                    self.cambiar_a = "IZQUIERDA"
                elif evento.key == pygame.K_RIGHT and self.direccion != "IZQUIERDA":
                    self.cambiar_a = "DERECHA"


    def mover_serpiente(self):

        # Rotamos las imagenes correspondientemente
        if self.cambiar_a == "ARRIBA":
            self.CABEZA = self.CABEZA_UP
            self.COLA = self.COLA_UP
            self.CUERPO = self.CUERPO_Y
        elif self.cambiar_a == "ABAJO":
            self.CABEZA = self.CABEZA_DOWN
            self.COLA = self.COLA_DOWN
            self.CUERPO = self.CUERPO_Y
        elif self.cambiar_a == "IZQUIERDA":
            self.CABEZA = self.CABEZA_LEFT
            self.COLA = self.COLA_LEFT
            self.CUERPO = self.CUERPO_X
        elif self.cambiar_a == "DERECHA":
            self.CABEZA = self.CABEZA_RIGHT
            self.COLA = self.COLA_RIGHT
            self.CUERPO = self.CUERPO_X

        # Actualizamos la direccion
        self.direccion = self.cambiar_a

        # Actualizamos la posicion de la serpiente
        x_cabeza, y_cabeza = self.serpiente[0]
        if self.direccion == "ARRIBA":
            y_cabeza -= self.SIZE_CASILLA
        elif self.direccion == "ABAJO":
            y_cabeza += self.SIZE_CASILLA
        elif self.direccion == "IZQUIERDA":
            x_cabeza -= self.SIZE_CASILLA
        elif self.direccion == "DERECHA":
            x_cabeza += self.SIZE_CASILLA

        nueva_pos_cabeza = (x_cabeza, y_cabeza)

        # Condicion de fin del juego
        if x_cabeza < self.bordeIzquierdo or x_cabeza >= self.bordeDerecho or y_cabeza < 0 or y_cabeza >= self.ALTO or nueva_pos_cabeza in self.serpiente:
            self.activo = False

        # Agregamos la nueva cabeza a la serpiente
        self.serpiente.insert(0, nueva_pos_cabeza)

        # Verificamos si la serpiente come
        if nueva_pos_cabeza == self.pos_manzana:
            self.puntuacion += 1
            self.pos_manzana = next(self.generador_manzana)
        else:
            self.serpiente.pop()


