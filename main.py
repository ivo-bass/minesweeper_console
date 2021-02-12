from logic import play
from initialize import create_boards, create_player_instance, ask_for_a_game
from utils.prints import show_board, print_welcome, print_goodbye, print_result_to_file


def main():
    print_welcome()
    player = create_player_instance()
    while True:
        play_board, reference_board = create_boards()
        show_board(play_board)
        play(player, play_board, reference_board)
        if not ask_for_a_game():
            print_goodbye(player)
            print_result_to_file(player)
            break


if __name__ == '__main__':
    main()