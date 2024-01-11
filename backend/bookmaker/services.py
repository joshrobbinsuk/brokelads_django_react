from django.db import transaction
from datetime import datetime

from bookmaker.utils import now_aware
from bookmaker.models import Match, Bet, TransactionRecord
from bookmaker.exceptions import (
    MatchDoesNotExistError,
    InsufficientBalanceError,
    MatchHasStartedError,
)
from bookmaker.utils import localise_time


def show_next_matches():
    future_matches = Match.objects.filter(datetime__gte=datetime.now())
    return [match for match in future_matches if match.has_odds and not match.result]


@transaction.atomic
def place_bet(user, match_id, choice, stake, returns):
    # todo - validate returns against stake * odds
    try:
        match = Match.objects.get(id=match_id)
    except Match.DoesNotExist:
        raise MatchDoesNotExistError
    if match.datetime < now_aware():
        raise MatchHasStartedError

    new_balance = float(user.balance) - float(stake)
    if new_balance < 0:
        raise InsufficientBalanceError
    else:
        bet = Bet.objects.create(
            user=user, match_id=match_id, choice=choice, stake=stake, returns=returns
        )
        new_balance = "{:.2f}".format(new_balance)
        TransactionRecord.objects.create(
            type=TransactionRecord.Types.BET,
            bet=bet,
            user_balance_before=user.balance,
            user_balance_after=new_balance,
        )
        user.balance = new_balance
        user.save()
        return user.balance


# CHECK WHAT TIME CELERY WILL NEXT UPDATE RESULTS
def check_time_of_next_refresh(refresh_times):
    todays_remaining_refreshes = [
        t for t in sorted(refresh_times) if t > datetime.now().time()
    ]
    index = len(refresh_times) - len(todays_remaining_refreshes)
    try:
        next_refresh = localise_time(refresh_times[index])
    except IndexError:
        next_refresh = localise_time(refresh_times[0])
        next_refresh = f"{next_refresh} (tomorrow)"
    try:
        last_refresh = localise_time(refresh_times[index - 1])
    except IndexError:
        last_refresh = localise_time(refresh_times[len(refresh_times)])
        last_refresh = f"{last_refresh} (yesterday)"
    return last_refresh, next_refresh
