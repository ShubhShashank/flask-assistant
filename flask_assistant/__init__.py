import logging

logger = logging.getLogger('flask_assistant')
logger.addHandler(logging.StreamHandler())
if logger.level == logging.NOTSET:
    logger.setLevel(logging.INFO)


from flask_assistant.core import (
    Assistant,
    context_manager
)

from flask_assistant.luis.luis import Bot
from flask_assistant.luis.connector import reply
from flask_assistant.luis.data_store import DataStore

from flask_assistant.response import ask, tell
from flask_assistant.manager import Context
