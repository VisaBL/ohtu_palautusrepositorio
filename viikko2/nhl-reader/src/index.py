import requests
from player import Player

class PlayerStats():
    def __init__(self, reader):
        self.players = reader
    def top_scorers_by_nationality(self, nat):
        print(f"Players from {nat}")
        filtered = filter(lambda p: p.nationality==nat, self.players)
        return sorted(filtered, key=lambda p: p.points, reverse=True)
    
## ei tartte luokkaa tälle toimenpitellee ainakaan vielä :)
def PlayerReader(url):
    response = requests.get(url).json()
    players = []
    for player_dict in response:
        player = Player(player_dict)
        players.append(player)
    return players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("SWE")

    for player in players:
        print(player)
if __name__ == "__main__":
    main()
