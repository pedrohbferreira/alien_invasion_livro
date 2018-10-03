import sys
import pygame


def check_keydown_events(event, ship):
    """ Responde somente a eventos quando aperta alguma tecla """
    if event == pygame.K_RIGHT:
        ship.moving_right = True
    if event == pygame.K_LEFT:
        ship.moving_left = True
    if event == pygame.K_UP:
        ship.moving_top = True
    if event == pygame.K_DOWN:
        ship.moving_bottom = True


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


def check_events(ship):
    """
    Realiza a escuta de eventos, evento de mouse e/ou teclado \n\r
    Todo evento de teclado é do tipo(type) KEYDOWN \n\r
    Cada tecla do é uma key que corresponde a K_<alguma coisa> do pygame
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event.key, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event.key, ship)


def update_screen(settings, screen, ship):
    """Atualiza as imagens na tela, e gera/seta a mais recente"""
    # redesenha a tela
    screen.fill(settings.bg_color)
    ship.blitme()

    # a presenta a tela mais recente
    pygame.display.flip()
