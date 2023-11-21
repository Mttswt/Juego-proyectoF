import pygame, notas, sys
class Juego:
    def __init__(self):
        self.SCREEN_WIDTH = 1066
        self.SCREEN_HEIGHT = 600

        pygame.init()
        pantalla = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("heros del ritmo")


        
    def jugar(self):
        pass
