import config.settings.base_settings as settings
from config.config_manage import check_debug
import pygame


class Front:

    @staticmethod
    def front_init():
        pygame.init()
        check_debug('Front init', 2)
        if settings.FULLSCREEN:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        else:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)

    @staticmethod
    def game_exit():
        check_debug('Main game loop is over', 3)
        settings.MAIN_LOOP = False
        exit()

    def game_loop(self):
        check_debug('Main game loop is start', 3)
        while settings.MAIN_LOOP:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.game_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.game_exit()
