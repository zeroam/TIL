import logging
import logging.handlers
import logging.config
from logging import StreamHandler


class CustomStreamHandler(StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream)

    def emit(self, record):
        msg = self.format(record)
        print(f"Custom: {msg}")


# add to logging.handlers
logging.handlers.CustomStreamHandler = CustomStreamHandler


logging.config.fileConfig(fname="file.conf", disable_existing_loggers=False)

# Get the logger specified in the filr
print(f"__name__: {__name__}")
logger = logging.getLogger(__name__)

sample_logger = logging.getLogger("sampleLogger")

logger.debug("This is a debug message")
sample_logger.debug("This is sample logger message")
