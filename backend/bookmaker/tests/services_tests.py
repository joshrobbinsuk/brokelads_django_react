from django.test import TestCase
from decimal import Decimal
from datetime import datetime

from bookmaker.rapid_api import handle_next_fixture, handle_odds, handle_result
from bookmaker.services import place_bet

from bookmaker.exceptions import MatchHasStartedError, InsufficientBalanceError
from bookmaker.models import Match, Bet, TransactionRecord
from account.models import CustomerUser
from .data import (
    original_data,
    results_data,
    odds_data,
    bad_data,
    bad_odds_data,
)


class PlaceBetTestCase(TestCase):
    def setUp(self):
        CustomerUser.objects.create(email="josh@test.com", cognito_uuid="dummy")
        # creates a fixture
        handle_next_fixture(original_data[0])
        handle_next_fixture(original_data[1])
        # adds odds
        match_one = Match.objects.get(api_id=855740)
        match_two = Match.objects.get(api_id=855741)
        handle_odds(match_one, odds_data)
        handle_odds(match_two, odds_data)

    def test_place_bet(self):
        # user with default balance
        user = CustomerUser.objects.get(email="josh@test.com")
        self.assertEqual(user.balance, Decimal('100.00'))
        match = Match.objects.get(api_id=855740)
        # user bets on match
        place_bet(user=user, match_id=match.id, choice="HOME", stake="10", returns="30")
        # bet and transaction created, user balance updated
        bet = Bet.objects.get(user=user)
        transaction = TransactionRecord.objects.get(bet=bet)
        user = CustomerUser.objects.get(email="josh@test.com")
        self.assertEqual(bet.stake, Decimal('10.00'))
        self.assertEqual(transaction.user_balance_before, Decimal('100.00'))
        self.assertEqual(transaction.user_balance_after, Decimal('90.00'))
        self.assertEqual(user.balance, Decimal('90.00'))

    def test_place_bet_on_match_has_started(self):
        with self.assertRaises(MatchHasStartedError):
            user = CustomerUser.objects.get(email="josh@test.com")
            match = Match.objects.get(api_id=855741)
            place_bet(
                user=user, match_id=match.id, choice="HOME", stake="10", returns="30"
            )

    def test_insufficient_balance(self):
        with self.assertRaises(InsufficientBalanceError):
            user = CustomerUser.objects.get(email="josh@test.com")
            match = Match.objects.get(api_id=855740)
            place_bet(
                user=user, match_id=match.id, choice="HOME", stake="999", returns="30"
            )

    def test_lost_bet(self):
        user = CustomerUser.objects.get(email="josh@test.com")
        match = Match.objects.get(api_id=855740)
        # user places losing bet on match
        place_bet(user=user, match_id=match.id, choice="HOME", stake="10", returns="30")
        handle_result(results_data[0])
        bet = Bet.objects.get(user=user)
        user = CustomerUser.objects.get(email="josh@test.com")
        self.assertEqual(bet.outcome, "LOST")
        self.assertEqual(user.balance, Decimal('90.00'))

    def test_won_bet(self):
        user = CustomerUser.objects.get(email="josh@test.com")
        match = Match.objects.get(api_id=855740)
        # user places winning bet on match
        place_bet(user=user, match_id=match.id, choice="DRAW", stake="10", returns="30")
        handle_result(results_data[0])
        bet = Bet.objects.get(user=user)
        transaction = TransactionRecord.objects.get(type="PAYOUT", bet=bet)
        user = CustomerUser.objects.get(email="josh@test.com")
        self.assertEqual(bet.outcome, "WON")
        self.assertEqual(user.balance, Decimal('120.00'))
        self.assertEqual(transaction.user_balance_before, Decimal('90.00'))
        self.assertEqual(transaction.user_balance_after, Decimal('120.00'))
