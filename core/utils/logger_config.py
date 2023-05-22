import logging
import logging.config
import os


cur_path = os.path.abspath(os.path.dirname(__file__))
logger_config_file = os.path.join(cur_path, r"../../logger_config.ini")


def get_logger(module_name: str) -> logging:
    logging.config.fileConfig(fname=logger_config_file, disable_existing_loggers=False)
    return logging.getLogger(module_name)
