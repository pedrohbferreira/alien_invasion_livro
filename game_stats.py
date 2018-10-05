# -*- coding: utf-8 -*-


class GameStats(object):
    """Armazena todos os dados estatiscos do jogo"""

    def __init__(self, ai_settins):
        """
        Inicializa todos os dados estatíscos, e dados default
        :param ai_settins: Configuração do jogo, objeto da classe Settings()
        """
        self.ai_settings = ai_settins
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Inicia os dados estatísticos, que mudam durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
