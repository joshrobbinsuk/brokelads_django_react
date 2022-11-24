from django.test import TestCase
from decimal import Decimal
from datetime import datetime

from bookmaker.services import place_bet

from bookmaker.exceptions import MatchHasStartedError, InsufficientBalanceError
from bookmaker.models import Match, TransactionRecord
from account.models import CustomerUser


class PlaceBetTestCase(TestCase):
    fixtures = ['user', 'match']

    def test_place_bet(self):
        # test user with default balance
        user = CustomerUser.objects.get(pk=1)
        self.assertEqual(user.balance, Decimal('100.00'))
        # test bo bets on match
        match = Match.objects.get(pk=4)
        self.assertEqual(len(match.bet_set.all()), 0)
        # user bets on match
        place_bet(user=user, match_id=match.id, choice="HOME", stake="55", returns="30")
        # test bet created
        match = Match.objects.get(pk=4)
        bet = match.bet_set.all()[0]
        self.assertEqual(bet.user.id, 1)
        self.assertEqual(bet.stake, Decimal('55.00'))
        # test transaction created
        transaction = TransactionRecord.objects.get(bet=bet)
        self.assertEqual(transaction.user_balance_before, Decimal('100.00'))
        self.assertEqual(transaction.user_balance_after, Decimal('45.00'))
        # test user balance updated
        user = CustomerUser.objects.get(pk=1)
        self.assertEqual(user.balance, Decimal('45.00'))


class TestPlaceBetErrors(TestCase):
    fixtures = ['user', 'match']

    def test_place_bet_on_match_has_started(self):
        with self.assertRaises(MatchHasStartedError):
            user = CustomerUser.objects.get(pk=1)
            match = Match.objects.get(pk=5)
            place_bet(
                user=user, match_id=match.id, choice="HOME", stake="10", returns="30"
            )

    def test_place_bet_with_insufficient_balance(self):
        with self.assertRaises(InsufficientBalanceError):
            user = CustomerUser.objects.get(pk=1)
            match = Match.objects.get(pk=4)
            place_bet(
                user=user, match_id=match.id, choice="HOME", stake="999", returns="30"
            )
