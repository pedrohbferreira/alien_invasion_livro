# -*- coding: UTF-8 -*-
import pygame
from settings import Settings
from game_stats import GameStats
from pygame import Surface
from pygame.sprite import Group
from ship import Ship


class Scoreboard(object):
    """Mostra informações do jogo"""
    def __init__(self, ai_settings: Settings, screen: Surface, stats: GameStats):
        # inicializa os atributos
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # configurações de font
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepara imagem da potuação
        self.score_image = None
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """transforma a pontuação em imagem"""
        roudend_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(roudend_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # exibe na parte superior direita
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)  # type: Surface

        # centraliza a pontuação na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top - 20

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        # posiciona abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # desenha as naves
        self.ships.draw(self.screen)
