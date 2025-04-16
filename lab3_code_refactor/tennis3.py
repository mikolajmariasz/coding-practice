class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_points += 1
        elif player_name == self.player2_name:
            self.p2_points += 1
        else:
            raise ValueError("Unknown player name")

    def score(self):
        if self._is_early_game():
            return self._early_game_score()
        if self.p1_points == self.p2_points:
            return "Deuce"
        return self._advantage_or_win()

    def _is_early_game(self):
        return self.p1_points < 4 and self.p2_points < 4 and (self.p1_points + self.p2_points) < 6

    def _early_game_score(self):
        p1_score = self.SCORE_NAMES[self.p1_points]
        p2_score = self.SCORE_NAMES[self.p2_points]
        return f"{p1_score}-All" if self.p1_points == self.p2_points else f"{p1_score}-{p2_score}"

    def _advantage_or_win(self):
        leading_player = self.player1_name if self.p1_points > self.p2_points else self.player2_name
        score_diff = abs(self.p1_points - self.p2_points)
        if score_diff == 1:
            return f"Advantage {leading_player}"
        return f"Win for {leading_player}"
