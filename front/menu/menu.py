import config.settings.base_settings as settings
from config.config_manage import check_debug
import pygame

from back.base.button import Button


class Menu:
    clock = pygame.time.Clock()

    @staticmethod
    def menu_init():
        pygame.init()
        check_debug('Menu init', 1)
        settings.SCREEN.fill((150,150,150))
        pygame.display.set_caption(settings.TITLE + ": Menu")
    
    @staticmethod
    def menu_exit():
        settings.MENU_LOOP = False
        settings.MAIN_LOOP = False
    
    @staticmethod
    def to_setting():
        settings.SETTINGS_LOOP = True
        settings.MENU_LOOP = False

    def menu_loop(self):
        setting_button = Button((100,100,100), settings.WIDTH/2-100, settings.HEIGHT/2-50, 240, 50, 'Настройки')
        exit_button = Button((100,100,100), settings.WIDTH/2-100, settings.HEIGHT/2+30, 240, 50, 'Выйти')

        check_debug('Menu loop is start', 1)
        while settings.MENU_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.menu_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.menu_exit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button.check(mouse):
                        self.menu_exit()
                    if setting_button.check(mouse):
                        self.to_setting()


            settings.SCREEN.fill((150,150,150))
            exit_button.draw(settings.SCREEN)
            setting_button.draw(settings.SCREEN)
            pygame.display.update()
            self.clock.tick(settings.FPS)
        
        check_debug('Menu loop is over', 1)
