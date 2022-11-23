# 855740 is valid for betting, 855741 has kicked off already
original_data = [
    {
        'fixture': {
            'id': 855740,
            'referee': 'F. Rapallini',
            'timezone': 'UTC',
            'date': '2023-11-23T10:00:00+00:00',
            'timestamp': 1669197600,
            'periods': {'first': None, 'second': None},
            'venue': {'id': None, 'name': 'Al Bayt Stadium', 'city': 'Al Khor'},
            'status': {'long': 'Not Started', 'short': 'NS', 'elapsed': None},
        },
        'league': {
            'id': 1,
            'name': 'World Cup',
            'country': 'World',
            'logo': 'https://media.api-sports.io/football/leagues/1.png',
            'flag': None,
            'season': 2022,
            'round': 'Group Stage - 1',
        },
        'teams': {
            'home': {
                'id': 31,
                'name': 'Morocco',
                'logo': 'https://media.api-sports.io/football/teams/31.png',
                'winner': None,
            },
            'away': {
                'id': 3,
                'name': 'Croatia',
                'logo': 'https://media.api-sports.io/football/teams/3.png',
                'winner': None,
            },
        },
        'goals': {'home': None, 'away': None},
        'score': {
            'halftime': {'home': None, 'away': None},
            'fulltime': {'home': None, 'away': None},
            'extratime': {'home': None, 'away': None},
            'penalty': {'home': None, 'away': None},
        },
    },
    {
        'fixture': {
            'id': 855741,
            'referee': 'Ivan Cisneros',
            'timezone': 'UTC',
            'date': '2022-11-23T13:00:00+00:00',
            'timestamp': 1669208400,
            'periods': {'first': None, 'second': None},
            'venue': {
                'id': None,
                'name': 'Khalifa International Stadium',
                'city': 'Ar-Rayyan',
            },
            'status': {'long': 'Not Started', 'short': 'NS', 'elapsed': None},
        },
        'league': {
            'id': 1,
            'name': 'World Cup',
            'country': 'World',
            'logo': 'https://media.api-sports.io/football/leagues/1.png',
            'flag': None,
            'season': 2022,
            'round': 'Group Stage - 1',
        },
        'teams': {
            'home': {
                'id': 25,
                'name': 'Germany',
                'logo': 'https://media.api-sports.io/football/teams/25.png',
                'winner': None,
            },
            'away': {
                'id': 12,
                'name': 'Japan',
                'logo': 'https://media.api-sports.io/football/teams/12.png',
                'winner': None,
            },
        },
        'goals': {'home': None, 'away': None},
        'score': {
            'halftime': {'home': None, 'away': None},
            'fulltime': {'home': None, 'away': None},
            'extratime': {'home': None, 'away': None},
            'penalty': {'home': None, 'away': None},
        },
    },
]

# match one == draw
# match two = home win
results_data = [
    {
        'fixture': {
            'id': 855740,
            'referee': 'F. Rapallini',
            'timezone': 'UTC',
            'date': '2022-11-23T10:00:00+00:00',
            'timestamp': 1669197600,
            'periods': {'first': None, 'second': None},
            'venue': {'id': None, 'name': 'Al Bayt Stadium', 'city': 'Al Khor'},
            'status': {'long': 'Not Started', 'short': 'FT', 'elapsed': None},
        },
        'league': {
            'id': 1,
            'name': 'World Cup',
            'country': 'World',
            'logo': 'https://media.api-sports.io/football/leagues/1.png',
            'flag': None,
            'season': 2022,
            'round': 'Group Stage - 1',
        },
        'teams': {
            'home': {
                'id': 31,
                'name': 'Morocco',
                'logo': 'https://media.api-sports.io/football/teams/31.png',
                'winner': None,
            },
            'away': {
                'id': 3,
                'name': 'Croatia',
                'logo': 'https://media.api-sports.io/football/teams/3.png',
                'winner': None,
            },
        },
        'goals': {'home': 1, 'away': 1},
        'score': {
            'halftime': {'home': None, 'away': None},
            'fulltime': {'home': None, 'away': None},
            'extratime': {'home': None, 'away': None},
            'penalty': {'home': None, 'away': None},
        },
    },
    {
        'fixture': {
            'id': 855741,
            'referee': 'Ivan Cisneros',
            'timezone': 'UTC',
            'date': '2022-11-23T13:00:00+00:00',
            'timestamp': 1669208400,
            'periods': {'first': None, 'second': None},
            'venue': {
                'id': None,
                'name': 'Khalifa International Stadium',
                'city': 'Ar-Rayyan',
            },
            'status': {'long': 'Not Started', 'short': 'FT', 'elapsed': None},
        },
        'league': {
            'id': 1,
            'name': 'World Cup',
            'country': 'World',
            'logo': 'https://media.api-sports.io/football/leagues/1.png',
            'flag': None,
            'season': 2022,
            'round': 'Group Stage - 1',
        },
        'teams': {
            'home': {
                'id': 25,
                'name': 'Germany',
                'logo': 'https://media.api-sports.io/football/teams/25.png',
                'winner': None,
            },
            'away': {
                'id': 12,
                'name': 'Japan',
                'logo': 'https://media.api-sports.io/football/teams/12.png',
                'winner': None,
            },
        },
        'goals': {'home': 2, 'away': 0},
        'score': {
            'halftime': {'home': None, 'away': None},
            'fulltime': {'home': None, 'away': None},
            'extratime': {'home': None, 'away': None},
            'penalty': {'home': None, 'away': None},
        },
    },
]

