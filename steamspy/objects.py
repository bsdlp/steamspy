class Game(object):
    _PARAMS = [
        'appid', 'name', 'owners', 'owners_variance', 'players_forever',
        'players_forever_variance', 'players_2weeks',
        'players_2weeks_variance', 'average_forever', 'average_2weeks',
        'median_forever', 'median_2weeks'
    ]

    def __init__(self, **kwargs):
        """
        * appid - Steam Application ID. If it's 999999, then data for this application is hidden on developer's request, sorry.
        * owners - owners of this application on Steam. **Beware of free weekends!**
        * owners_variance - variance in owners. The real number of owners lies somewhere on owners +/- owners_variance range.
        * players_forever - people that have played this game since March 2009.
        * players_forever_variance - variance for total players.
        * players_2weeks - people that have played this game in the last 2 weeks.
        * players_2weeks_variance - variance for the number of players in the last two weeks.
        * average_forever - average playtime since March 2009. In minutes.
        * average_2weeks - average playtime in the last two weeks. In minutes.
        * median_forever - median playtime since March 2009. In minutes.
        * median_2weeks - median playtime in the last two weeks. In minutes.
        """
        for param in self._PARAMS:
            setattr(self, param, kwargs.get(param, None))
