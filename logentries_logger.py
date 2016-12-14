import logging
import os
from logentries import LogentriesHandler

logger = logging.getLogger('logentries')
logger.setLevel(logging.INFO)

if os.environ.get('LOGENTRIES_TOKEN') is not None:
    logentry_handler = LogentriesHandler(os.environ.get('LOGENTRIES_TOKEN'))
    logger.addHandler(logentry_handler)
else:
    logger.addHandler(logging.StreamHandler())
