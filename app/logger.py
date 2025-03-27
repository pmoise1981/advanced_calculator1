import logging

def setup_logger(name="app", log_level=logging.DEBUG):
    """Sets up a logger with a stream handler and formatted output."""
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Avoid adding multiple handlers if the logger already has them
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

# Initialize logger
logger = setup_logger()

