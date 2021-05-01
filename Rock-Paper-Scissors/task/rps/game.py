from game_processor import GameProcessor


def game_process(game):
    while True:
        print("Okay, let's start")

        user_choice = input()

        if user_choice == '!exit':
            break

        elif user_choice == '!rating':
            print(f"Your rating: {game.get_user_score()}")
            continue

        elif user_choice not in game.get_game_options():
            print('Invalid input')
            continue

        game.play_game(user_choice)

    print('Bye!')


def main():
    new_game = GameProcessor()

    new_game.set_user(input("Enter your name:\n"))

    game_options = input()
    if game_options:
        new_game.set_game_options(game_options.split(','))

    game_process(new_game)


if __name__ == '__main__':
    main()
