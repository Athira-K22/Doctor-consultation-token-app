import logging
import os

class CustomFormatter(logging.Formatter):
    def format(self, record):
        # Add folder name (parent directory of the file)
        folder = os.path.basename(os.path.dirname(record.pathname))
        record.folder = folder
        return super().format(record)

# Log format: time | folder | filename:line | level | message
LOG_FORMAT = '%(asctime)s | %(folder)s | %(filename)s:%(lineno)d | %(levelname)s | %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

formatter = CustomFormatter(LOG_FORMAT, DATE_FORMAT)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger_cvgk: logging.Logger = logging.getLogger("customLogger")
logger_cvgk.setLevel(logging.INFO)
logger_cvgk.handlers = []  # Remove other handlers
logger_cvgk.addHandler(handler)
logger_cvgk.propagate = False
