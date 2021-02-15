import pygame as pg  # Importa a biblioteca pygame com o nome de pg
import sys  # Importa a biblioteca System

from pygame.locals import *  # Adiciona constantes utilizadas pelo pygame

pg.init()  # Inicializa toda a biblioteca e funcionalidades do pygame

clock = pg.time.Clock()  # Cria um objeto relógio que será responsável por manter o FPS do jogo
WINDOW_SIZE = (400, 400)  # Constante que define o tamanho da janela

screen = pg.display.set_mode(WINDOW_SIZE, 0, 32)  # Comando responsável por criar a janela
pg.display.set_caption("Meu Jogo")  # Adiciona um título para a janela

while True:  # Loop principal do jogo

    for event in pg.event.get():  # Verifica se algum evento está acontecendo, normalmente eventos de teclado e mouse
        if event.type == QUIT:  # Condicional, caso o evento seja o de fechar a janela então:
            pg.quit()  # Fecha o pygame
            sys.exit() # Fecha a janela e o programa

    pg.display.update()  # Atualiza a tela
    clock.tick(60)  # Define a quantidade de quadros por segundo do jogo
