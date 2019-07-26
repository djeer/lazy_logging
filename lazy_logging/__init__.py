from .logger_factory import logger_factory
from .configure_django_logging import configure_django_logging
name = "lazy_logging"

__all__ = (
    'name',
    'logger_factory',
    'configure_django_logging',
)
