import pygame
import random
class juego:
    # Inicializa pygame
    pygame.init()

    # Configura la pantalla
    pantalla = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Juego de ritmo")

    # Importa la clase Nota
    from notas import Nota

    # Carga el archivo de música
    #musica = pygame.mixer.Sound("CancionAMi.wav")

    # Establece el volumen de la música
    #musica.set_volume(0.5)

    # Reproduce la música
    #musica.play()

    # Crea una lista de notas
    notas = []

    # Establece la tasa de desove de notas
    tasa_de_desove = 2000

    # Establece la velocidad de las notas
    velocidad_de_las_notas = 0.5

    # Establece el tiempo objetivo
    tiempo_objetivo = 0

    # Bucle principal del juego
    while True:
        # Comprueba los eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Actualiza las notas
        for nota in notas:
            nota.actualizar(velocidad_de_las_notas)

            # Comprueba si la nota ha llegado al fondo de la pantalla
            if nota.y > pantalla.get_height():
                notas.remove(nota)

        # Comprueba si se ha alcanzado el tiempo objetivo
        if pygame.time.get_ticks() >= tiempo_objetivo:
            # Crea una nueva nota
            nota = None

            # Create a new instance of the Nota class
            nota = Nota(random.randrange(0, pantalla.get_width() - 60), 0)

            notas.append(nota)

            # Actualiza el tiempo objetivo
            tiempo_objetivo = pygame.time.get_ticks() + tasa_de_desove

        # Comprueba si se ha presionado una tecla
        if evento.type == pygame.KEYDOWN:
            # Comprueba si la tecla presionada es una de las teclas a, s, d o f
            if evento.key == pygame.K_a:
                # La nota correspondiente se ha presionado correctamente
                notas[0].correcta = True
            elif evento.key == pygame.K_s:
                # La nota correspondiente se ha presionado correctamente
                notas[1].correcta = True
            elif evento.key == pygame.K_d:
                # La nota correspondiente se ha presionado correctamente
                notas[2].correcta = True
            elif evento.key == pygame.K_f:
                # La nota correspondiente se ha presionado correctamente
                notas[3].correcta = True

        # Rellena la pantalla con negro
        pantalla.fill((0, 0, 0))

        # Dibuja las notas
        for nota in notas:
            nota.dibujar(pantalla)

        # Actualiza la pantalla
        pygame.display.flip()

