import logging

import pytest

from lazy_logging import logger_factory


def test_dummy():
    logger = logger_factory()
    assert isinstance(logger, logging.Logger)
