import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Classe que servirá de projétil das naves"""

    def __init__(self, settings, screen, ship):
        """Cria a instancia de um projétil"""
        super(Bullet, self).__init__()
        self.screen = screen

        # cria uma área(retângulo = rect) para o projétil em (x=0,y=0)
        # define a posição no topo-centro da nave
        # self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        # self.rect.centerx = ship.rect.centerx
        # self.rect.top = ship.rect.top

        # alternativa para teste
        self.rect = pygame.Rect(ship.rect.centerx, ship.rect.top, settings.bullet_width, settings.bullet_height)

        # armazena a posição decima do projétil
        self.y = float(self.rect.y)

        # pega as configs de cor e velocidade
        self.color = settings.bullet_color
        self.speed = settings.bullet_speed_factor

    def update(self):
        """
        Move o projétil pra cima da tela \n\r
        Decrementa de y pois quanto mais par abaixo da tela, maior o valor \n\r
        o canto superior esquerdo, corresponde ao eixo x=0, y=0
        """
        # atualizado do projétil
        self.y -= self.speed
        # atualiza a posição
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
