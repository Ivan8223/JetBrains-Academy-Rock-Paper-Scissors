import random


class RockPaperScissors:
    def __init__(self, game_options):
        self.game_options = game_options
        self.user_choice = None
        self.computer_choice = None
        self.game_result = None

    def print_game_result(self):
        game_results = {
            'user_lose': self._print_lose_message,
            'user_draw': self._print_draw_message,
            'user_win': self._print_win_message,
        }

        return game_results[self.game_result]()

    def get_game_result(self):
        return self.game_result

    def process_game(self, user_choice):
        self.game_result = self._calculate_game_result_(user_choice)

    def _calculate_game_result_(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = self._get_computer_choice()

        search_range = len(self.game_options) // 2
        user_choice_index = self.game_options.index(self.user_choice)
        computer_choice_index = self.game_options.index(self.computer_choice)

        if user_choice_index == computer_choice_index:
            return 'user_draw'

        elif (computer_choice_index < user_choice_index <= computer_choice_index + search_range
              or user_choice_index + search_range < computer_choice_index):
            return 'user_win'

        return 'user_lose'

    def _get_computer_choice(self):
        return random.choice(self.game_options)

    def _print_lose_message(self):
        print(f"Sorry, but the computer chose {self.computer_choice}")

    def _print_draw_message(self):
        print(f"There is a draw ({self.computer_choice})")

    def _print_win_message(self):
        print(f"Well done. The computer chose {self.computer_choice} and failed")
