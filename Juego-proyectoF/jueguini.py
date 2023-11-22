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

# Pulsadores (círculos)
circles = []
for i in range(4):
    circle_rect = pygame.draw.circle(screen, (255, 255, 255), (150 + i * 200, height - 50), 50)
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                correct_hits += 1
                hits.append((circles[0].centerx, frame_count))
            elif event.key == pygame.K_DOWN:
                correct_hits += 1
                hits.append((circles[1].centerx, frame_count))
            elif event.key == pygame.K_LEFT:
                correct_hits += 1
                hits.append((circles[2].centerx, frame_count))
            elif event.key == pygame.K_RIGHT:
                correct_hits += 1
                hits.append((circles[3].centerx, frame_count))

    screen.fill(background_color)

    for circle_rect in circles:
        pygame.draw.circle(screen, (255, 255, 255), circle_rect.center, 50)

    for hit in hits:
        angle = math.atan2(hit[0] - width / 2, height - height / 2 - hit[1])
        diamond_pos = (hit[0] - 100 / 2, hit[1] - 100 / 2)
        diamond = pygame.Surface((100, 100))
        diamond.fill((255, 255, 255))
        diamond_rotated = pygame.transform.rotate(diamond, math.degrees(angle))
        screen.blit(diamond_rotated, diamond_pos)

    frame_count += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()