import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import check_debug


def main_world_generator():
    world_map = {}
    world_map["name"] = "test"
    world_map["world_size"] = settings.PRESET['size']
    world_map["matrix"] = generator_vision_false_matrix()
    print(world_map)


def generator_vision_false_matrix():
    matrix = []
    size = 9 if settings.PRESET['size'] == 'большой' else 5 if settings.PRESET['size'] == 'средний' else 3
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append({"visible": False})
    matrix[size//2][size//2]["visible"] = True
    return matrix
