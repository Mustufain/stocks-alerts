"""Logging module for stocks alerting."""
import logging.config
import os
import json

CONFIG = '{}/log_config.json'.format(os.path.dirname(__file__))
LOG_DIR = '{}/logs'.format(os.path.dirname(__file__))
LOG_FILE = LOG_DIR+'/stocks-alerting.log'


def get_logger():
    """
    Gets logger.
    :return: logger
    """
    logger = logging.getLogger('py4j')
    return logger


def set_config():
    """Sets configuration of the logger."""
    if os.path.exists(CONFIG):
        with open(CONFIG, 'rt') as file:
            config = json.load(file)
        config.setdefault('handlers', {}).setdefault('file', {})[
            'filename'] = LOG_FILE
        logging.config.dictConfig(config)

    else:
        logging.basicConfig(level=logging.INFO)


def initialize():
    """
    Initialize logger.
    :return: logger
    """
    if os.path.exists(LOG_DIR):

        set_config()
        logger = get_logger()

    else:
        os.makedirs(LOG_DIR)
        set_config()
        logger = get_logger()

    return logger
