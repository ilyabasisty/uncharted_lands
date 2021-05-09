import config.settings.base_settings as settings
import json


def check_debug(massage, color_type='BASE', status=0):
    if settings.DEBUG:
        print(settings.CONS_COLOR[color_type] + '-'*status + ' ' + massage + ' ' + '-'*status + settings.CONS_COLOR['ENDLINE'])


class BaseConfig():

    def __init__(self):
        check_debug('Config init', 'INIT', 2)
        settings.WINDOW_DATA = self.setting_load(settings.WINDOW_JSON_PARAMS)
        self.set_window_params(settings.WINDOW_DATA)

# base json methods
    @staticmethod
    def setting_load(url):
        with open(url, 'r') as read:
            save = json.load(read)
        check_debug('setting load', 'SETTING', 1)
        return save

    @staticmethod
    def setting_dump(url, data):
        with open(url, 'w') as write:
            json.dump(data, write)
        check_debug('setting dump', 'SETTING', 1)

# params parse methods
    @staticmethod
    def set_window_params(data):
        settings.TITLE = data['title']
        settings.WIDTH = data['screen']['width']
        settings.HEIGHT = data['screen']['height']
        settings.FPS = data['fps']
        settings.FULLSCREEN = data['fullscreen']
