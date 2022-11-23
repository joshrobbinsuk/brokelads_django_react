from .celery import app as celery_app

__all__ = ("celery_app",)

# setting celery beat scheduler (cron) and matching timestrings (use to tell front end when match results will next be updated) in the same place.
# investigate ways to generate one programatically from the other.
CRON_RESULTS_MINUTE = '*/30'
CRON_RESULTS_HOUR = '14,15,16,17,18,19,20,21,22'
CRON_RESULTS_EQUIVALENT_TIME_STRINGS = [
    "14:00:00",
    "14:30:00",
    "15:00:00",
    "15:30:00",
    "16:00:00",
    "16:30:00",
    "17:00:00",
    "17:30:00",
    "18:00:00",
    "18:30:00",
    "19:00:00",
    "19:30:00",
    "20:00:00",
    "20:30:00",
    "21:00:00",
    "21:30:00",
    "22:00:00",
    "22:30:00",
]
