from time import perf_counter
from functools import wraps
import logging
from datetime import datetime, date
import os


# Создание папки logs для логов
path = "."
if "logs" not in os.listdir(path):
    os.mkdir(".\\logs")

logger = logging.getLogger(__name__)

log_format = logging.Formatter('[%(asctime)s.%(msecs)03d] %(levelname)6s:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

file_handler = logging.FileHandler(f"logs\\{date.today()}_logs.txt", encoding="utf-8")
file_handler.setFormatter(fmt=log_format)

logging.basicConfig(level=logging.DEBUG, handlers=[file_handler])


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Start {func.__name__} at {datetime.now()}")
        start = perf_counter()
        result = func(*args, **kwargs)
        total = (perf_counter() - start).__round__(4)
        logger.info(f"Finish {func.__name__} at {datetime.now()}")
        logger.info(f"{func.__name__} execution time {total}")
        return result
    return wrapper
