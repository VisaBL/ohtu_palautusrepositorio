import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticService(unittest.TestCase):
    def setUp(self): 
        self.service = StatisticsService(
            PlayerReaderStub()
        )
    def test_search_known_player(self):
        player = self.service.search("Semenko")
        self.assertAlmostEqual("Semenko", player.name)

    def test_search_returns_null_if_player_not_exist(self):
        player = self.service.search("Pelihenkilö")
        self.assertIsNone(player)
    
    def test_returns_players_of_team(self):
        players = self.service.team("EDM")
        self.assertEqual(len(players), 3)
    
    def test_returns_player_on_top_by_points(self):
        best_player = self.service.top(4, SortBy.POINTS)
        self.assertEqual("Gretzky", best_player[0].name)

    def test_returns_player_on_top_by_goals(self):
        best_player = self.service.top(4, SortBy.GOALS)
        self.assertEqual("Lemieux", best_player[0].name)
    
    def test_returns_player_on_top_by_assists(self):
        best_player = self.service.top(4, SortBy.ASSIST)
        self.assertEqual("Gretzky", best_player[0].name)
    
    def test_returns_player_second_last_by_assists(self):
        best_player = self.service.top(4, SortBy.ASSIST)
        self.assertEqual("Kurri", best_player[3].name)