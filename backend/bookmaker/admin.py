from django.contrib import admin, messages
from django.db.models import Q
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils import timezone
from datetime import datetime

from .models import Match, Bet, TransactionRecord
from bookmaker.rapid_api import (
    get_next_matches_and_save_to_db,
    get_odds_and_update_matches_on_db,
    get_results_and_update_matches_on_db,
    update_match_bets_and_payout,
)
from bookmaker.exceptions import (
    RapidApiDataFetchingError,
    RapidApiDataParsingError,
)
from bookmaker.utils import localise_datetime


@admin.register(Bet)
class Bet(admin.ModelAdmin):
    model = Bet
    search_fields = (
        "match__home_team",
        "match__away_team",
        "user__email",
    )
    list_filter = ("outcome",)


class MatchOddsFilter(admin.SimpleListFilter):
    title = 'Match odds'
    parameter_name = 'odds'

    def lookups(self, request, model_admin):
        return (
            ('has-odds', 'Has odds'),
            ('no-odds', 'No odds'),
        )

    def queryset(self, request, queryset):
        now = datetime.now()
        if self.value() == "has-odds":
            return queryset.filter(
                home_odds__isnull=False,
                draw_odds__isnull=False,
                away_odds__isnull=False,
            )
        elif self.value() == "no-odds":
            return queryset.filter(
                home_odds__isnull=True,
                draw_odds__isnull=True,
                away_odds__isnull=True,
            )


class MatchStatusFilter(admin.SimpleListFilter):
    title = 'Match status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('not-started', 'Not started'),
            ("in-play", "In play"),
            ('result', 'Result'),
        )

    def queryset(self, request, queryset):
        now = datetime.now()
        if self.value() == "not-started":
            return queryset.filter(datetime__gte=now)
        elif self.value() == "in-play":
            return queryset.exclude(
                Q(datetime__gte=now)
                | Q(home_goals__isnull=False)
                | Q(away_goals__isnull=False)
            )
        elif self.value() == "result":
            return queryset.filter(home_goals__isnull=False, away_goals__isnull=False)


@admin.register(Match)
class Match(admin.ModelAdmin):
    model = Match
    list_filter = (MatchStatusFilter, MatchOddsFilter)
    search_fields = ("home_team", "away_team")
    list_display = ("match", "kickoff")

    actions = ("fake_result",)

    @admin.display(description='match')
    def match(self, obj):
        return obj

    @admin.display(description='kick off')
    def kickoff(self, obj):
        return localise_datetime(obj.datetime)

    @admin.action(description='Fake a 1-1 draw')
    def fake_result(modeladmin, request, queryset):
        for match in queryset:
            data = {"home_goals": 1, "away_goals": 1}
            update_match_bets_and_payout(match, data)
        messages.success(request, "Result(s) faked!")

    def get_urls(self):
        urls = super().get_urls()
        my_action_urls = [
            path('matches/', self.get_next_matches_and_save_to_db),
            path('odds/', self.get_odds_and_update_matches_on_db),
            path('results/', self.get_results_and_update_matches_on_db),
        ]
        return my_action_urls + urls

    def get_next_matches_and_save_to_db(self, request):
        try:
            get_next_matches_and_save_to_db()
            self.message_user(request, "Next matches have been fetched")
        except RapidApiDataFetchingError:
            messages.error(request, "Data Fetching Error")
        except RapidApiDataParsingError:
            messages.error(request, "Data Parsing Error")
        return HttpResponseRedirect("../")

    def get_odds_and_update_matches_on_db(self, request):
        try:
            get_odds_and_update_matches_on_db()
            self.message_user(request, "Odds have been fetched")
        except RapidApiDataFetchingError:
            messages.error(request, "Data Fetching Error")
        except RapidApiDataParsingError:
            messages.error(request, "Data Parsing Error")
        return HttpResponseRedirect("../")

    def get_results_and_update_matches_on_db(self, request):
        try:
            get_results_and_update_matches_on_db()
            self.message_user(request, "Results have been fetched")
        except RapidApiDataFetchingError:
            messages.error(request, "Data Fetching Error")
        except RapidApiDataParsingError:
            messages.error(request, "Data Parsing Error")
        return HttpResponseRedirect("../")


@admin.register(TransactionRecord)
class TransactionRecordAdmin(admin.ModelAdmin):
    model: TransactionRecord
    search_fields = ("bet__user__email",)
