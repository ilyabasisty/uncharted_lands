import config.settings.base_settings as settings
import json


class BaseConfig():

    def config_init(self):
        if settings.DEBUG:
            print('-- Config init --')
        settings.WINDOW_DATA = self.setting_load(settings.WINDOW_JSON_PARAMS)

        self.set_window_params(settings.WINDOW_DATA)

# base json methods
    @staticmethod
    def setting_load(url):
        with open(url, 'r') as read:
            save = json.load(read)
        if settings.DEBUG:
            print('- setting load -')
        return save

    @staticmethod
    def setting_dump(url, data):
        with open(url, 'w') as write:
            json.dump(data, write)
        if settings.DEBUG:
            print('- setting dump -')

# params parse methods
    @staticmethod
    def set_window_params(data):
        settings.TITLE = data['title']
        settings.WIDTH = data['screen']['width']
        settings.HEIGHT = data['screen']['height']
        settings.FPS = data['fps']
        settings.FULLSCREEN = data['fullscreen']
