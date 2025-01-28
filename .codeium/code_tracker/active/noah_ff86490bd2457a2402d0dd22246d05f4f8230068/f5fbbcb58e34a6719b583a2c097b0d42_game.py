
+/Users/noah/rock-paper-scissors/src/game.pyÛ# import random
# # game logic
# options = ("rock", "paper", "scissors")
# running = True

# while running:
#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissors): ")
#         if player not in options:
#             print("Invalid choice.Pleae try again.")

#     print(f"player: {player}")
#     print(f"computer: {computer}")

#     # win conditions
#     if player == computer:
#         print("It's a Tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You Win!")
#     elif player == "paper" and computer == "rock":
#         print("You Win!")
#     elif player == "scissors" and computer == "paper":
#         print("You Win!")
#     else:
#         print("You lose!")

#     play_again = input("play again? (y/n): ").lower()
#     if not play_again == "y":
#         running = False  


# print("thanks for playing")


# ##scoreboard
# player_score = 0
# computer_score = 0
# ties = 0

# #Update scores based on the game outcome
# if player == computer:
#     ties += 1
# elif (player == "rock" and computer == "scissors") or \
#      (player == "paper" and computer == "rock") or \
#      (player == "scissors" and computer == "paper"):
#     player_score += 1
# else:
#     computer_score += 1

# print(f"Score - You: {player_score}, Computer: {computer_score}, Ties: {ties}")

import random

# Game Logic Function
def play_game(player_choice):
    # Valid options
    options = ("rock", "paper", "scissors")
    
    # Generate computer's choice
    computer_choice = random.choice(options)
    
    # Initialize result and score
    result = ""
    score = {"player": 0, "computer": 0, "ties": 0}
    
    # Determine result
    if player_choice == computer_choice:
        result = "It's a Tie!"
        score["ties"] += 1
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
        score["player"] += 1
    else:
        result = "You Lose!"
        score["computer"] += 1
    
    # Return the result and score
    return {
        "result": result,
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "score": score
    }

# For manual testing
if __name__ == "__main__":
    running = True
    overall_score = {"player": 0, "computer": 0, "ties": 0}

    while running:
        player = None
        while player not in ("rock", "paper", "scissors"):
            player = input("Enter a choice (rock, paper, scissors): ").lower()
            if player not in ("rock", "paper", "scissors"):
                print("Invalid choice. Please try again.")
        
        # Play the game
        result = play_game(player)
        
        # Update overall score
        for key in overall_score:
            overall_score[key] += result["score"][key]
        
        # Print result
        print(f"Player: {result['player_choice']}, Computer: {result['computer_choice']}")
        print(result["result"])
        print(f"Score - You: {overall_score['player']}, Computer: {overall_score['computer']}, Ties: {overall_score['ties']}")
        
        # Play again?
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            running = False
    
    print("Thanks for playing!")



## open the venv: source venv/bin/activate
##  cd /Users/noah/rock-paper-scissors/src
## python3 game.py





## pushing changes to GitHub:
## git add game.py
## git commit -m "update game.py"
## git push origin main

# Steps now:
# 1.fixing the game logic to fit with app.py file.
# 2. try to run program with flask.
# 3. export FLASK_APP=src.app
  #  set FLASK_APP=src.app
  # flask run

# go to src after venv and run: flask run.
° 
°Í 4ÍÎ *$009526fe-f558-4604-89cb-02beacdab8ae08ÎÏ4ÏÕ *$009526fe-f558-4604-89cb-02beacdab8ae082ÕÙ*$8c9bf4d4-c959-487b-8982-db6a1b11071808
ÙÛ "(ff86490bd2457a2402d0dd22246d05f4f8230068*/Users/noah22file:///Users/noah/rock-paper-scissors/src/game.py:file:///Users/noah