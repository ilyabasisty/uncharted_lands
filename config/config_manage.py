import config.settings.base_settings as settings
import config.settings.json_path as json_path
import json


def check_debug(massage, color_type='BASE', status=0):
    if settings.DEBUG:
        print(settings.CONS_COLOR[color_type] + '-'*status + ' ' + massage + ' ' + '-'*status + settings.CONS_COLOR['ENDLINE'])


def get_json_text(url):
    ex = ReturnJson()
    return ex.return_json_info(url)


class BaseConfig():

    def base_config_init(self):
        check_debug('Config init', 'INIT', 2)
        settings.WINDOW_DATA = self.setting_load(json_path.WINDOW_JSON_PARAMS)
        self.set_window_params(settings.WINDOW_DATA)

# base json methods
    @staticmethod
    def setting_load(url):
        with open(url, 'r', encoding='utf-8') as read:
            save = json.load(read)
        check_debug('setting load', 'SETTING', 1)
        return save

    @staticmethod
    def setting_dump(url, data):
        with open(url, 'w', encoding='utf-8') as write:
            json.dump(data, write, indent=2, ensure_ascii=False)
        check_debug('setting dump', 'SETTING', 1)

# params parse methods
    @staticmethod
    def set_window_params(data):
        settings.TITLE = data['title']
        settings.WIDTH = data['screen']['width']
        settings.HEIGHT = data['screen']['height']
        settings.FPS = data['fps']
        settings.FULLSCREEN = data['fullscreen']

    @staticmethod
    def set_preset_params(data):
        settings.PRESET_LOAD = True
        for key in settings.PRESET_LIST:
            settings.PRESET_LIST[key] = data[key.lower()]

    @staticmethod
    def update_preset(value, key):
        settings.PRESET[key] = value


class ReturnJson(BaseConfig):

    def return_json_info(self, url):
        check_debug('return json: ' + url, 'SETTING')
        data = self.setting_load(url)
        return data['text']
