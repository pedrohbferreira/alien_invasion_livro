import pygame


class Settings(object):
    """Classe que contem todas as configurações"""

    def __init__(self):
        """Inicializa as configurações do jogo"""
        # configurações de tela
        self.screen_width = 1000
        self.screen_height = 600

        # configuração de cor
        self.bg_color = (230, 230, 230)

        # guarda o icone do jogo
        self.icon_image = None

        # velocidade das naves
        self.ship_speed_factor = 1.5

    def set_icon(self, icon_name):
        """
        Seta o icone do jogo, deve ser um arquivo .bmp \n\r
        :param icon_name: nome da imagem de icone .bmp
        """
        # cria o icone, passando o tamanho máximo
        icon = pygame.Surface((32, 32))

        # define a cor de fundo do icone, preto, ficará transparente
        icon.set_colorkey((0, 0, 0))

        # carrega o img do icone
        self.icon_image = pygame.image.load('images/' + str(icon_name))

        # mapeia os pixels da imagem carregada para o icon(Surface) gerado
        for i in range(0, 32):
            for j in range(0, 32):
                icon.set_at((i, j), self.icon_image.get_at((i, j)))

        # define o icon na tela do jogo
        pygame.display.set_icon(icon)
