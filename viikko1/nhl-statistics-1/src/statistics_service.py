from enum import Enum

class SortBy(Enum):
    GOALS = 1
    POINTS = 2
    ASSIST = 3

class StatisticsService():
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, type: SortBy): 
        methods = {
            "ASSIST": lambda player: player.assists, 
            "GOALS": lambda player: player.goals, 
            "POINTS": lambda player: player.points
            }
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=methods[type.name]
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
