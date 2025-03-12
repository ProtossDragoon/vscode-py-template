import logging


print(__file__)


def hello_world():
    logger = logging.getLogger('myproject')
    logger.info('hello world!')


if __name__ == '__main__':
    from myproject.log_utils import setup_logging
    setup_logging()
    hello_world()
