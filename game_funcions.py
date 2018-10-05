# -*- coding: utf-8 -*-

import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets_group):
    """
    Dispara um projétil se o limite não for alcançado \n\r
    Adiciona ao grupo de projeteis se for menor que o número permitido em Settings()
    :param ai_settings: Configurações do jogo, objeto do tipo Settings()
    :param screen: Tela/quadro do jogo, objeto de pygame.display.set_mode()
    :param ship: Espaçonave do jogo, objeto do tipo Ship()
    :param bullets_group: Grupo de projéteis disparados, objeto de pygame.sprite.Group()
    """
    # verifica se o número de já gerados é menor que o permitido
    if len(bullets_group) < ai_settings.bullets_allowed:
        # cria um novo projétil e coloca-o no grupo
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets_group.add(new_bullet)


def check_keydown_events(event_key, ai_settings, screen, ship, bullets_group):
    """
    Responde somente a eventos quando aperta alguma tecla \n\r
    Seta para movimentos continuos nas direções \n\r
    :param event_key: Chave de evento disparado pelo teclado, tipo pygame.event.get().event.key
    :param ai_settings: Configurações do jogo, objeto do tipo Settings()
    :param screen: Tela/quadro do jogo, objeto de pygame.display.set_mode()
    :param ship: Espaçonave, objeto do tipo Ship()
    :param bullets_group: Grupo de projéteis disparados, objeto de pygame.sprite.Group()
    """
    # saí do jogo ao apertar 'q' ou 'esc'
    if event_key == pygame.K_q or event_key == pygame.K_ESCAPE:
        sys.exit()
    # testa o event_key.key para cada possibilidade
    # nas setas de direção, seta para movimento continuo
    if event_key == pygame.K_RIGHT:
        ship.moving_right = True
    if event_key == pygame.K_LEFT:
        ship.moving_left = True
    if event_key == pygame.K_UP:
        ship.moving_top = True
    if event_key == pygame.K_DOWN:
        ship.moving_bottom = True
    # em caso de barra de espaço, dispara um projétil
    if event_key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets_group)


def check_keyup_events(event_key, ship):
    """
    Responde somente a eventos quando solta alguma tecla \n\r
    :param event_key: Chave de evento disparado pelo teclado, tipo pygame.event.get().event.key
    :param ship: Espaçonave, objeto do tipo Ship()
    """
    if event_key == pygame.K_RIGHT:
        ship.moving_right = False
    if event_key == pygame.K_LEFT:
        ship.moving_left = False
    if event_key == pygame.K_UP:
        ship.moving_top = False
    if event_key == pygame.K_DOWN:
        ship.moving_bottom = False


def check_button_play(game_stats, btn_play, mouse_x, mouse_y):
    """
    Marca o game_active como True \n\r
    :param game_stats: Objeto com estatisticas do jogo, objeto de GameStats()
    :param btn_play: Botão play do jogo, objeto de Button()
    :param mouse_x: Posição x do clique do mouse
    :param mouse_y: Posição y do clique do mouse
    """
    if btn_play.rect.collidepoint(mouse_x, mouse_y):
        game_stats.game_active = True


def check_events(ai_settings, screen, game_stats, btn_play, ship, bullets_group):
    """
    Realiza a escuta de eventos, evento de mouse e/ou teclado \n\r
    Todos os eventos de teclado são do tipo(type) KEYDOWN \n\r
    Cada tecla do é uma key que corresponde a K_<alguma coisa> do pygame \n\r
    :param ai_settings: Configurações do jogo, objeto de Settings()
    :param screen: Tela/quadro do jogo, objeto de pygame.display.set_mode()
    :param game_stats: possui dados estatisticos do jogo, do tipo GameStats()
    :param btn_play: Objeto da classe Button()
    :param ship: Espaçonave do jogo, objeto de Ship()
    :param bullets_group: Grupo de balas disparadas, objeto de pygame.sprite.Group()
    """
    # para cada evento, mouse/teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()   # quando fechar em X da janela
        # eventos de teclado são em pygame.KEYDOWN
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event.key, ai_settings, screen, ship, bullets_group)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event.key, ship)
        # eventos do mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()   # pega a posição onde foi clicado
            check_button_play(game_stats, btn_play, mouse_x, mouse_y)


