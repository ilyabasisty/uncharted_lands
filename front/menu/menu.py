import config.settings.base_settings as settings
from config.config_manage import check_debug
from front.other.choice import add_choice
import pygame

from back.base.button import Button


class Menu():

    def __init__(self):
        pygame.init()
        check_debug('Menu init', 'INIT', 1)
        settings.SCREEN.fill((150,150,150))
        self.clock = pygame.time.Clock()

        self.setting_button = None
        self.exit_button = None
    
    @staticmethod
    def menu_exit():
        settings.MENU_LOOP = False
        settings.MAIN_LOOP = False
        check_debug('GAME EXIT !', 'ALERT')
    
    @staticmethod
    def to_setting():
        settings.SETTINGS_LOOP = True
        settings.MENU_LOOP = False
    
    def update(self):
        self.setting_button = Button((100,100,100), settings.WIDTH/2-100, settings.HEIGHT/2-50, 240, 50, 'Настройки')
        self.exit_button = Button((100,100,100), settings.WIDTH/2-100, settings.HEIGHT/2+30, 240, 50, 'Выйти')

    def menu_loop(self):
        self.update()
        check_debug('Menu loop is start', 'BASE', 1)
        while settings.MENU_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.menu_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.menu_exit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.check(mouse):
                        self.menu_exit()
                    if self.setting_button.check(mouse):
                        self.to_setting()
                if ev.type == pygame.MOUSEMOTION:
                    if self.exit_button.check(mouse):
                        self.exit_button = Button((120,120,120), settings.WIDTH/2-100, settings.HEIGHT/2+30, 240, 50, 'Выйти')
                    elif self.setting_button.check(mouse):
                        self.setting_button = Button((120,120,120), settings.WIDTH/2-100, settings.HEIGHT/2-50, 240, 50, 'Настройки')
                    else:
                        self.update()

            settings.SCREEN.fill((150,150,150))
            self.exit_button.draw(settings.SCREEN)
            self.setting_button.draw(settings.SCREEN)
            
            pygame.display.update()
            self.clock.tick(settings.FPS)
        
        check_debug('Menu loop is over', 'BASE', 1)
