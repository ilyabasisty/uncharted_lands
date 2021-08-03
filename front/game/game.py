import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import check_debug, get_json_text

from front.other.choice import add_choice
from front.other.info import add_info
import pygame

from back.base.button import Button
from back.generation import world_map, local_map


class Game():

    def __init__(self):
        pygame.init()
        check_debug('Game init', 'INIT', 1)
        settings.SCREEN.fill((150, 150, 150))
        self.clock = pygame.time.Clock()

        self.exit_button = None

    @staticmethod
    def game_exit():
        settings.GAME_LOOP = False
        settings.MAIN_LOOP = False
        check_debug('GAME EXIT !', 'ALERT')

    def update(self):
        self.exit_button = Button((100, 100, 100),
                                  settings.WIDTH / 2 - 100, settings.HEIGHT / 2 + 30, 240, 50, 'Выйти')

    def game_loop(self):
        self.update()
        check_debug('Game loop is start', 'BASE', 1)
        world_map.main_world_generator()
        while settings.GAME_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.game_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.game_exit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.check(mouse):
                        if add_choice('Выйти из игры ?', 500):
                            self.game_exit()
                if ev.type == pygame.MOUSEMOTION:
                    if self.exit_button.check(mouse):
                        self.exit_button.color = (120, 120, 120)
                    else:
                        self.update()

            settings.SCREEN.fill((150, 150, 150))
            self.exit_button.draw(settings.SCREEN)

            pygame.display.update()
            self.clock.tick(settings.FPS)

        check_debug('Game loop is over', 'BASE', 1)
