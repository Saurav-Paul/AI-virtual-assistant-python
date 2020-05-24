import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(".log",'w'),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger()
