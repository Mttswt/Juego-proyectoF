import pygame

class Util:

    def cargar_imagen(self, nombre, optimizar = False):
        imagen = pygame.image.load(nombre)

        if optimizar:
            imagen = imagen.convert()
        else:
            imagen = imagen.convert_alpha()
        return imagen  
