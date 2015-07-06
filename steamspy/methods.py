import inspect
import requests
from .objects import Game


class APIHelper(object):
    _API_URL = 'http://steamspy.com/api.php'

    def __init__(self):
        self.game = Game(**self._get())

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
    pass


class Top100Forever(APIHelper):
    pass


class Top100Owned(APIHelper):
    pass


class All(APIHelper):
    pass
