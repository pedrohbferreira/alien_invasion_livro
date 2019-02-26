# -*- coding: utf-8 -*-
from settings import Settings


class GameStats(object):
    """Armazena todos os dados estatiscos do jogo"""

    def __init__(self, ai_settins: Settings):
        """
        Inicializa todos os dados estatíscos, e dados default
        :param ai_settins: Configuração do jogo, objeto da classe Settings()
        """
        self.ai_settings = ai_settins
        self.ships_left = None
        self.score = 0

        self.reset_stats()
        self.game_active = False

        # pontuação máxima
        self.high_score = 0
        # informa o level
        self.level = 1

    def reset_stats(self):
        """Inicia os dados estatísticos, que mudam durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # informa o level
        self.level = 1
