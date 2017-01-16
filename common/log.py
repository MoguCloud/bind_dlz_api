import logging
from logging.handlers import RotatingFileHandler

from common.config import CONF

rthandler = RotatingFileHandler(CONF.log_path, maxBytes=10 * 1024 * 1024, backupCount=10)

formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
rthandler.setFormatter(formatter)

logging.getLogger('werkzeug').addHandler(rthandler)

LOGGING = logging.getLogger('werkzeug')

if CONF.debug:
    LOGGING.setLevel(logging.DEBUG)
else:
    LOGGING.setLevel(logging.INFO)