odds_data = [
    {
        "league": {
            "id": 1,
            "name": "World Cup",
            "country": "World",
            "logo": "https://media.api-sports.io/football/leagues/1.png",
            "flag": None,
            "season": 2022,
        },
        "fixture": {
            "id": 855748,
            "timezone": "UTC",
            "date": "2022-11-25T16:00:00+00:00",
            "timestamp": 1669392000,
        },
        "update": "2022-11-23T00:05:11+00:00",
        "bookmakers": [
            {
                "id": 6,
                "name": "Bwin",
                "bets": [
                    {
                        "id": 1,
                        "name": "Match Winner",
                        "values": [
                            {"value": "Home", "odd": "1.80"},
                            {"value": "Draw", "odd": "3.50"},
                            {"value": "Away", "odd": "4.60"},
                        ],
                    }
                ],
            }
        ],
    }
]

bad_data = [
    {
        'fixtureX': {
            'id': 855740,
            'referee': 'F. Rapallini',
            'timezone': 'UTC',
            'date': '2022-11-23T10:00:00+00:00',
            'timestamp': 1669197600,
            'periods': {'first': None, 'second': None},
            'venue': {'id': None, 'name': 'Al Bayt Stadium', 'city': 'Al Khor'},
            'status': {'long': 'Not Started', 'short': 'NS', 'elapsed': None},
        },
        'league': {
            'id': 1,
            'name': 'World Cup',
            'country': 'World',
            'logo': 'https://media.api-sports.io/football/leagues/1.png',
            'flag': None,
            'season': 2022,
            'round': 'Group Stage - 1',
        },
        'teams': {
            'home': {
                'id': 31,
                'name': 'Morocco',
                'logo': 'https://media.api-sports.io/football/teams/31.png',
                'winner': None,
            },
            'away': {
                'id': 3,
                'name': 'Croatia',
                'logo': 'https://media.api-sports.io/football/teams/3.png',
                'winner': None,
            },
        },
        'goals': {'home': None, 'away': None},
        'score': {
            'halftime': {'home': None, 'away': None},
            'fulltime': {'home': None, 'away': None},
            'extratime': {'home': None, 'away': None},
            'penalty': {'home': None, 'away': None},
        },
    },
    {
        'fixture': {
            'id': 855741,
            'referee': 'Ivan Cisneros',
            'timezone': 'UTC',
            'date': '2022-11-23T13:00:00+00:00',
            'timestamp': 1669208400,
            'periods': {'first': None, 'second': None},
            'venue': {
                'id': None,
                'name': 'Khalifa International Stadium',
                'city': 'Ar-Rayyan',
            },
            'status': {'long': 'Not Started', 'short': 'NS', 'elapsed': None},
        },
        'league': {
            'id': 1,
            'name': 'World Cup',
            'country': 'World',
            'logo': 'https://media.api-sports.io/football/leagues/1.png',
            'flag': None,
            'season': 2022,
            'round': 'Group Stage - 1',
        },
        'teams': {
            'homeX': {
                'id': 25,
                'name': 'Germany',
                'logo': 'https://media.api-sports.io/football/teams/25.png',
                'winner': None,
            },
            'away': {
                'id': 12,
                'name': 'Japan',
                'logo': 'https://media.api-sports.io/football/teams/12.png',
                'winner': None,
            },
        },
        'goals': {'home': None, 'away': None},
        'score': {
            'halftime': {'home': None, 'away': None},
            'fulltime': {'home': None, 'away': None},
            'extratime': {'home': None, 'away': None},
            'penalty': {'home': None, 'away': None},
        },
    },
]

bad_odds_data = [
    {
        "league": {
            "id": 1,
            "name": "World Cup",
            "country": "World",
            "logo": "https://media.api-sports.io/football/leagues/1.png",
            "flag": None,
            "season": 2022,
        },
        "fixture": {
            "id": 855748,
            "timezone": "UTC",
            "date": "2022-11-25T16:00:00+00:00",
            "timestamp": 1669392000,
        },
        "update": "2022-11-23T00:05:11+00:00",
        "bookmakers": [
            {
                "id": 6,
                "name": "Bwin",
                "bets": [
                    {
                        "id": 1,
                        "name": "Match Winner",
                        "values": [
                            {"value": "Home", "oddX": "1.80"},
                            {"value": "Draw", "odd": "3.50"},
                            {"value": "Away", "odd": "4.60"},
                        ],
                    }
                ],
            }
        ],
    }
]
