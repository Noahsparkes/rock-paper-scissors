import random
# game logic
options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
        if player not in options:
            print("Invalid choice.Pleae try again.")

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


##scoreboard
player_score = 0
computer_score = 0
ties = 0

#Update scores based on the game outcome
if player == computer:
    ties += 1
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    player_score += 1
else:
    computer_score += 1

print(f"Score - You: {player_score}, Computer: {computer_score}, Ties: {ties}")




## open the venv: source venv/bin/activate
##  cd /Users/noah/rock-paper-scissors/src
## python3 game.py





## pushing changes to GitHub:
## git add game.py
## git commit -m "update game.py"
## git push origin main

# Steps now:
# 1. Create an app.py file and add flask to it.
# 2. Create a route to the game.py file.
# 3. Create a route to the index.html file.
# 4. Create a route to the style.css file.
# 5. Create a route to the script.js file.

# DevOps steps next!