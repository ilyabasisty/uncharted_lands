import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import check_debug, get_json_text

from front.other.choice import add_choice
from front.other.info import add_info
import pygame

from back.base.button import Button
from back.base.loop import Loop

from back.generation import world_map, local_map


class Game():

    def __init__(self):
        pygame.init()
        check_debug('Game init', 'INIT', 1)
        settings.SCREEN.fill((150, 150, 150))
        self.clock = pygame.time.Clock()

        self.exit_button = None
        self.loop = None

    def game_exit(self):
        if add_choice('Выйти в меню ?', 500):
            settings.GAME_LOOP = False
            settings.MENU_LOOP = True
            self.loop.stop()
            check_debug('GAME EXIT !', 'ALERT')

    def update(self):
        self.exit_button = Button((100, 100, 100),
                                  settings.WIDTH / 2 - 100, settings.HEIGHT - 70, 240, 50, 'Выйти')

    def game_loop(self):
        self.update()
        check_debug('Game loop is start', 'BASE', 1)
        self.loop = Loop(
            loop_name=settings.GAME_LOOP,
            update=self.update,
            exit_name="game_exit",
            autorun={
                "load_world_map": world_map.main_world_generator,
            },
            funcs={
                "game_exit": self.game_exit,
            },
            buttons={
                "game_exit": self.exit_button,
            },
        )
        self.loop.run()

        check_debug('Game loop is over', 'BASE', 1)
