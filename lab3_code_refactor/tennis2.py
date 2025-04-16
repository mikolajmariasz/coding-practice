class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        points_to_text = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"} # słownik z nazwami poszczególnych wyników

        if self.p1_points == self.p2_points:
            if self.p1_points < 3:
                return f"{points_to_text[self.p1_points]}-All"
            else:
                return "Deuce"  

        if self.p1_points >= 4 or self.p2_points >= 4:
            point_diff = self.p1_points - self.p2_points
            if point_diff == 1:
                return f"Advantage {self.player1_name}" # zmieniono z hard-coded wartosci
            elif point_diff == -1:
                return f"Advantage {self.player2_name}" 
            elif point_diff >= 2:
                return f"Win for {self.player1_name}"  
            elif point_diff <= -2:
                return f"Win for {self.player2_name}"  

        p1_score_text = points_to_text[self.p1_points]
        p2_score_text = points_to_text[self.p2_points]
        return f"{p1_score_text}-{p2_score_text}"

    # usunięto zbędne pętle
    def set_p1_score(self, number):
        self.p1_points = number

    def set_p2_score(self, number):
        self.p2_points = number

    def p1_score(self):
        self.p1_points += 1

    def p2_score(self):
        self.p2_points += 1
