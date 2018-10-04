# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.sprite import Group

import game_funcions as gf
from settings import Settings
from ship import Ship


def run_game():
    # Inicia o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()
    ai_settings.set_icon("alien_icon_32x32.bmp")

    # cria uma tela com as dimensões de ai_settings
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # cria o grupo de projéteis, todos disparados ficaram aqui
    bullets_group = Group()
    aliens_group = Group()

    # cria a espaçonave
    ship = Ship(ai_settings, screen)

    # cria a frota de aliens
    gf.create_fleet(ai_settings, screen, ship.rect.height, aliens_group)

    # Inicia o laço principal do jogo
    # neste onde ocorre todos os eventos
    while True:

        # escuta de eventos de mouse ou teclado
        gf.check_events(ai_settings, screen, ship, bullets_group)

        # atualiza a posição da nave
        ship.update()

        # atualiza e limpa os projéteis
        gf.update_bullets(bullets_group)

        # atualiza as informações da tela
        gf.update_screen(ai_settings, screen, ship, aliens_group, bullets_group)


run_game()
