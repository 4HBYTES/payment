import logging
import os
from logentries import LogentriesHandler

logger = logging.getLogger('logentries')
logger.setLevel(logging.INFO)

if os.environ.get('LOGENTRIES_TOKEN') is not None:
    formatter = logging.Formatter('%(message)s')

    logentry_handler = LogentriesHandler(os.environ.get('LOGENTRIES_TOKEN'), format=formatter)
    logger.addHandler(logentry_handler)
else:
    logger.addHandler(logging.StreamHandler())
