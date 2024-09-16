import logging
from colorlog import ColoredFormatter
# ---------------------------------------------#
# Logging configuration
LOG_LEVEL = logging.DEBUG
# Include date and time in the log format
LOGFORMAT = "%(log_color)s[yumParty Bot]%(reset)s[%(log_color)s%(levelname)s%(reset)s] %(asctime)s %(log_color)s%(message)s%(reset)s"
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(
    LOGFORMAT, "%Y-%m-%d %H:%M:%S"
)  # Specify the date/time format
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger("pythonConfig")
log.setLevel(LOG_LEVEL)
log.addHandler(stream)
# End of configuration
# ---------------------------------------------#