def update_screen(ai_settings, screen, game_stats, ship, aliens_group, bullets_group, button):
    """
    Atualiza as imagens na tela, e gera/seta a mais recente \n\r
    Atualiza também todo os conteúdos que devem ir para a tela \n\r
    :param ai_settings: Configurações do jogo, objeto de Settings()
    :param screen: Tela/quadro do jogo, objeto de pygame.display.set_mode()
    :param ship: Espaçonave do jogo, objeto do tipo Ship()
    :param game_stats: possui dados estatisticos do jogo, do tipo GameStats()
    :param aliens_group: Grupo de aliens gerados na tela, objeto de pygame.sprite.Group()
    :param bullets_group: Grupo de projéteis disparados, objeto de pygame.sprite.Group()
    :param button: Objeto da classe Button()
    """
    # redesenha a tela
    screen.fill(ai_settings.bg_color)

    # redesenha todos os projéteis antes de atualizar a tela = flip()
    for bullet in bullets_group.sprites():
        bullet.draw_bullet()

    # desenha a nave e o alien
    ship.blitme()
    aliens_group.draw(screen)

    # desenha o botão se o jogo não estiver ativo
    if not game_stats.game_active:
        button.draw_button()

    # a presenta a tela mais recente
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship_height, bullets_group, aliens_group):
    """
    Atualiza os projéteis na tela e limpa os que passaram os limites da screen \n\r
    Chama método para verificar colisão com algum alien \n\r
    :param ai_settings: Configurações do jogo, objeto do tipo Settings()
    :param screen: Tela/quadro do jogo, objeto de pygame.display.set_mode()
    :param ship_height: Altura da espaçonave
    :param bullets_group: Grupo de projéteis gerados, objeto de pygame.sprite.Group()
    :param aliens_group: Grupo de aliens gerados, objeto de pygame.sprite.Group()
    :return:
    """
    # chama o método update de cada item o grupo
    bullets_group.update()

    # limpa os projéteis cuja a base(bottom) seja 0, o bottom está no topo da tela
    for bullet in bullets_group.copy():
        if bullet.rect.bottom <= 0:
            bullets_group.remove(bullet)

    # verifica se um projétil atingiu o alien
    check_colisao_bullet_alien(ai_settings, screen, ship_height, bullets_group, aliens_group)


def check_colisao_bullet_alien(ai_settings, screen, ship_height, bullets_group, aliens_group):
    """
    Resolve a colisão entre projeteis e aliens \n\r
    Ao colidir, remove o projétil e o alien \n\r
    Cria uma nova leva de aliens caso não tenha mais ao remover \n\r
    :param ai_settings: Objeto da classe Settings
    :param screen: Objecto de pygame.display.set_mode()
    :param ship_height: Altura da nave
    :param bullets_group: Grupo de projéteis Objeto de pygame.sprite.Group()
    :param aliens_group: Grupo de alienígena, Objeto de pygame.sprite.Group()
    """
    # caso sim, remove o alien e o projétil, por isso o True, True no final do método
    colisoes = pygame.sprite.groupcollide(bullets_group, aliens_group, True, True)

    # verifica se ainda existem aliens, caso não, limpa as balas e recria a frota
    if len(aliens_group) == 0:
        # apaga os projéteis
        bullets_group.empty()
        # recria frota de aliens
        create_fleet(ai_settings, screen, ship_height, aliens_group)


def get_number_rows(screen_height, ship_height, alien_height) -> int:
    """
    Determina o número de linhas de aliens que cabem na tela \n\r
    :param screen_height: Altura total da tela, definido em Settings
    :param ship_height: Altura de uma espaçonave
    :param alien_height: Altura de um alien
    :return: Quantidade de de linhas possíveis
    """
    # cálculo: altura da tela, menos a altura de 3 aliens, menos a nave
    # 3 aliens: para 1 alien no topo e dois na base acima de 1 nave
    espaco_disponivel_y = (screen_height - (3 * alien_height) - ship_height)

    # espaço disponível dividido por 2x 1/5 de um alien
    numero_linhas = int(espaco_disponivel_y / (2 * alien_height))
    return numero_linhas


def get_number_aliens_x(screen_width, alien_width) -> int:
    """
    Determina o número de aliens que cabem em uma linha horizontal \n\r
    :param screen_width: Largura total da tela, determinado em Settings
    :param alien_width: largura de um alien
    :return: retorna o número de aliens possíveis na horizontal
    """
    espaco_disponivel_x = screen_width - (2 * alien_width)
    numero_aliens_x = int(espaco_disponivel_x / (2 * alien_width))
    return numero_aliens_x


def create_alien(ai_settings, screen, aliens_group, alien_number, numero_linhas):
    """
    Cria um alien e o adiciona em aliens_group, grupo de aliens gerenciado na tela \n\r
    :param ai_settings: Objeto de Settings() passao por parametro em Alien()
    :param screen: Objeto de pygame.display.set_mode() passado por parametro em Alien()
    :param aliens_group: grupo de aliens
    :param alien_number: numero de aliens
    :param numero_linhas: numero de linhas possíveis
    """
    # cria um alienígena e coloca n alinha
    alien = Alien(ai_settings, screen)
    largura_alien = alien.rect.width
    # calcula e seta a posição dele na tela
    alien.x = largura_alien + 2 * largura_alien * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * numero_linhas
    # adiciona ao grupo de alienígenas
    aliens_group.add(alien)


