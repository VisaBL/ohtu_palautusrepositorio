class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def def_score(self):
        victory = 4
        if self.player1_score == self.player2_score:
            return "tie"
        if self.player1_score >= victory or self.player2_score >= victory :
            return "abovefor"
        return "calculate"

    def calculate_points(self, score_names):
        score = ""
        for i in range(2):
            if i == 0:
                points = self.player1_score
            else:
                score += "-"
                points = self.player2_score
            score += score_names[points]
        return score
    
    def calculate_winner(self): 
        define_diffecende = self.player1_score - self.player2_score
        case =  "Advantage "
        if abs(define_diffecende) > 1:
            case = "Win for "
        if define_diffecende > 0:
            return case + self.player1_name
        return case + self.player2_name
    
    def get_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        situation = self.def_score()
        match situation:
            case "tie":
                if self.player1_score < 3:
                    return score_names[self.player1_score] + "-All"
                return "Deuce"
            case "abovefor":
                return self.calculate_winner()
            case "calculate":
                return self.calculate_points(score_names)