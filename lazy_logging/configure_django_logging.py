from .logger_factory import logger_factory
from django.conf import settings


def optional_setting(name: str):
    if hasattr(settings, name):
        return getattr(settings, name)
    else:
        return None


def configure_django_logging(logger_name=None, level='INFO', json_stdout=False, json_file=True) -> None:

    log_dir = optional_setting('LOG_DIR')
    log_file = optional_setting('LOG_FILE')
    log_fmt = optional_setting('LOG_FMT')
    append_pid = optional_setting('LOG_APPEND_PID')

    if logger_name:
        app_names = [logger_name, ]
    else:
        app_names = ['', 'django', *settings.INSTALLED_APPS]

    for app in app_names:
        logger_factory(logger_name=app, message_type=app, level=level,
                       json_stdout=json_stdout, json_file=json_file,
                       log_dir=log_dir, log_file=log_file,
                       append_pid=append_pid, fmt=log_fmt)
