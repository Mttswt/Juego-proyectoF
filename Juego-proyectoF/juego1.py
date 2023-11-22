import pygame
import random
import math

pygame.init()

# Dimensiones de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Configuración de la pantalla
pygame.display.set_caption("Juego Rítmico")

# Carga de imágenes
diamond = pygame.image.load('imagenes/diamond.png')
circle = pygame.image.load('imagenes/circle.png')

# Carga de sonidos
hit = pygame.mixer.Sound('hit.wav')
miss = pygame.mixer.Sound('miss.wav')

# Pulsadores (círculos)
circles = []
for i in range(4):
    circle_rect = circle.get_rect(center=(150 + i * 200, height - 50))
    circles.append(circle_rect)

# Estilos
background_color = (20, 20, 20)

# Contador de frames
frame_count = 0

# Contador de pulsaciones correctas
correct_hits = 0

# Lista de hitos
hits = []

# Cronómetro
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for circle_rect in circles:
                if circle_rect.collidepoint(event.pos):
                    correct_hits += 1
                    hits.append((circle_rect.centerx, frame_count))
                    hit.play()

    screen.fill(background_color)

    for circle_rect in circles:
        screen.blit(circle, circle_rect)

    for hit in hits:
        angle = math.atan2(hit[0] - diamond.get_width() / 2, height - diamond.get_height() / 2 - hit[1])
        diamond_pos = (hit[0] - diamond.get_width() / 2, hit[1] - diamond.get_height() / 2)
        diamond_rotated = pygame.transform.rotate(diamond, math.degrees(angle))
        screen.blit(diamond_rotated, diamond_pos)

    frame_count += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()