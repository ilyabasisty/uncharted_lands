import config.settings.base_settings as settings
from config.config_manage import check_debug
import pygame

from back.base.button import Button


class Setting:
    clock = pygame.time.Clock()

    @staticmethod
    def setting_init():
        pygame.init()
        check_debug('Setting init', 1)
        settings.SCREEN.fill((120,120,120))
        pygame.display.set_caption(settings.TITLE + ": Setting")
    
    @staticmethod
    def to_menu():
        settings.MENU_LOOP = True
        settings.SETTINGS_LOOP = False

    def setting_loop(self):
        back_button = Button((100,100,100), settings.WIDTH/2-100, settings.HEIGHT-100, 200, 40, 'Назад')
        
        check_debug('Setting loop is start', 1)
        while settings.SETTINGS_LOOP:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.to_menu()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.to_menu()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.check(mouse):
                        self.to_menu()

            

            settings.SCREEN.fill((120,120,120))
            back_button.draw(settings.SCREEN)
            pygame.display.update()
            self.clock.tick(settings.FPS)
        
        check_debug('Setting loop is over', 1)
