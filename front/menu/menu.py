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

    def switch_scene(self, scene_key):
        settings.MENU_LOOP = False
        settings.SETTINGS_LOOP = False
        settings.PRE_GAME_LOOP = False
        settings.GAME_LOOP = False
        if scene_key == 'Main':
            settings.MENU_LOOP = True
        elif scene_key == 'Settings':
            settings.SETTINGS_LOOP = True
        elif scene_key == 'PreGame':
            settings.PRE_GAME_LOOP = True
        elif scene_key == 'Game':
            settings.GAME_LOOP = True
        elif scene_key == 'Exit':
            settings.MENU_LOOP = False
            settings.MAIN_LOOP = False
        self.loop.stop()

    def menu_exit(self):
        if add_choice('Выйти из игры ?', 500):
            self.switch_scene('Exit')
            check_debug('GAME EXIT !', 'ALERT')
    
    def to_setting(self):
        self.switch_scene('Settings')

    def to_new_game(self):
        self.switch_scene('PreGame')
    
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
