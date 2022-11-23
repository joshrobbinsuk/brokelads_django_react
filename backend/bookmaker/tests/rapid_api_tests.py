from django.test import TestCase
from decimal import Decimal
from datetime import datetime

from bookmaker.rapid_api import (
    handle_next_fixture,
    handle_result,
    handle_odds,
    rapid_api_request,
)
from bookmaker.exceptions import RapidApiDataFetchingError, RapidApiDataParsingError
from bookmaker.models import Match
from .data import (
    original_data,
    results_data,
    odds_data,
    bad_data,
    bad_odds_data,
)


class RapidApiTestCase(TestCase):
    def setUp(self):
        handle_next_fixture(original_data[0])
        handle_next_fixture(original_data[1])

    def test_create_fixtures(self):
        match_one = Match.objects.get(api_id=855740)
        match_two = Match.objects.get(api_id=855741)
        self.assertEqual(match_one.home_team, 'Morocco')
        self.assertEqual(match_one.away_team, 'Croatia')
        self.assertEqual(match_two.home_team, 'Germany')
        self.assertEqual(match_two.away_team, 'Japan')

    # todo - test date update

    def test_update_with_odds(self):
        # match has no odds
        match = Match.objects.get(api_id=855740)
        self.assertEqual(match.home_odds, None)
        # match has odds
        handle_odds(match, odds_data)
        match = Match.objects.get(api_id=855740)
        self.assertEqual(match.home_odds, Decimal('1.80'))

    def test_update_with_results(self):
        handle_result(results_data[0])
        handle_result(results_data[1])
        match_one = Match.objects.get(api_id=855740)
        match_two = Match.objects.get(api_id=855741)
        self.assertEqual(match_one.result, 'DRAW')
        self.assertEqual(match_two.result, 'HOME')


class BadRequestTestCase(TestCase):
    def test_bad_request(self):
        with self.assertRaises(RapidApiDataFetchingError):
            rapid_api_request("https://api-football-v1.p.rapidapi.com/v3/bad-url", {})


class BadParseTestCase(TestCase):
    def setUp(self):
        handle_next_fixture(original_data[0])

    def test_bad_next_fixture(self):
        with self.assertRaises(RapidApiDataParsingError):
            handle_next_fixture(bad_data[1])

    def test_bad_odds(self):
        with self.assertRaises(RapidApiDataParsingError):
            match = Match.objects.get(api_id=855740)
            handle_odds(match, bad_odds_data)
