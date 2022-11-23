from django.db import models
from django_extensions.db.models import TimeStampedModel


from account.models import CustomerUser
from bookmaker import utils


class Match(models.Model):
    api_id = models.IntegerField()
    datetime = models.DateTimeField()

    venue = models.CharField(max_length=255)
    home_team = models.CharField(max_length=255)
    home_team_logo = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    away_team_logo = models.CharField(max_length=255)

    home_odds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    away_odds = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    draw_odds = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    home_goals = models.IntegerField(null=True)
    away_goals = models.IntegerField(null=True)

    voided = models.BooleanField(default=False)
    voided_message = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.home_team} v {self.away_team}"

    @property
    def has_odds(self):
        return (
            (self.home_odds is not None)
            and (self.away_odds is not None)
            and (self.draw_odds is not None)
        )

    @property
    def has_goals(self):
        return (self.home_goals is not None) and (self.away_goals is not None)

    @property
    def result(self):
        if not self.has_goals:
            return None
        if self.home_goals > self.away_goals:
            return Bet.BetChoices.HOME
        if self.away_goals > self.home_goals:
            return Bet.BetChoices.AWAY
        return Bet.BetChoices.DRAW

    # ** TODO: has started

    class Meta:
        verbose_name_plural = "Matches"
        ordering = ('datetime',)


class Bet(TimeStampedModel):
    class BetChoices(models.TextChoices):
        HOME = "HOME"
        AWAY = "AWAY"
        DRAW = "DRAW"

    class Outcomes(models.TextChoices):
        UNDECIDED = "UNDECIDED"
        WON = "WON"
        LOST = "LOST"

    match = models.ForeignKey(
        Match,
        on_delete=models.PROTECT,
    )

    user = models.ForeignKey(
        CustomerUser,
        on_delete=models.PROTECT,
    )
    choice = models.CharField(max_length=5, choices=BetChoices.choices)
    stake = models.DecimalField(max_digits=5, decimal_places=2)
    returns = models.DecimalField(max_digits=5, decimal_places=2)

    outcome = models.CharField(
        max_length=10, choices=Outcomes.choices, default=Outcomes.UNDECIDED
    )

    def __str__(self):
        return f"{self.user} - £{self.stake} - {self.choice} - {self.match}  -{utils.localise_datetime(self.match.datetime)}"

    class Meta:
        ordering = ('match__datetime',)


class TransactionRecord(TimeStampedModel):
    class Types(models.TextChoices):
        BET = "BET"
        PAYOUT = "PAYOUT"

    type = models.CharField(max_length=6, choices=Types.choices)
    bet = models.ForeignKey(
        Bet,
        on_delete=models.PROTECT,
    )
    user_balance_before = models.DecimalField(max_digits=5, decimal_places=2)
    user_balance_after = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.bet.user} {self.type} from {self.user_balance_before} to {self.user_balance_after}"

    class Meta:
        ordering = ("created",)
