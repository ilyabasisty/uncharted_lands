import config.settings.base_settings as settings
from config.config_manage import check_debug
import pygame

from front.menu.menu import Menu
from front.setting.setting import Setting


class Front():

    def __init__(self):
        pygame.init()
        check_debug('Front init', 'INIT', 2)
        if settings.FULLSCREEN:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        else:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        settings.SCREEN.fill((100,100,100))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()

    @staticmethod
    def game_exit():
        settings.MAIN_LOOP = False
        exit()

    def game_loop(self):
        menu = Menu()
        setting = Setting()

        check_debug('Main game loop is start', 'CORE', 3)
        while settings.MAIN_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.game_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.game_exit()
            
            if settings.MENU_LOOP: menu.menu_loop()
            if settings.SETTINGS_LOOP: setting.setting_loop()
            settings.SCREEN.fill((100,100,100))
            pygame.display.update()
            self.clock.tick(settings.FPS)
        
        check_debug('Main game loop is over', 'CORE', 3)
