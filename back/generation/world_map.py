import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import BaseConfig, check_debug

import random


def main_world_generator():
    world_map = {}
    world_map["name"] = "test"
    world_map["size"] = settings.PRESET['size']
    world_map["challenge"] = settings.PRESET['challenge']
    world_map["folk"] = settings.PRESET['folk']
    world_map["environment"] = settings.PRESET['environment']

    world_map["matrix"] = generator_vision_base_matrix()

    settings.WORLD_MAP = world_map

    print(settings.WORLD_MAP)

    config = BaseConfig()
    config.setting_dump(json_path.GENER_WORLD_MAP, world_map)


def world_map_local_params(world_map_matrix):
    for line in world_map_matrix:
        for params in line:
            if params["visible"] == True:
                params["visible"] = {
                    "type": random.randint(1,10),
                    "id": settings.WORLD_MAP_ID,
                }
                settings.WORLD_MAP_ID += 1
    return world_map_matrix


def generator_vision_base_matrix():
    matrix = []
    size = 9 if settings.PRESET['size'] == 'большой' else 5 if settings.PRESET['size'] == 'средний' else 3
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append({"visible": False})
    matrix[size//2][size//2]["visible"] = True
    world_map_local_params(matrix)
    return matrix