def create_fleet(ai_settings, screen, ship_height, aliens_group):
    """
    Cria uma frota de alienígena \n\r
    Utiliza o primeiro criado para calcular a quantidade por linha e o espaçamento \n\r
    :param ai_settings: Objeto da classe Settings
    :param screen: Objeto de retorne de pygame.display.set_mode()
    :param aliens_group: objeto da classe Group() em pygame.sprite
    :param ship_height: Altura na espaço nave
    """
    # este é apenas para ter as medidas
    alien = Alien(ai_settings, screen)
    numero_aliens_x = get_number_aliens_x(ai_settings.screen_width, alien.rect.width)
    numero_aliens_y = get_number_rows(ai_settings.screen_height, ship_height, alien.rect.height)

    # para cada linha de alien
    for numero_y in range(numero_aliens_y):
        # cria um alien para cada espaço de alien disponível
        for numero_x in range(numero_aliens_x):
            create_alien(ai_settings, screen, aliens_group, numero_x, numero_y)


def check_fleet_bordas(ai_settings, aliens_group):
    """
    Verifica se algum alien do group encostou na borda \n\r
    :param ai_settings: Objeto da classe Settings()
    :param aliens_group: Objeto da class pygame.sprite.Group()
    """
    for alien in aliens_group.sprites():
        if alien.check_bordas():
            mudar_direcao_fleet(ai_settings, aliens_group)
            break


def mudar_direcao_fleet(ai_settings, aliens_group):
    """
    Faz toda a tropa descer e muda a direção \n\r
    :param ai_settings: Objeto da classe Settings()
    :param aliens_group: Objeto da classe pygame.sprite.Group()
    """
    # para cada alien desce a altura de settings
    for alien in aliens_group.sprites():
        alien.rect.y += ai_settings.fleet_alien_drop_speed

    # muda a direção de config
    ai_settings.fleet_alien_direction *= -1


def update_aliens(ai_settings, game_stats, screen, ship, aliens_group, bullets_group):
    """
    Atualiza a posição dos aliens do grupo de aliens \n\r
    Chamada de método para verifica se algum alien encostou nas bordas \n\r
    Chamada de método para colisão de nave com alien \n\r

    :param ai_settings: Objeto da classe Settings
    :param game_stats: possui dados estatisticos do jogo, do tipo GameStats()
    :param screen: Objeto de retorne de pygame.display.set_mode()
    :param ship: Espaçonave do jogo. Objeto da classe Ship()
    :param aliens_group: Objeto do tipo pygame.sprite.Group()
    :param bullets_group: Grupo de projéteis Objeto de pygame.sprite.Group()
    """
    # verifica se chegou na borda
    check_fleet_bordas(ai_settings, aliens_group)
    # atualiza a posição de cada alien no grupo
    aliens_group.update()

    # verifica se houve colisão entre a nave ou qualquer alien do grupo
    if pygame.sprite.spritecollideany(ship, aliens_group):
        ship_hit(ai_settings, game_stats, screen, ship, aliens_group, bullets_group)

    # Verifica se alguma alien atingiu o bottom da tela
    check_alien_bottom(ai_settings, game_stats, screen, ship, aliens_group, bullets_group)


def ship_hit(ai_settings, game_stats, screen, ship, aliens_group, bullets_group):
    """
    Responde quando uma espaçonave é atingida/encosta em um alien \n\r
    Reduzindo a quantidade de tentativas, reiniciando a frota de aliens e limpando os projéteis \n\r
    Coloca um tempo de espera antes de reiniciar o jogo \n\r
    :param ai_settings: Configurações do jogo, objeto de Settings()
    :param game_stats: Estatísticas do jogo, objeto da classe GameStats()
    :param screen: Objeto de retorne de pygame.display.set_mode()
    :param ship: Espaçonave do jogo. Objeto da classe Ship()
    :param aliens_group: Objeto do tipo pygame.sprite.Group()
    :param bullets_group: Grupo de projéteis Objeto de pygame.sprite.Group()
    """
    if game_stats.ships_left > 0:
        # decrementa a quantidade de tentativas
        game_stats.ships_left -= 1

        # limpa os aliens e projéteis
        aliens_group.empty()
        bullets_group.empty()

        # cria uma frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship.rect.height, aliens_group)
        ship.center_ship()

        # faz uma pausa
        sleep(0.5)
    else:
        game_stats.game_active = False


def check_alien_bottom(ai_settings, game_stats, screen, ship, aliens_group, bullets_group):
    """
    Verifica se algum alien encostou na parte inferior da tela \n\r
    Ao encostar, chama mesmo método de colisão de alien com a espaçonave \n\r
    :param ai_settings: Configurações do jogo, objeto de Settings()
    :param game_stats: Estatísticas do jogo, objeto da classe GameStats()
    :param screen: Objeto de retorne de pygame.display.set_mode()
    :param ship: Espaçonave do jogo. Objeto da classe Ship()
    :param aliens_group: Objeto do tipo pygame.sprite.Group()
    :param bullets_group: Grupo de projéteis Objeto de pygame.sprite.Group()
    """
    # pega o retangulo da tela
    screen_rect = screen.get_rect()

    # verifica em cada alien o bottom com o bottom da tela
    for alien in aliens_group.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # mesmo quando nave atinge alien
            ship_hit(ai_settings, game_stats, screen, ship, aliens_group, bullets_group)
