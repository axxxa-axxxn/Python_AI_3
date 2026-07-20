import logging

logging.basicConfig(
    filename="hospital.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


class Logger:

    @staticmethod
    def log(message):
        logging.info(message)