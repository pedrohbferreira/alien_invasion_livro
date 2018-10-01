import sys
import pygame

from settings import Settings


def run_game():
    # Inicia o jogo e cria um objeto para a tela
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Inicia o laço principal do jogo
    # neste onde ocorre todos os eventos
    while True:

        # realiza escuta de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # seta a cor na tela
        screen.fill(ai_settings.bg_color)
            
        # Atualiza a tela, deixando a tela mais recente visivel
        pygame.display.flip()


run_game()
