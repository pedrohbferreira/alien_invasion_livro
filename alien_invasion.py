# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.sprite import Group
from pygame import Surface

import game_funcions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Inicia o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    ai_settings.set_icon("alien_icon_32x32.bmp")

    # cria uma tela com as dimensões de ai_settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )   # type: Surface

    pygame.display.set_caption("Alien Invasion")

    # cria o grupo de projéteis, todos disparados ficaram aqui
    bullets_group = Group()
    aliens_group = Group()

    # cria a espaçonave
    ship = Ship(ai_settings, screen)

    # cria a frota de aliens
    gf.create_fleet(ai_settings, screen, ship.rect.height, aliens_group)

    # cria a instancia para estatísticas
    stats = GameStats(ai_settings)

    score_board = Scoreboard(ai_settings, screen, stats)

    # cria a instancia do botão play
    btn_play = Button(screen, "Play")

    # Inicia o laço principal do jogo
    # neste onde ocorre todos os eventos
    while True:

        # escuta de eventos de mouse ou teclado
        gf.check_events(ai_settings, screen, stats, score_board, btn_play, ship, aliens_group, bullets_group)

        if stats.game_active:
            # atualiza a posição da nave
            ship.update()

            # atualiza e limpa os projéteis
            gf.update_bullets(ai_settings, screen, stats, score_board, ship.rect.height, bullets_group, aliens_group)

            # atualiza a posição dos aliens
            gf.update_aliens(ai_settings, stats, score_board, screen, ship, aliens_group, bullets_group)

        # atualiza as informações da tela
        gf.update_screen(ai_settings, screen, stats, score_board, ship, aliens_group, bullets_group, btn_play)


run_game()
