import logging
import logging.config


class Logging:
    def __init__(self):
        pass

    @staticmethod
    def init_logging(log_config_path):
        logging.config.fileConfig(log_config_path)

    @staticmethod
    def get_default_logger():
        return logging.getLogger()
