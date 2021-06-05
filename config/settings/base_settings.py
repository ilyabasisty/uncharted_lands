# core
DEBUG = True
MAIN_LOOP = True


# loops
MENU_LOOP = True
SETTINGS_LOOP = False
PRE_GAME_LOOP = False

CHOICE_LOOP = False
INFO_LOOP = False


# window params
TITLE = None
WIDTH = None
HEIGHT = None
FPS = None
FULLSCREEN = None


# preset params
PRESET_LOAD = False
PRESET_LIST = {
    'SIZE': None,
    'CHALLENGE': None,
    'FOLK': None,
    'ENVIRONMENT': None
}
PRESET = {
    "size": None,
    "challenge": None,
    "folk": None,
    "environment": None
}


# pygame params
SCREEN = None


# data
WINDOW_DATA = None
PRESET_DATA = None


# console colors
CONS_COLOR = {
    'BASE': '\033[0;37m',
    'ENDLINE': '\033[0;0m',
    'INIT': '\033[0;32m',
    'ALERT': '\033[1;31m',
    'SETTING': '\033[2;33m',
    'CORE': '\033[1;35m',
    'EVENT': '\033[1;36m'
}
