# -*- coding: utf-8 -*-

import pygame.font


class Button(object):
    """Classe responsável pelos botões da tela"""

    def __init__(self, screen, mensagem):
        """
        Cria uma instancia de Button, passando as configurações do jogo, a tela e a mensagem \n\r
        param ai_settings: Configurações o jogo, objeto do tipo Settings()\n\r
        :param screen: Objeto de pygame.display.set_mode()
        :param mensagem: Mensagem do botão
        """
        self.screen = screen
        self.screen_rec = screen.get_rect()

        # dimensões do botão
        self.width, self.height = 200, 50
        self.button_color, self.text_color = (0, 255, 0), (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # constrói o rect do botão e coloca no centro
        # passa coordenada x, y e dimensões
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rec.center

        # a mensagem deve ser somente uma vez
        self.prep_msg(mensagem)

    def prep_msg(self, mensagem):
        """
        Prepara a mensagem, transformando-a em imagem renderizada e centraliza no botão
        :param mensagem: Mensagem do botão
        """
        # renderiza a mensagem
        self.msg_imagem = self.font.render(mensagem, True, self.text_color, self.button_color)
        self.msg_imagem_rect = self.msg_imagem.get_rect()
        self.msg_imagem_rect.center = self.rect.center

    def draw_button(self):
        """Desenha  botão na tela"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_imagem, self.msg_imagem_rect)
