from django.test import TestCase
from decimal import Decimal
from datetime import datetime

from bookmaker.rapid_api import (
    handle_next_fixture,
    handle_result,
    handle_odds,
    rapid_api_request,
)
from bookmaker.exceptions import (
    RapidApiDataFetchingError,
    RapidApiDataParsingError,
)
from bookmaker.models import Match, Bet, TransactionRecord
from account.models import CustomerUser
from .data import (
    mock_api_response_data,
    mock_api_results_data,
    mock_api_odds_data,
    bad_mock_api_response_data,
    bad_mock_api_odds_data,
)


class CreateFixtureFromParsedApiDataTestCase(TestCase):
    def test_create_fixtures(self):
        # test no matches with relevant api_ids
        non_matches = Match.objects.filter(api_id__in=[855740, 855741])
        self.assertEquals(len(non_matches), 0)
        # api data parsed and fixtures created
        handle_next_fixture(mock_api_response_data[0])
        handle_next_fixture(mock_api_response_data[1])
        # test matches created with correct teams
        match_one = Match.objects.get(api_id=855740)
        match_two = Match.objects.get(api_id=855741)
        self.assertEqual(match_one.home_team, 'Morocco')
        self.assertEqual(match_one.away_team, 'Croatia')
        self.assertEqual(match_two.home_team, 'Germany')
        self.assertEqual(match_two.away_team, 'Japan')


class UpdateFixturesFromParsedApiOddsDataTestCase(TestCase):
    fixtures = ['match']

    def test_update_with_odds(self):
        # test match has no odds
        match = Match.objects.get(pk=1)
        self.assertEqual(match.home_odds, None)
        self.assertEqual(match.draw_odds, None)
        self.assertEqual(match.away_odds, None)
        # parse api odds and update match
        handle_odds(match, mock_api_odds_data)
        match = Match.objects.get(pk=1)
        self.assertEqual(match.home_odds, Decimal('1.80'))
        self.assertEqual(match.draw_odds, Decimal('3.50'))
        self.assertEqual(match.away_odds, Decimal('4.60'))


# todo - test update datetime of fixture


class UpdateResultsBetsAndBalancesFromParsedApiResultsDataTestCase(TestCase):
    fixtures = ['match', "bet", "user"]

    def test_update_match_with_result(self):
        # test match has no result
        match = Match.objects.get(pk=3)
        self.assertEqual(match.result, None)
        # parse api result and update match
        handle_result(mock_api_results_data[0])
        # test match has a result
        match = Match.objects.get(pk=3)
        self.assertEqual(match.result, Bet.BetChoices.DRAW)

    def test_update_bets_with_results(self):
        # test two bets -- both bets undecided
        bet1 = Bet.objects.get(pk=1)
        bet2 = Bet.objects.get(pk=2)
        self.assertEqual(bet1.outcome, Bet.Outcomes.UNDECIDED)
        self.assertEqual(bet2.outcome, Bet.Outcomes.UNDECIDED)
        # parse api result and update match
        handle_result(mock_api_results_data[0])
        # test bets have been decided
        bet1 = Bet.objects.get(pk=1, user_id=1)
        bet2 = Bet.objects.get(pk=2, user_id=2)
        self.assertEqual(bet1.outcome, Bet.Outcomes.LOST)
        self.assertEqual(bet2.outcome, Bet.Outcomes.WON)

    def test_user_balance_unchanged_on_lost_bet(self):
        # test user with balance of 100
        user = CustomerUser.objects.get(pk=1)
        self.assertEqual(user.balance, Decimal('100.00'))
        # parse api result and update match
        handle_result(mock_api_results_data[0])
        # test user bet lost
        bet = Bet.objects.get(user_id=1, pk=1)
        self.assertEqual(bet.outcome, Bet.Outcomes.LOST)
        # test user balance unchanged
        user = CustomerUser.objects.get(pk=1)
        self.assertEqual(user.balance, Decimal('100.00'))

    def test_transaction_record_and_new_user_balance_on_won_bet(self):
        # test user with balance of 100
        user = CustomerUser.objects.get(pk=2)
        self.assertEqual(user.balance, Decimal('100.00'))
        # parse api result and update match
        handle_result(mock_api_results_data[0])
        # test users bet wins
        bet = Bet.objects.get(user_id=2, pk=2)
        self.assertEqual(bet.outcome, Bet.Outcomes.WON)
        # test transaction record created
        transaction = TransactionRecord.objects.get(
            bet_id=2, type=TransactionRecord.Types.PAYOUT
        )
        self.assertEqual(transaction.user_balance_before, Decimal('100.00'))
        self.assertEqual(transaction.user_balance_after, Decimal('124.00'))
        # test user balance updated
        user = CustomerUser.objects.get(pk=2)
        self.assertEqual(user.balance, Decimal('124.00'))


class RaiseApiErrorsTestCase(TestCase):
    fixtures = ['match']

    def test_bad_next_fixture_parse(self):
        with self.assertRaises(RapidApiDataParsingError):
            handle_next_fixture(bad_mock_api_response_data[1])

    def test_bad_odds_parse(self):
        with self.assertRaises(RapidApiDataParsingError):
            match = Match.objects.get(api_id=855740)
            handle_odds(match, bad_mock_api_odds_data)

    def test_bad_request(self):
        with self.assertRaises(RapidApiDataFetchingError):
            rapid_api_request("https://api-football-v1.p.rapidapi.com/v3/bad-url", {})
