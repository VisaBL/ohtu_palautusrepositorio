#{'name': 'Joey Daccord', 'nationality': 
#'USA', 'assists': 0, 'goals': 0, 'penalties': 0, 'team': 'SEA', 'games': 5}
#
class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = self.goals+self.assists
    
    def __str__(self):
        return f"{self.name:22} {self.team:5}{self.goals:2} + {self.assists:2} = {self.points}"
