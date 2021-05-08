from config.config_manage import BaseConfig
from front.front_manage import Front


if __name__ == '__main__':
    config = BaseConfig()
    front = Front()

    config.config_init()
    front.front_init()
    front.game_loop()
