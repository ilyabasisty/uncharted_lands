from config.config_manage import BaseConfig
from front.front_manage import Front


if __name__ == '__main__':
    config = BaseConfig()
    config.base_config_init()

    front = Front()

    front.game_loop()
