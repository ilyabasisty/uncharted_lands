import config.settings.base_settings as settings
from config.config_manage import check_debug
import pygame

from front.menu.menu import Menu


class Front:
    clock = pygame.time.Clock()

    @staticmethod
    def front_init():
        pygame.init()
        check_debug('Front init', 2)
        if settings.FULLSCREEN:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        else:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        settings.SCREEN.fill((100,100,100))
        pygame.display.set_caption(settings.TITLE)

    @staticmethod
    def game_exit():
        settings.MAIN_LOOP = False
        exit()

    def game_loop(self):
        menu = Menu()
        menu.menu_init()

        check_debug('Main game loop is start', 3)
        while settings.MAIN_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.game_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.game_exit()
            
            menu.menu_loop()
            settings.SCREEN.fill((100,100,100))
            pygame.display.update()
            self.clock.tick(settings.FPS)
        
        check_debug('Main game loop is over', 3)
