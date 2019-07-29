from logging import Logger

from .logger_factory import logger_factory
from django.conf import settings


def optional_setting(name: str, default=None):
    if hasattr(settings, name):
        return getattr(settings, name)
    else:
        return default


def configure_django_logging(logger_name=None, level='INFO', is_command=False) -> Logger:

    log_dir = optional_setting('LOG_DIR')
    log_file = optional_setting('LOG_FILE')
    log_fmt = optional_setting('LOG_FMT')
    json_stdout = optional_setting('LOG_JSON_STDOUT', default=False)
    json_file = optional_setting('LOG_JSON_FILE', default=True)
    append_pid = optional_setting('LOG_APPEND_PID', default=is_command)

    if logger_name:
        app_names = [logger_name, ]
    else:
        app_names = ['', *settings.INSTALLED_APPS, 'django']

    for app in app_names:
        logger = logger_factory(logger_name=app, message_type=app, level=level,
                       json_stdout=json_stdout, json_file=json_file,
                       log_dir=log_dir, log_file=log_file,
                       append_pid=append_pid, fmt=log_fmt)

    return logger  # <logger_name> or django
