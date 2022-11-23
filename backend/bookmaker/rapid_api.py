from django.conf import settings
from django.db import transaction
import requests

from bookmaker.models import Match, Bet, TransactionRecord
from bookmaker.exceptions import (
    RapidApiDataFetchingError,
    RapidApiDataParsingError,
    NoOddsFixtureWarning,
)

fixtures_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
odds_url = "https://api-football-v1.p.rapidapi.com/v3/odds"

headers = {
    "X-RapidAPI-Key": settings.RAPID_API_KEY,
    "X-RapidAPI-Host": settings.RAPID_API_HOST,
}

next_params = {"league": settings.RAPID_API_LEAGUE_ID, "next": "20"}
last_params = {"league": settings.RAPID_API_LEAGUE_ID, "last": "12"}


def get_next_matches():
    response = rapid_api_request(fixtures_url, next_params)
    for res in response:
        handle_next_fixture(res)


def get_odds():
    # just checking on home odds -- assumption is that
    # all odds are either null or not null
    no_odds_fixtures = Match.objects.filter(home_odds__isnull=True)
    for match in no_odds_fixtures:
        try:
            res = rapid_api_request(odds_url, {"fixture": match.api_id})
            handle_odds(match, res)
        except NoOddsFixtureWarning:
            print(f"*** No odds for {match.home_team} v {match.away_team}")


def get_results():
    response = rapid_api_request(fixtures_url, last_params)
    for res in response:
        handle_result(res)


def handle_next_fixture(res):
    data = rapid_api_parse_fixture(res)
    # check for new datetimes on existing matches
    try:
        match = Match.objects.get(api_id=data['api_id'])
        match.datetime = data["datetime"] = data['datetime']
        match.save()
    # create new match if not in db
    except Match.DoesNotExist:
        Match.objects.create(**data)


def handle_odds(match, res):
    data = rapid_api_parse_odds(res)
    match.home_odds = data['home_odds']
    match.away_odds = data['away_odds']
    match.draw_odds = data['draw_odds']
    match.save()


def handle_result(res):
    data = rapid_api_parse_result(res)
    if data['status'] != "FT":
        print(f"*** match {data['api_id']} is still in play")
    else:
        try:
            match = Match.objects.get(api_id=data['api_id'])
            if match.has_goals:
                print(f"*** {match.home_team} v {match.away_team} has goals already")
            else:
                match.home_goals = data["home_goals"]
                match.away_goals = data["away_goals"]
                match.save()
                update_bets_and_payout(match)
        except Match.DoesNotExist:
            print(f"No match found: {data['api_id']}")


@transaction.atomic
def update_bets_and_payout(match):
    bets = match.bet_set.all()
    for bet in bets:
        if bet.choice == match.result:
            bet.outcome = Bet.Outcomes.WON
            user = bet.user
            TransactionRecord.objects.create(
                type=TransactionRecord.Types.PAYOUT,
                bet=bet,
                user_balance_before=user.balance,
                user_balance_after=user.balance + bet.returns,
            )
            user.balance = user.balance + bet.returns
            user.save()
        else:
            bet.outcome = Bet.Outcomes.LOST
        bet.save()


# BASIC DATA FETCH REQUEST
def rapid_api_request(url, params):
    try:
        response = requests.request("GET", url, headers=headers, params=params)
        data = response.json()
        return data["response"]
    except Exception as e:
        print("Fetch error:", e)
        raise RapidApiDataFetchingError


# DATA PARSING
def rapid_api_parse_fixture(res):
    try:
        data = {}
        fixture = res["fixture"]
        home_team = res["teams"]["home"]
        away_team = res["teams"]["away"]
        data["api_id"] = fixture["id"]
        data["datetime"] = fixture["date"]
        data["home_team"] = home_team["name"]
        data["home_team_logo"] = home_team["logo"]
        data["away_team"] = away_team["name"]
        data["away_team_logo"] = away_team["logo"]
        data["venue"] = fixture["venue"]["name"]
        return data
    except Exception as e:
        raise RapidApiDataParsingError


def rapid_api_parse_odds(res):
    try:
        odds_set = res[0]["bookmakers"][0]["bets"][0]["values"]
    except IndexError as e:
        raise NoOddsFixtureWarning
    try:
        data = {}
        for odds in odds_set:
            if odds["value"] == "Home":
                data['home_odds'] = odds["odd"]
            if odds["value"] == "Away":
                data['away_odds'] = odds["odd"]
            if odds["value"] == "Draw":
                data['draw_odds'] = odds["odd"]
        return data
    except Exception as e:
        print("Parse error:", e)
        raise RapidApiDataParsingError


def rapid_api_parse_result(res):
    try:
        data = {}
        fixture = res["fixture"]
        goals = res["goals"]
        data['status'] = fixture['status']['short']
        data["api_id"] = fixture["id"]
        data['home_goals'] = goals["home"]
        data['away_goals'] = goals["away"]

        return data
    except Exception as e:
        print("Parse error:", e)
        raise RapidApiDataParsingError
