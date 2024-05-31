import pygame

pygame.init()

def esticar_cobrinha(tela, lista_cobrinha):
    for coord in lista_cobrinha:
        pygame.draw.rect(tela, (0, 255, 0), (coord[0], coord[1], 10, 10))