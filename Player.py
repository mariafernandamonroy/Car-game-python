class Player:
    def __init__(self):
        self._player_name = ""
        self._car = 0
        self._rail = 0
        self._position_distance = 0
        self._won_games = 0
        self._podium_position = 0

    def get_player_name (self):
        return self._player_name

    def set_player_name(self, player_name):
        self._player_name = player_name

    def get_car (self):
            return self._car

    def set_car(self, car):
        self._car = car

    def get_rail (self):
            return self._rail

    def set_rail(self, rail):
        self._rail = rail

    def get_position_distance (self):
        return self._position_distance

    def set_position_distance(self, position_distance):
        self._position_distance = position_distance

    def get_won_games (self):
        return self._won_games

    def set_won_games(self, won_games):
        self._won_games = won_games

    def get_podium_position (self):
        return self._podium_position

    def set_podium_position(self, podium_position):
        self._podium_position = podium_position

    def to_db_collection(self):
        return {
            "player_name": self._player_name,
            "car": self._car,
            "rail": self._rail,
            "position_distance": self._position_distance,
            "won_games": self._won_games,
            "podium_position": self._podium_position,
        }
