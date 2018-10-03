import sys
import pygame

from bullet import Bullet


def fire_bullet(settings, screen, ship, bullets_group):
    """Dispara um projétil se o limiete não for alcançado"""
    # cria um novo projétil e coloca-o no grupo
    if len(bullets_group) < settings.bullets_allowed:
        new_bullet = Bullet(settings, screen, ship)
        bullets_group.add(new_bullet)


def check_keydown_events(event, settings, screen, ship, bullets_group):
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
        fire_bullet(settings, screen, ship, bullets_group)


def check_keyup_events(event, ship):
    """ Responde somente a eventos quando solta alguma tecla """
    if event == pygame.K_RIGHT:
        ship.moving_right = False
    if event == pygame.K_LEFT:
        ship.moving_left = False
    if event == pygame.K_UP:
        ship.moving_top = False
    if event == pygame.K_DOWN:
        ship.moving_bottom = False


def check_events(settings, screen, ship, bullets_group):
    """
    Realiza a escuta de eventos, evento de mouse e/ou teclado \n\r
    Todo evento de teclado é do tipo(type) KEYDOWN \n\r
    Cada tecla do é uma key que corresponde a K_<alguma coisa> do pygame
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event.key, settings, screen, ship, bullets_group)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event.key, ship)


def update_screen(settings, screen, ship, bullets_group):
    """Atualiza as imagens na tela, e gera/seta a mais recente"""
    # redesenha a tela
    screen.fill(settings.bg_color)
    ship.blitme()

    # redesenha todos os projéteis antes de atualizar a tela = flip()
    for bullet in bullets_group.sprites():
        bullet.draw_bullet()

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
