# -*- coding: utf-8 -*-

import pygame
from pygame import Surface
from settings import Settings
from pygame.sprite import Sprite


class Ship(Sprite):
    """
    Classe responsável por todas as funcionalidades da nave
    """
    def __init__(self, settings: Settings, screen: Surface):
        """Inicializa a espaçonave e defina a posição inicial"""
        super(Ship, self).__init__()

        self.screen = screen
        self.setting = settings

        # carrega a imagem da nave
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # inicia cada nova nave na parte central inferior da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # valor decimal para o centro horizontal da nave
        self.__center_x = float(self.rect.centerx)
        self.__center_y = float(self.rect.centery)

        # flag para monitorar o andamento continuo para direita ou esquerda
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """
        Atualiza a posição da espaçonave enquanto estiver com a flag True \n \r
        Left e Right do rect(retângulo) corresponde ao x das coordenadas \n\r
        Atualiza p/ direita se a direita(right) do rect(retângulo da nave) seja menor que o rect da tela \n\r
        Atualiza p/ esquerda se a esquerda(left) do rect(retângulo da nave) seja maior que 0 \n\r
        Atualiza p/ cima se o topo(top) do rect(retângulo da nave) seja maior que 0 \n\r
        Atualiza p/ baixo se a base(bottom) do rect(retângulo da nave) seja menor que o da tela \n\r
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.__center_x += self.setting.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.__center_x -= self.setting.ship_speed_factor

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.__center_y += self.setting.ship_speed_factor

        if self.moving_top and self.rect.top > 0:
            self.__center_y -= self.setting.ship_speed_factor

        # atualiza a posição da nave
        self.rect.centerx = self.__center_x
        self.rect.centery = self.__center_y

    def blitme(self):
        """Desenha a espaçonave na tela"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centraliza o objeto na tela"""
        # inicia cada nova nave na parte central inferior da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # valor decimal para o centro horizontal da nave
        self.__center_x = float(self.rect.centerx)
        self.__center_y = float(self.rect.centery)
