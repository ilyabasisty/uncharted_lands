import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import BaseConfig, check_debug


def main_world_generator():
    world_map = {}
    world_map["name"] = "test"
    world_map["size"] = settings.PRESET['size']
    world_map["challenge"] = settings.PRESET['challenge']
    world_map["folk"] = settings.PRESET['folk']
    world_map["environment"] = settings.PRESET['environment']

    world_map["matrix"] = generator_vision_base_matrix()
    config = BaseConfig()
    config.setting_dump(json_path.GENER_WORLD_MAP, world_map)


def generator_vision_base_matrix():
    matrix = []
    size = 9 if settings.PRESET['size'] == 'большой' else 5 if settings.PRESET['size'] == 'средний' else 3
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append({"visible": False})
    matrix[size//2][size//2]["visible"] = True
    return matrix
