import sys
import pygame
import random

pygame.init()

# Dimensões da tela:
largura_tela = 640
altura_tela = 480

# Inicialização da Fonte e da Contagem de Pontos:
fonte = pygame.font.SysFont('Arial', 20, bold=True)
pontos = 0


# Criação da tela e ajustes de display:
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da Cobrinha')
clock = pygame.time.Clock()

# Especificações de tamanho e posição da Cobrinha:
largura_objeto_cobrinha = 10
altura_objeto_cobrinha = 10

x_cobrinha = largura_tela/2 - largura_objeto_cobrinha/2
y_cobrinha = altura_tela/2 - altura_objeto_cobrinha/2

lista_cobrinha = []
comprimento = 3 

# Especificações de tamanho e posição da Comidinha:
largura_objeto_comidinha = 10
altura_objeto_comidinha = 10

x_comidinha = random.randint(10, 620)
y_comidinha = random.randint(10, 460)

# Especificações de controle:
velocidade = 5
x_controle = velocidade
y_controle = 0