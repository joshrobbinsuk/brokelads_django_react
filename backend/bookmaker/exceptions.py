class InsufficientBalanceError(Exception):
    error = {
        "error": "Insufficient funds. If this seems wrong to you, please contact us."
    }


class MatchDoesNotExistError(Exception):
    error = {"error": "Something's gone wrong! Please bet on another match"}


class MatchHasStartedError(Exception):
    error = {
        "error": "This match has already kicked off. Refresh the page for matches you can bet on."
    }


class RapidApiDataFetchingError(Exception):
    pass


class RapidApiDataParsingError(Exception):
    pass


class NoOddsFixtureWarning(Exception):
    pass
