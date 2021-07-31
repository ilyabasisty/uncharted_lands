import config.settings.base_settings as settings
from config.config_manage import check_debug
from front.other.choice import add_choice
import pygame

from back.base.button import Button
from back.base.loop import Loop


class Setting():

    def __init__(self):
        pygame.init()
        check_debug('Setting init', 'INIT', 1)
        settings.SCREEN.fill((150,150,150))
        self.clock = pygame.time.Clock()

        self.back_button = None
        self.fullscreen_button = None    

        self.loop = None
    
    def to_menu(self):
        settings.MENU_LOOP = True
        settings.SETTINGS_LOOP = False
        self.loop.stop()
    
    @staticmethod
    def switch_fullscreen():
        settings.FULLSCREEN = not settings.FULLSCREEN
        check_debug(f'Set fullscreen: {settings.FULLSCREEN}', 'SETTING')
        if settings.FULLSCREEN:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT), pygame.FULLSCREEN)
        else:
            settings.SCREEN = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
    
    def set_fullscrean(self):
        if add_choice('Подтвердить изменения ?', 600):
            self.switch_fullscreen()
            self.update()

    def update(self):
        self.back_button = Button((100,100,100), settings.WIDTH/2-100, settings.HEIGHT-100, 200, 50, 'Назад')
        self.fullscreen_button = Button((100,100,100), 50, 50, 300, 50, 'Полный экран')

    def setting_loop(self):
        self.update()
        check_debug('Setting loop is start', 'BASE', 1)
        self.loop = Loop(
            loop_name=settings.SETTINGS_LOOP,
            update=self.update,
            exit_name="to_menu",
            funcs={
                "to_menu": self.to_menu,
                "set_fullscrean": self.set_fullscrean
            },
            buttons={
                "to_menu": self.back_button,
                "set_fullscrean": self.fullscreen_button
            },
        )
        self.loop.run()
        
        check_debug('Setting loop is over', 'BASE', 1)
