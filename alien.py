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

    def update(self):
        """Move os aliens para a direita"""
        # multiplica por ou para ficar positivo ou -1 para negativo
        # elimina a necessidade de if-else para determinar a direção
        # + vai somar indo para a direita, - vai subtrair indo para esquerda
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_alien_direction)
        self.rect.x = self.x

    def check_bordas(self):
        """Devolve True se o alien estiver em alguma das bordas"""
        # pega o retangulo da tela
        screen_rect = self.screen.get_rect()

        # se a borda direita do alien >= que a borda direita da tela
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
