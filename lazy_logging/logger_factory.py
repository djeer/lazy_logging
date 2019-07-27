import logging
import os
from logging.handlers import TimedRotatingFileHandler
import time

from .log_colorlog_formatter import ColoredFormatter
from .log_json_formatter import LogstashFormatter


def logger_factory(logger_name: str = '', message_type: str = 'lazy_logs', level='INFO', fmt=None, json_stdout=False,
                   json_file=True, log_dir: str = None, log_file: str = None, append_pid: bool = True,
                   propagate: bool = False):
    # formatters
    json_formatter = LogstashFormatter(
        message_type=message_type,
        tags=[log_file] if log_file else '',
        force_string=True,
        ensure_ascii=False,
        extra_prefix='x'
    )

    fmt = fmt if fmt else '%(cyan)s%(asctime)s %(funcName)s %(lineno)d %(log_color)s %(message)s'
    colored_formatter = ColoredFormatter(fmt)
    colored_formatter.converter = time.gmtime

    # handlers
    stdout_handler = logging.StreamHandler()
    if json_stdout:
        stdout_handler.setFormatter(json_formatter)
    else:
        stdout_handler.setFormatter(colored_formatter)
    stdout_handler.setLevel(level)

    # loggers
    app_logger = logging.getLogger(logger_name)
    app_logger.setLevel(level)
    app_logger.addHandler(stdout_handler)
    app_logger.propagate = propagate

    if not log_file:
        return app_logger
    # file handler
    # should we append pid to filename?
    if append_pid:
        log_path = f'{log_file}_{os.getpid()}.log'
    else:
        log_path = f'{log_file}.log'

    if log_dir:
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, log_path)

    file_handler = TimedRotatingFileHandler(log_path, when='midnight', encoding='utf8')
    if json_file:
        file_handler.setFormatter(json_formatter)
    else:
        file_handler.setFormatter(colored_formatter)
    app_logger.addHandler(file_handler)
    return app_logger
