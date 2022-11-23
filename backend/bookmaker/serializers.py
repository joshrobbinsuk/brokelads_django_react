from rest_framework import serializers

from account.models import CustomerUser
from bookmaker.models import Match, Bet


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ("balance", "email")


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "home_team",
            "home_team_logo",
            "away_team",
            "away_team_logo",
            "venue",
            "datetime",
            "id",
            "home_odds",
            "away_odds",
            "draw_odds",
        )


class BetSerializer(serializers.ModelSerializer):
    match = MatchSerializer(
        read_only=True,
    )
    match_id = serializers.PrimaryKeyRelatedField(
        queryset=Match.objects.all(), required=False
    )

    class Meta:
        model = Bet
        fields = ("match_id", "choice", "stake", "returns", "match")
