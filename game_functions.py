import pygame


def update_screen(ttt_settings, screen):
    screen.fill(ttt_settings.bg_color)

    pygame.display.flip()
