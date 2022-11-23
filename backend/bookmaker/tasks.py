from celery import shared_task
from celery.utils.log import get_task_logger

from bookmaker.rapid_api import get_next_matches, get_odds, get_results

logger = get_task_logger(__name__)


@shared_task
# beat task test
def task_test():
    logger.info("Task test log")
    return "return test"


@shared_task
def next_matches():
    logger.info("Getting next matches")
    try:
        get_next_matches()
    except Exception as e:
        logger.info("Next matches exception,", e)


@shared_task
def odds():
    logger.info("Getting odds")
    try:
        get_odds()
    except Exception as e:
        logger.info("Odds exception,", e)


@shared_task
def results():
    logger.info("Getting results")
    try:
        get_results()
    except Exception as e:
        logger.info("Results exception,", e)
