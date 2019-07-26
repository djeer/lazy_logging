# Example of how settings.py may look
# You can just append it in the end of your settings.py
from lazy_logging import configure_django_logging

LOGGING_CONFIG = None  # we don't use django dictconfig
LOG_FILE = 'myapp'  # remove this line if you don't need file logs
configure_django_logging()
