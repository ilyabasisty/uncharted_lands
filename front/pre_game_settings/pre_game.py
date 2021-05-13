import config.settings.base_settings as settings
from config.config_manage import check_debug

from front.other.choice import add_choice
import pygame

from back.base.button import Button


class PreGame():

    def __init__(self):
        pygame.init()
        check_debug('Pre game init', 'INIT', 1)
        settings.SCREEN.fill((150, 150, 150))
        self.clock = pygame.time.Clock()

        self.exit_button = None

    @staticmethod
    def pre_game_exit():
        settings.PRE_GAME_LOOP = False
        settings.MENU_LOOP = True

    def update(self):
        self.exit_button = Button((100, 100, 100),
                                  settings.WIDTH - 250, settings.HEIGHT - 60, 240, 50, 'Выйти')

    def pre_game_loop(self):
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
                        if add_choice('Выйти в меню ?', 500):
                            self.pre_game_exit()
                if ev.type == pygame.MOUSEMOTION:
                    if self.exit_button.check(mouse):self.exit_button.color = (120,120,120)
                    else:
                        self.update()

            settings.SCREEN.fill((150, 150, 150))
            self.exit_button.draw(settings.SCREEN)

            pygame.display.update()
            self.clock.tick(settings.FPS)

        check_debug('Pre game loop is over', 'BASE', 1)
