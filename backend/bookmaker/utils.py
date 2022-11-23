import pytz
from django.utils import timezone
from datetime import datetime, date


def localise_datetime(datetime):
    london_tz = pytz.timezone('Europe/London')
    london_time = datetime.astimezone(london_tz)
    return london_time.strftime("%H:%M - %b %e %a")


def localise_time(time):
    today = date.today()
    combined = datetime.combine(today, time)
    return localise_datetime(combined)[0:5]


def now_aware():
    return timezone.now()


def string_to_time(time_str):
    return datetime.strptime(time_str, '%H:%M:%S').time()
