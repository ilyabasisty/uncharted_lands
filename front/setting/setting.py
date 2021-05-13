import config.settings.base_settings as settings
from config.config_manage import check_debug
from front.other.choice import add_choice
import pygame

from back.base.button import Button


class Setting():

    def __init__(self):
        pygame.init()
        check_debug('Setting init', 'INIT', 1)
        settings.SCREEN.fill((150,150,150))
        self.clock = pygame.time.Clock()

        self.back_button = None
        self.fullscreen_button = None    
    
    @staticmethod
    def to_menu():
        settings.MENU_LOOP = True
        settings.SETTINGS_LOOP = False
    
    @staticmethod
    def switch_fullscreen():
        settings.FULLSCREEN = not settings.FULLSCREEN
        check_debug(f'Set fullscreen: {settings.FULLSCREEN}', 'SETTING')
        if settings.FULLSCREEN:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        else:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

    def update(self):
        self.back_button = Button((100,100,100), settings.WIDTH/2-100, settings.HEIGHT-100, 200, 50, 'Назад')
        self.fullscreen_button = Button((100,100,100), 50, 50, 300, 50, 'Полный экран')

    def setting_loop(self):
        self.update()
        check_debug('Setting loop is start', 'BASE', 1)
        while settings.SETTINGS_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.to_menu()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.to_menu()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.check(mouse):
                        self.to_menu()
                    if self.fullscreen_button.check(mouse):
                        if add_choice('Подтвердить изменения ?', 600):
                            self.switch_fullscreen()
                            self.update()
                if ev.type == pygame.MOUSEMOTION:
                    if self.back_button.check(mouse):self.back_button.color = (120,120,120)
                    elif self.fullscreen_button.check(mouse):self.fullscreen_button.color = (120,120,120)
                    else:
                        self.update()
            

            settings.SCREEN.fill((150,150,150))
            self.back_button.draw(settings.SCREEN)
            self.fullscreen_button.draw(settings.SCREEN)

            pygame.display.update()
            self.clock.tick(settings.FPS)
        
        check_debug('Setting loop is over', 'BASE', 1)
