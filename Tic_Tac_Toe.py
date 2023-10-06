import settings
import pygame
from time import sleep


def run_game():
    pygame.init()
    ttt_settings = settings.Settings()
    screen = pygame.display.set_mode(
        (ttt_settings.screen_width, ttt_settings.screen_height)
    )
    pygame.display.set_caption("井字棋")

    while True:
        sleep(0.001)