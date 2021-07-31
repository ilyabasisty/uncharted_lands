import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import check_debug, get_json_text

from front.other.choice import add_choice
from front.other.info import add_info
import pygame

from back.base.button import Button
from back.base.loop import Loop


class Menu():

    def __init__(self):
        pygame.init()
        check_debug('Menu init', 'INIT', 1)
        settings.SCREEN.fill((150,150,150))
        self.clock = pygame.time.Clock()

        self.new_game_button = None
        self.setting_button = None
        self.exit_button = None

        self.info_game_button = None

        self.loop = None
    
    def menu_exit(self):
        if add_choice('Выйти из игры ?', 500):
            settings.MENU_LOOP = False
            settings.MAIN_LOOP = False
            self.loop.stop()
            check_debug('GAME EXIT !', 'ALERT')
    
    def to_setting(self):
        settings.SETTINGS_LOOP = True
        settings.MENU_LOOP = False
        self.loop.stop()

    def to_new_game(self):
        settings.PRE_GAME_LOOP = True
        settings.MENU_LOOP = False
        self.loop.stop()
    
    def update(self):
        self.new_game_button = Button((100, 100, 100),
                                     settings.WIDTH / 2 - 100, settings.HEIGHT / 2 - 110, 240, 50,'Новая игра')
        self.setting_button = Button((100,100,100),
                                     settings.WIDTH/2-100, settings.HEIGHT/2-50, 240, 50, 'Настройки')
        self.exit_button = Button((100,100,100),
                                  settings.WIDTH/2-100, settings.HEIGHT/2+30, 240, 50, 'Выйти')
        self.info_game_button = Button((100, 100, 100),
                                       settings.WIDTH - 60, settings.HEIGHT - 60, 50, 50, '!')

    def menu_loop(self):
        self.update()
        check_debug('Menu loop is start', 'BASE', 1)
        self.loop = Loop(
            loop_name=settings.MENU_LOOP,
            update=self.update,
            exit_name="menu_exit",
            funcs={
                "menu_exit": self.menu_exit,
                "to_setting": self.to_setting,
                "to_new_game": self.to_new_game,
            },
            buttons={
                "menu_exit": self.exit_button,
                "to_setting": self.setting_button,
                "to_new_game": self.new_game_button,
            },
            back_img="back/data/image/back/menu_back.png"
        )
        self.loop.run()
        
        check_debug('Menu loop is over', 'BASE', 1)
