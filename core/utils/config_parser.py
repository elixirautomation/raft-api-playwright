import configparser
import os


cur_path = os.path.abspath(os.path.dirname(__file__))
config_file = os.path.join(cur_path, r"../../config.ini")


def get_config(section, key) -> str:
    config = configparser.ConfigParser()
    config.read(config_file)
    return config.get(section=section, option=key)


def get_endpoint(key) -> str:
    return get_config("EndPoints", key)


def set_config(section, key, value):
    config = configparser.ConfigParser()
    config.read(config_file)
    config.set(section=section, option=key, value=value)
    with open(config_file, "w") as configfile:
        config.write(configfile)
