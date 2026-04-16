class TennisGame2:
    # Stała zamiast powtarzających się ifów (usunięcie duplikacji kodu)
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name

        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        #obsługa zarówno "player1", jak i rzeczywistej nazwy
        if player_name == self.player1_name:
            self.p1_score()
        elif player_name == self.player2_name:
            self.p2_score()

    def score(self):
        #rozbicie dużej metody na mniejsze
        if self._is_tie():
            return self._tie_score()

        if self._is_endgame():
            return self._endgame_score()

        return self._regular_score()

    def _is_tie(self):
        #wydzielona logika sprawdzania remisu
        return self.p1points == self.p2points

    def _is_endgame(self):
        #wydzielona logika końcowej fazy gry
        return self.p1points >= 4 or self.p2points >= 4

    def _tie_score(self):
        #uproszczona logika remisu (bez wielu ifów)
        if self.p1points < 3:
            return f"{self._score_name(self.p1points)}-All"
        return "Deuce"

    def _endgame_score(self):
        #uproszczone warunki (usunięcie zbędnych sprawdzeń)
        point_difference = self.p1points - self.p2points

        if point_difference == 1:
            return f"Advantage {self.player1_name}"
        if point_difference == -1:
            return f"Advantage {self.player2_name}"
        if point_difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _regular_score(self):
        #proste budowanie wyniku zamiast wielu ifów
        return (
            f"{self._score_name(self.p1points)}"
            f"-{self._score_name(self.p2points)}"
        )

    def _score_name(self, points):
        #jedno miejsce mapowania punktów na nazwy
        return self.SCORE_NAMES[points]

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
