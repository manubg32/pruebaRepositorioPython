import random
import pygame



class pantalla_juego:

    #Declaramos e inicializamos algunas de las variables necesarias
    dificultad = 0
    puntuacion = 0
    ALTO = 400
    SIZE_CASILLA = 20

    #Cargamos la imagen correspondiente de la cabeza y la cola con sus respectivas modificaciones en variables
    CABEZA_UP = pygame.image.load("src/cabeza.png")
    CABEZA_LEFT = pygame.transform.rotate(CABEZA_UP, 90)
    CABEZA_DOWN = pygame.transform.rotate(CABEZA_UP, 180)
    CABEZA_RIGHT = pygame.transform.rotate(CABEZA_UP, -90)

    CUERPO_Y = pygame.image.load("src/cuerpo.png")
    CUERPO_X = pygame.transform.rotate(CUERPO_Y, 90)

    COLA_UP = pygame.image.load("src/cola.png")
    COLA_LEFT = pygame.transform.rotate(COLA_UP, 90)
    COLA_DOWN = pygame.transform.rotate(COLA_UP, 180)
    COLA_RIGHT = pygame.transform.rotate(COLA_UP, -90)

    #Inicializamos las variables con sus respectivas posiciones
    CABEZA = CABEZA_RIGHT
    CUERPO = CUERPO_X
    COLA = COLA_RIGHT


    #Cargamos la imagen de la manzana
    MANZANA = pygame.image.load("src/manzana.png")

    #Color blanco para el texto
    COLOR_TEXTO = (255, 255, 255)

    #Metodo constructor de la pantalla de juego
    def __init__(self, config):

        #Iniciamos la musica que se ejecutará durante el desarrollo del juego
        pygame.mixer.music.load("src/juego.mp3")
        pygame.mixer.music.play(loops=-1)

        #Inicializamos los bordes donde se desarrollará el juego
        self.bordeIzquierdo = 0
        self.bordeDerecho = 600

        #Creamos un archivo config
        self.config = config
        self.dificultad = self.config.dificultad

        #El ancho depende de la dificultad excepto en el modo intermedio que lo que hago es cambiar la velocidad de la serpiente
        if self.dificultad == 500:
            self.ANCHO = 600
            self.dificultad = 600
        else:
            self.ANCHO = self.dificultad

        #Calculamos el total de cuadros
        self.TOTAL_CUADROS = (self.ANCHO // self.SIZE_CASILLA) * (self.ALTO // self.SIZE_CASILLA)

        # Inicializamos la serpiente
        self.serpiente = [(300, 200), (280, 200), (260, 200)]
        self.direccion = "DERECHA"
        self.cambiar_a = self.direccion

        #Establecemos la condicion por la cual se sigue mostrando la pantalla
        self.activo = True

        #Cargamos la imagen de fondo
        self.IMG_FONDO = pygame.image.load("src/imagenFondo.png")

        ruta = ""

        # Ruteamos el tablero segun la dificultad y establecemos sus límites
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

        #Instanciamos un generador de manzana con una posicion x, y
        self.generador_manzana = self.generar_manzana(self.serpiente)

        #Ponemos la manzana en la posicion que se nos indique
        self.pos_manzana = next(self.generador_manzana)

        #Cargamos la imagen del tablero
        self.tablero = pygame.image.load(ruta)

    #Metodo que dibuja en la pantalla el juego
    def dibujar(self, pantalla):
        #La imagen de fondo y la del tablero tienen el mismo tamaño que la ventana por eso se instancian en 0,0
        pantalla.blit(self.IMG_FONDO, (0, 0))
        pantalla.blit(self.tablero, (0, 0))

        #Dibujamos la manzana
        pantalla.blit(self.MANZANA, self.pos_manzana)

        #Dibujamos la serpiente por segmentos
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

        #Actualizar la pantalla
        pygame.display.flip()

        #Siempre que se desactive la pantalla se le manda la opcion correspondiente para que se active la pantalla contraria
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

    #Gestionamos los eventos
    def gestion_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT: #Quitamos el juego
                pygame.quit()
            if evento.type == pygame.KEYDOWN: #Si el evento es una tecla de la cruceta pulsada movemos la serpiente siempre que la direccion a la que se va a mover no sea la contraria a la que está yendo
                if evento.key == pygame.K_UP and self.direccion != "ABAJO":
                    self.cambiar_a = "ARRIBA"
                elif evento.key == pygame.K_DOWN and self.direccion != "ARRIBA":
                    self.cambiar_a = "ABAJO"
                elif evento.key == pygame.K_LEFT and self.direccion != "DERECHA":
                    self.cambiar_a = "IZQUIERDA"
                elif evento.key == pygame.K_RIGHT and self.direccion != "IZQUIERDA":
                    self.cambiar_a = "DERECHA"

    #Metodo que mueve la serpiente a la siguiente posicion
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
            sonido = pygame.mixer.Sound("src/manzana.mp3") #Reproducimos el sonido
            sonido.play()
            self.puntuacion += 1
            self.pos_manzana = next(self.generador_manzana)
        else:
            self.serpiente.pop()


