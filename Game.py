class Game:
    def __init__(self):
        self._id = ""
        self._track_limit = 0
        self._players = []

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_track_limit(self):
        return self._track_limit

    def set_track_limit(self,track_limit):
        self._track_limit = track_limit

    def get_players(self):
        return self._players

    def set_players(self, players):
        self._players = players



