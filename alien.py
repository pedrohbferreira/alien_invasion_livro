# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Classe que representa um único alien"""

    def __init__(self, settings, screen):
        """Inicia o alien salvando a tela e o"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # carrega a imagem do alien e define o retangulo(rect)
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # cada novo alien no canto superior direito
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # armazena a posição decimal
        self.x = float(self.rect.x)

    def blitme(self):
        """Desenha o alien na posição atual"""
        self.screen.blit(self.image, self.rect)
