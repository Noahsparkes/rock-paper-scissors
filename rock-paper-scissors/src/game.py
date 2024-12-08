import random
# game logic
options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    # win conditions
    if player == computer:
        print("It's a Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose!")

    play_again = input("play again? (y/n): ").lower()
    if not play_again == "y":
        running = False  


print("thanks for playing")




## open the venv: source venv/bin/activate
##  cd /Users/noah/rock-paper-scissors/src
## python3 game.py





## pushing changes to GitHub:
## git add game.py
## git commit -m "update game.py"
## git push origin main