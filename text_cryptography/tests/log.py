import logging

# Create a logger called 'Tester'
test_logger = logging.getLogger('Tester')
test_logger.setLevel(logging.DEBUG)

# Create a file handler which logs even debug messages
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Create a formatter and add it to the handler
formatter_format = "%(asctime)s - %(name)s - %(levelname)s - " + \
    "%(funcName)s - Line: %(lineno)s - %(message)s"
formatter = logging.Formatter(formatter_format)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
test_logger.addHandler(file_handler)
test_logger.addHandler(console_handler)
