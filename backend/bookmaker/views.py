from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from backend import CRON_RESULTS_EQUIVALENT_TIME_STRINGS

from account.authentification import CustomerAuthentification
from bookmaker.serializers import CustomerSerializer, MatchSerializer, BetSerializer
from bookmaker.models import Bet
from bookmaker.services import place_bet, check_time_of_next_refresh, show_next_matches
from bookmaker.utils import string_to_time


class GetCustomerView(GenericAPIView):
    authentication_classes = [CustomerAuthentification]
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        user = self.get_serializer(request.user)
        return Response(status=200, data=user.data)


class NextMatchesView(ListAPIView):
    authentication_classes = [CustomerAuthentification]
    serializer_class = MatchSerializer

    def get_queryset(self):
        return show_next_matches()


class MyBetsView(ListCreateAPIView):
    authentication_classes = [CustomerAuthentification]
    serializer_class = BetSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["outcome"]
    ordering_fields = ["match__datetime"]

    def get_queryset(self):
        return Bet.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            place_bet(user=user, **serializer.data)
        except Exception as e:
            return Response(status=400, data=e.error)
        return Response(status=200, data={"success": "Bet has been posted. Good luck!"})


class ServerWillRefreshView(GenericAPIView):
    authentication_classes = [CustomerAuthentification]
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        # CHECK WHAT TIME CELERY WILL NEXT UPDATE RESULTS
        refresh_times = list(
            map(lambda x: string_to_time(x), CRON_RESULTS_EQUIVALENT_TIME_STRINGS)
        )
        last_refresh, next_refresh = check_time_of_next_refresh(refresh_times)
        return Response(
            status=200,
            data={"next_refresh": next_refresh, "last_refresh": last_refresh},
        )
