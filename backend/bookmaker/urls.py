from django.urls import path

from bookmaker.views import (
    GetCustomerView,
    NextMatchesView,
    MyBetsView,
    ServerWillRefreshView,
)

app_name = "bookmaker"

urlpatterns = [
    path(
        "get-customer/",
        GetCustomerView.as_view(),
    ),
    path(
        "next-matches/",
        NextMatchesView.as_view(),
    ),
    path(
        "my-bets/",
        MyBetsView.as_view(),
    ),
    path(
        "server-will-refresh/",
        ServerWillRefreshView.as_view(),
    ),
]
