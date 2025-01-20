while True:
    from os import execl
    from sys import executable, argv
    from colorama import Fore, Style
    from random import randint

    rock = 'ROCK'
    paper = 'PAPER'
    scissors = 'SCISSORS'

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    computer_move = ''

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Please try again...")

    print(Style.BRIGHT + f"You chose {player_move}.")

    computer_random_number = randint(1, 3)

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(Fore.BLUE + f"The computer chose {computer_move}.\n")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.GREEN + "You win!")
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        print(Fore.RED + "You lose!")

    exit_game = 'no'

    while True:
        restart = input(Style.RESET_ALL + "\nType [yes] to Play again or [no] to quit: ")

        if restart == 'yes':
            break
        elif restart == 'no':
            print(Style.BRIGHT + "\x1B[3mThank you for playing!")
            exit_game = 'yes'
            break
        else:
            print(Fore.RED + "Invalid input. Please try again...")
            continue

    if exit_game == 'yes':
        break