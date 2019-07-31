from .logger_factory import logger_factory
try:
    from .configure_django_logging import configure_django_logging
except ModuleNotFoundError:
    pass  # so we can use logger_factory without django installed

name = "lazy_logging"

__all__ = (
    'name',
    'logger_factory',
    'configure_django_logging',
)
