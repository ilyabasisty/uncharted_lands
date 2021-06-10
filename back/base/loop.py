import config.settings.base_settings as settings
import pygame


class Loop:

    def __init__(self, loop_name, update, exit_name, funcs, buttons, back_img):
        pygame.init()
        settings.SCREEN.fill((150, 150, 150))
        self.clock = pygame.time.Clock()

        self.loop_name = loop_name
        self.update = update
        self.exit = exit_name
        self.funcs = funcs
        self.buttons = buttons
        self.back_img = back_img

    def stop(self):
        self.loop_name = False

    def run(self):
        self.update()
        while self.loop_name:
            for ev in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                if ev.type == pygame.QUIT:
                    self.funcs[self.exit]()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_ESCAPE:
                        self.funcs[self.exit]()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    for key in self.buttons:
                        if self.buttons[key].check(mouse):
                            self.funcs[key]()
            settings.SCREEN.fill((150, 150, 150))
            settings.SCREEN.blit(pygame.image.load(self.back_img), (0, 0))
            for key in self.buttons:
                self.buttons[key].draw(settings.SCREEN)
            pygame.display.update()
            self.clock.tick(settings.FPS)
