from rock_paper_scissors import RockPaperScissors


class GameProcessor:
    def __init__(self):
        self.game_options = ('rock', 'paper', 'scissors')
        self.user_name = None
        self.user_score = None

    def game_process(self):
        print("Okay, let's start")

        while True:
            user_choice = input()

            if user_choice == '!exit':
                break

            elif user_choice == '!rating':
                print(f"Your rating: {self.user_score}")
                continue

            elif user_choice not in self.game_options:
                print('Invalid input')
                continue

            self.play_game(user_choice)

        print('Bye!')

    def play_game(self, user_choice):
        new_game = self._init_game()

        new_game.process_game(user_choice)

        self._update_user_score(new_game.get_game_result())

        new_game.print_game_result()

    def set_user(self, user_name):
        self.user_name = user_name
        print(f"Hello, {self.user_name}")
        self.user_score = self._init_user_score_by_name()

        return self

    def set_game_options(self, game_options):
        if game_options:
            self.game_options = game_options.split(',')

        return self

    def _init_game(self):
        return RockPaperScissors(self.game_options)

    def _init_user_score_by_name(self):
        with open('rating.txt', 'r') as rating_file:
            for line in rating_file:

                if self.user_name in line:
                    return int(line.split()[1])

        return 0

    def _update_user_score(self, game_result):
        self.user_score += ((game_result == 'user_win' and 1) * 100
                            + (game_result == 'user_draw' and 1) * 50)
