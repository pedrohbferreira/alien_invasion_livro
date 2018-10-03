# -*- coding: utf-8 -*-

import sys
import pygame

from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets_group):
    """Dispara um projétil se o limiete não for alcançado"""
    # cria um novo projétil e coloca-o no grupo
    if len(bullets_group) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets_group.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets_group):
    """ Responde somente a eventos quando aperta alguma tecla """
    if event == pygame.K_RIGHT:
        ship.moving_right = True
    if event == pygame.K_LEFT:
        ship.moving_left = True
    if event == pygame.K_UP:
        ship.moving_top = True
    if event == pygame.K_DOWN:
        ship.moving_bottom = True
    if event == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets_group)


def check_keyup_events(event_key, ship):
    """ Responde somente a eventos quando solta alguma tecla """
    if event_key == pygame.K_q or event_key == pygame.K_ESCAPE:
        sys.exit()
    if event_key == pygame.K_RIGHT:
        ship.moving_right = False
    if event_key == pygame.K_LEFT:
        ship.moving_left = False
    if event_key == pygame.K_UP:
        ship.moving_top = False
    if event_key == pygame.K_DOWN:
        ship.moving_bottom = False


def check_events(ai_settings, screen, ship, bullets_group):
    """
    Realiza a escuta de eventos, evento de mouse e/ou teclado \n\r
    Todo evento de teclado é do tipo(type) KEYDOWN \n\r
    Cada tecla do é uma key que corresponde a K_<alguma coisa> do pygame
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event.key, ai_settings, screen, ship, bullets_group)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event.key, ship)


def update_screen(ai_settings, screen, ship, aliens_group, bullets_group):
    """Atualiza as imagens na tela, e gera/seta a mais recente"""
    # redesenha a tela
    screen.fill(ai_settings.bg_color)

    # redesenha todos os projéteis antes de atualizar a tela = flip()
    for bullet in bullets_group.sprites():
        bullet.draw_bullet()

    # desenha a nave e o alien
    ship.blitme()
    aliens_group.draw(screen)

    # a presenta a tela mais recente
    pygame.display.flip()


def update_bullets(bullets_group):
    """
    Atualiza os projéteis na tela e limpa os que passaram os limites da screen
    """
    # chama o método update de cada item o grupo
    bullets_group.update()

    # limpa os projéteis cuja a base(bottom) seja 0, o bottom está no topo da tela
    for bullet in bullets_group.copy():
        if bullet.rect.bottom <= 0:
            bullets_group.remove(bullet)


def create_fleet(ai_settings, screen, aliens_group):
    """
    Cria uma frota de alienígena \n\r
    Utiliza o primeiro criado para calcular a quantidade por linha e o esoaçamento \n\r
    :param ai_settings: Objeto da classe Settings
    :param screen: Objeto de retorne de pygame.display.set_mode()
    :param aliens_group: objeto da classe Group() em pygame.sprite
    """
    # este é apenas para ter as medidas
    alien = Alien(ai_settings, screen)
    largura_alien = alien.rect.width
    espaco_disponivel_x = ai_settings.screen_width - (2 * largura_alien)
    numero_aliens_x = int(espaco_disponivel_x / (2 * largura_alien))

    # cria a primeira linha de alienígenas
    for numero_alien in range(numero_aliens_x):
        # cria um alienígena e coloca n alinha
        alien = Alien(ai_settings, screen)
        alien.x = largura_alien + 2 * largura_alien * numero_alien
        alien.rect.x = alien.x
        # adiciona ao grupo de alienígenas
        aliens_group.add(alien)
