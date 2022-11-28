from celery import shared_task
from celery.utils.log import get_task_logger

from bookmaker.rapid_api import (
    get_next_matches_and_save_to_db,
    get_odds_and_update_matches_on_db,
    get_results_and_update_matches_on_db,
)

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
        get_next_matches_and_save_to_db()
    except Exception as e:
        logger.info("Next matches exception,", e)


@shared_task
def odds():
    logger.info("Getting odds")
    try:
        get_odds_and_update_matches_on_db()
    except Exception as e:
        logger.info("Odds exception,", e)


@shared_task
def results():
    logger.info("Getting results")
    try:
        get_results_and_update_matches_on_db()
    except Exception as e:
        logger.info("Results exception,", e)
