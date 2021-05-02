from game_processor import GameProcessor


def main():
    (GameProcessor()
     .set_user(input("Enter your name:\n"))
     .set_game_options(input())
     .game_process())


if __name__ == '__main__':
    main()
