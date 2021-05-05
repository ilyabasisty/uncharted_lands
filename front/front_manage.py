import config.settings.base_settings as settings
import pygame


class Front:

    @staticmethod
    def front_init():
        pygame.init()
        if settings.DEBUG:
            print('-- Front init --')
        if settings.FULLSCREEN:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        else:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)

    @staticmethod
    def game_exit():
        if settings.DEBUG:
            print('--- Main game loop is over ---')
        settings.MAIN_LOOP = False
        exit()

    def game_loop(self):
        if settings.DEBUG:
            print('--- Main game loop is start ---')
        while settings.MAIN_LOOP:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.game_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.game_exit()
