import json
import os

__BASE_DIR = os.path.dirname(os.path.dirname(__file__))

"""
    Leemos el archivo de configuraciones y devolvemos como objeto JSON
    :return:
    """
def get_settings():
    with open("{0}/{1}".format(__BASE_DIR, "../settings.json")) as data_file:
        data = json.load(data_file)
    return data