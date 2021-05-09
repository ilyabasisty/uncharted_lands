from config.config_manage import BaseConfig
from front.front_manage import Front


if __name__ == '__main__':
    config = BaseConfig()
    front = Front()

    front.game_loop()
