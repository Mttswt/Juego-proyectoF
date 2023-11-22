import pygame
reloj = pygame.time.Clock()
class Nota:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 10

    def dibujar(self, superficie):
        pygame.draw.rect(superficie, (255, 255, 255), (self.x, self.y, self.ancho, self.alto))

    def actualizar(self, velocidad):
        self.y += velocidad

reloj.tick()