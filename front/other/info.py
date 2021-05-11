import config.settings.base_settings as settings
from config.config_manage import check_debug
import pygame

from back.base.button import Button


def add_info(massage, width=500, height=200):
    settings.INFO_LOOP = True
    info = Info((110, 110, 110), width=width, height=height, text=massage)
    info.draw(settings.SCREEN)
    return info.info_loop()


class Info:

    def __init__(self, color, width, height, text=''):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.width = width
        self.height = height
        self.text = text
        self.color = color

        self.apply_button = None

    @staticmethod
    def info_exit():
        settings.INFO_LOOP = False

    def update(self):
        self.apply_button = Button((100, 100, 100), settings.WIDTH / 2 - 110,
                                   settings.HEIGHT / 2 + self.height / 2 - 60, 220, 50, 'Продолжить')

    def draw(self, win):
        pygame.draw.rect(win, self.color,
                         (settings.WIDTH / 2 - self.width / 2,
                          settings.HEIGHT / 2 - self.height / 2, self.width, self.height))

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (settings.WIDTH / 2 - text.get_width() / 2, settings.HEIGHT / 2 - self.height / 2 + 20))

    def info_loop(self):
        self.update()
        check_debug('Info loop', 'EVENT')
        while settings.INFO_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.info_exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.info_exit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.apply_button.check(mouse):
                        self.info_exit()
                if ev.type == pygame.MOUSEMOTION:
                    if self.apply_button.check(mouse):
                        self.apply_button = Button((120, 120, 120), settings.WIDTH / 2 - 110,
                                                   settings.HEIGHT / 2 + self.height / 2 - 60, 220, 50, 'Продолжить')
                    else:
                        self.update()

            self.apply_button.draw(settings.SCREEN)

            pygame.display.update()
            self.clock.tick(settings.FPS)
