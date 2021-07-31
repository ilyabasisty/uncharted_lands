import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import check_debug, BaseConfig

from front.other.choice import add_choice
import pygame
import functools

from back.base.button import Button
from back.base.loop import Loop


class PreGame():

    def __init__(self):
        pygame.init()
        check_debug('Pre game init', 'INIT', 1)
        settings.SCREEN.fill((150, 150, 150))
        self.clock = pygame.time.Clock()
        self.config = BaseConfig()

        self.exit_button = None
        self.start_button = None
        self.preset_buttons = {
            'size': [],
            'challenge': [],
            'folk': [],
            'environment': []
        }

        self.loop = None

    def pre_game_exit(self):
        settings.PRE_GAME_LOOP = False
        settings.MENU_LOOP = True
        self.loop.stop()

    def pre_game_start(self):
        result = True
        for value in settings.PRESET.values():
            if not value:
                result = False
                check_debug('There are empty parameters', 'ALERT')
                break
        if result:
            self.config.setting_dump(json_path.PRESET, settings.PRESET)
            check_debug('Pre game settings saved', 'EVENT')
            settings.PRE_GAME_LOOP = False
            settings.GAME_LOOP = True
            self.loop.stop()

    def load_preset(self):
        if not settings.PRESET_LOAD:
            settings.PRESET_DATA = self.config.setting_load(json_path.PRESET_LIST)
            self.config.set_preset_params(settings.PRESET_DATA)
        width = 0
        for key in settings.PRESET_LIST:
            height = 50
            for el in settings.PRESET_LIST[key]:
                self.preset_buttons[key.lower()].append(Button((100, 100, 100),
                                  20 + width, 10 + height, 240, 50, el))
                height += 60
            width += 260
    
    def check_preset(self, mouse):
        for key in self.preset_buttons:
            for button in self.preset_buttons[key]:
                if button.check(mouse):
                    self.config.update_preset(button.text, key)

    def blit_preset(self):
        for key in self.preset_buttons:
            for button in self.preset_buttons[key]:
                button.draw(settings.SCREEN)

    def update(self):
        self.exit_button = Button((100, 100, 100),
                                  20, settings.HEIGHT - 60, 240, 50, 'Выйти')
        self.start_button = Button((100, 100, 100),
                                  settings.WIDTH - 250, settings.HEIGHT - 60, 240, 50, 'Начать')

    def pre_game_loop(self):
        self.update()
        check_debug('Pre game loop is start', 'BASE', 1)
        self.loop = Loop(
            loop_name=settings.PRE_GAME_LOOP,
            update=self.update,
            exit_name="pre_game_exit",
            autorun={
                "load_preset": self.load_preset,
            },
            funcs={
                "pre_game_exit": self.pre_game_exit,
                "pre_game_start": self.pre_game_start,
            },
            buttons={
                "pre_game_exit": self.exit_button,
                "pre_game_start": self.start_button,
            },
            mousebuttondown={
                "check_preset": self.check_preset,
            },
            post_for={
                "blit_preset": self.blit_preset,
            },
        )
        self.loop.run()

        check_debug('Pre game loop is over', 'BASE', 1)
