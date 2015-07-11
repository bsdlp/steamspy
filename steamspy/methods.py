import inspect
import requests
from .objects import Game


class APIHelper(object):
    _API_URL = 'http://steamspy.com/api.php'
    _attribute = None

    def __init__(self):
        _games = (Game(**game) for game in self._get().values())
        # remove bogus 999999 app inserted by steamspy api
        _games = filter(lambda x: x.appid != 999999, _games)
        if self._attribute:
            self.games = sorted(
                _games, reverse=True,
                key=lambda game: getattr(game, self._attribute))
        else:
            self.games = list(_games)

    def _get(self, params={}):
        """
        :param params: Parameters to pass to the steamspy query.
        :type  params: ``dict``

        :return: Steamspy API response object.
        :rtype:  ``dict``
        """
        params['request'] = self.__class__.__name__.lower()
        resp = requests.get(self._API_URL, params=params)
        return resp.json()


class AppDetails(APIHelper):
    def __init__(self, appid):
        """
        :param appid: Steam AppID.
        :type  appid: ``int``
        """
        self.game = Game(**self._get(params={'appid': appid}))


class Genre(APIHelper):
    def __init__(self, genre):
        """
        :param genre: Game genre.
        :type  genre: ``str``
        """
        self.game = Game(**self._get(params={'genre': genre}))


class Top100In2Weeks(APIHelper):
    _attribute = 'players_2weeks'


class Top100Forever(APIHelper):
    _attribute = 'players_forever'


class Top100Owned(APIHelper):
    pass


class All(APIHelper):
    pass
