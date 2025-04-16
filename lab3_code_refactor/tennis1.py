class TennisGame1:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"] # dodano stałą klasową przechowująca nazwy punktacji

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0 # zmieniono nazewnictwo zmiennych punktów
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_points += 1
        elif player_name == self.player2_name:
            self.p2_points += 1
        else:
            raise ValueError("Unknown player name") # dodano rzucanie wyjątku przy nieznanej nazwie gracza

    def score(self): # score uzywa trzech nowych metod pomocniczych
        if self.p1_points == self.p2_points:
            return self._even_score()
        elif self.p1_points >= 4 or self.p2_points >= 4:
            return self._advantage_or_win()
        else:
            return self._regular_score()

    def _even_score(self):
        if self.p1_points < 3:
            return f"{self.SCORE_NAMES[self.p1_points]}-All"
        return "Deuce"

    def _advantage_or_win(self):
        score_diff = self.p1_points - self.p2_points
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _regular_score(self):
        p1_score = self.SCORE_NAMES[self.p1_points]
        p2_score = self.SCORE_NAMES[self.p2_points]
        return f"{p1_score}-{p2_score}"
