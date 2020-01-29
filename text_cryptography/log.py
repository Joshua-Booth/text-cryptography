import logging

# Create a logger called 'Debugger'
debug_logger = logging.getLogger('Debugger')
debug_logger.setLevel(logging.DEBUG)

# Create a file handler which logs even debug messages
file_handler = logging.FileHandler('debug.log')
file_handler.setLevel(logging.DEBUG)

# Create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Create a formatter and add it to the handler
formatter_format = "%(asctime)s - %(name)s - %(levelname)s - " + \
    "%(funcName)s - Line: %(lineno)s - %(message)s"
formatter = logging.Formatter(formatter_format)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
debug_logger.addHandler(file_handler)
debug_logger.addHandler(console_handler)
