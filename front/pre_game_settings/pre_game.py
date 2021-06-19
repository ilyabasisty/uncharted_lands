import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import check_debug, BaseConfig

from front.other.choice import add_choice
import pygame
import functools

from back.base.button import Button
import back.generation.world_map as world_map


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

    @staticmethod
    def pre_game_exit():
        settings.PRE_GAME_LOOP = False
        settings.MENU_LOOP = True

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
            world_map.main_world_generator()

    def load_preset(self):
        if not settings.PRESET_LOAD:
            settings.PRESET_DATA = self.config.setting_load(json_path.PRESET_LIST)
            self.config.set_preset_params(settings.PRESET_DATA)
        width = 0
        for key in settings.PRESET_LIST:
            height = 50
            for el in settings.PRESET_LIST[key]:
                self.preset_buttons[key.lower()].append(Button((100, 100, 100),
                                  20 + width, 10 + height, 240, 50, el.split(':')[0]))
                height += 60
            width += 260

    def update(self):
        self.exit_button = Button((100, 100, 100),
                                  20, settings.HEIGHT - 60, 240, 50, 'Выйти')
        self.start_button = Button((100, 100, 100),
                                  settings.WIDTH - 250, settings.HEIGHT - 60, 240, 50, 'Начать')

    def pre_game_loop(self):
        self.load_preset()
        self.update()
        check_debug('Pre game loop is start', 'BASE', 1)
        while settings.PRE_GAME_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.pre_game_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.pre_game_exit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.check(mouse):
                        self.pre_game_exit()
                    if self.start_button.check(mouse):
                        self.pre_game_start()
                    for key in self.preset_buttons:
                        for button in self.preset_buttons[key]:
                            if button.check(mouse):
                                self.config.update_preset(button.text, key)
                if ev.type == pygame.MOUSEMOTION:
                    if self.exit_button.check(mouse):self.exit_button.color = (120,120,120)
                    if self.start_button.check(mouse):self.start_button.color = (120, 120, 120)
                    else:
                        self.update()

            settings.SCREEN.fill((150, 150, 150))
            self.exit_button.draw(settings.SCREEN)
            self.start_button.draw(settings.SCREEN)
            for key in self.preset_buttons:
                for button in self.preset_buttons[key]:
                    button.draw(settings.SCREEN)

            pygame.display.update()
            self.clock.tick(settings.FPS)

        check_debug('Pre game loop is over', 'BASE', 1)
