import sys
import logging
import logging.config

def configure_logging(config_path="logging.conf"):
    logging.config.fileConfig(config_path, disable_existing_loggers=False)

