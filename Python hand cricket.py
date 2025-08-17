import random

def play_hand_cricket():
    print("")
    print("---Welcome to Hand Cricket!---")
    print()
    print("""               RULES
1.You are given the chance to bat first and will be up against the computer.
2.You are not allowed to play a number above 10 and below zero i.e., you can only play numbers between 0 and 10(0 and 10 included).
3.Your total score will be displayed after each ball.
4.If the computer guesses your number, then you are declared out!!
5.All these rules apply for the computer also.
""")
    print("")
    print("Let's toss to decide batting or bowling.")
    print("Enter '1' for heads or '2' for tails.")

    toss_choice = int(input("Your choice: "))
    toss_result = random.randint(1, 2)

    if toss_choice == toss_result:
        print("You won the toss!")
        print("What do you choose? Enter '1' for batting or '2' for bowling.")
        choice = int(input("Your choice: "))

        if choice == 1:
            player_score = play_innings(player_bats=True)
            computer_score = play_innings(player_bats=False)
        elif choice == 2:
            computer_score = play_innings(player_bats=False)
            player_score = play_innings(player_bats=True)
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    else:
        print("You lost the toss.")
        toss_choice = random.randint(1, 2)

        if toss_choice == 1:
            print("The computer chose to bat.")
            computer_score = play_innings(player_bats=False)
            player_score = play_innings(player_bats=True)
        elif toss_choice == 2:
            print("The computer chose to bowl.")
            player_score = play_innings(player_bats=True)
            computer_score = play_innings(player_bats=False)

    print("Game over!")
    print("Your score:", player_score)
    print("Computer's score:", computer_score)

    if player_score > computer_score:
        print("Congratulations! You won!")
    elif player_score < computer_score:
        print("You lost! Better luck next time.")
    else:
        print("It's a tie!")

def play_innings(player_bats):
    score = 0

    print("Let's play Hand Cricket!")
    print("You're batting." if player_bats else "Computer is batting.")

    while True:
        if player_bats:
            player_throw = int(input("Enter your throw (1-6): "))
            computer_throw = random.randint(1, 6)
        else:
            computer_throw = random.randint(1, 6)
            player_throw = int(input("Enter your throw (1-6): "))

        print("You threw:", player_throw)
        print("Computer threw:", computer_throw)

        if player_throw < 1 or player_throw > 6:
            print("Invalid throw. Please enter a number between 1 and 6.")
            continue

        if player_throw == computer_throw:
            print("Out!")
            break

        score += player_throw

        if not player_bats:
            score += computer_throw

        print("Current score:", score)
        print()

    print("Innings over!")
    print("Total score:", score)

    return score

play_hand_cricket()