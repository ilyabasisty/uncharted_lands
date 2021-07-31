import config.settings.base_settings as settings
import config.settings.json_path as json_path
from config.config_manage import check_debug


def main_world_generator():
    map = {}
    map["name"] = "test"
    map["world_size"] = settings.PRESET['size']
    map["matrix"] = generator_vision_false_matrix()
    print(settings.PRESET_LIST)


def generator_vision_false_matrix():
    matrix = []
    size = 9 if settings.PRESET['size'] == 'большой' else 6 if settings.PRESET['size'] == 'средний' else 3
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append({"visible": False})
    return matrix
