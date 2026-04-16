class TennisGame3:
    #stała z nazwami punktów zamiast lokalnej listy w metodzie
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        #czytelniejsze nazwy pól
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        #obsługa celowego błędu z zadania i prawdziwych nazw graczy
        if player_name == self.player1_name:
            self.player1_points += 1
        elif player_name == self.player2_name:
            self.player2_points += 1

    def score(self):
        #rozbicie logiki na prostsze przypadki
        if self._is_regular_score():
            return self._regular_score()

        if self._is_deuce():
            return "Deuce"

        return self._endgame_score()

    def _is_regular_score(self):
        #wydzielony warunek zwykłej punktacji
        return (
            self.player1_points < 4
            and self.player2_points < 4
            and self.player1_points + self.player2_points < 6
        )

    def _regular_score(self):
        #uproszczone budowanie zwykłego wyniku
        player1_score = self.SCORE_NAMES[self.player1_points]

        if self.player1_points == self.player2_points:
            return f"{player1_score}-All"

        player2_score = self.SCORE_NAMES[self.player2_points]
        return f"{player1_score}-{player2_score}"

    def _is_deuce(self):
        #osobna metoda poprawia czytelność
        return self.player1_points == self.player2_points

    def _endgame_score(self):
        #czytelniejsza różnica punktów zamiast mnożenia
        point_difference = self.player1_points - self.player2_points
        leading_player = self._leading_player_name()

        if abs(point_difference) == 1:
            return f"Advantage {leading_player}"

        return f"Win for {leading_player}"

    def _leading_player_name(self):
        #wydzielenie wyboru prowadzącego gracza
        if self.player1_points > self.player2_points:
            return self.player1_name
        return self.player2_name