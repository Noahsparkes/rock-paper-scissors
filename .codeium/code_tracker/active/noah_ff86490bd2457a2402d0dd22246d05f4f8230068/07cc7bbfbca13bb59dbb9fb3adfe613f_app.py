
*/Users/noah/rock-paper-scissors/src/app.pyˆ# from flask import Flask, render_template, request, jsonify
# from .game import play_game

# # Flask App Setup
# app = Flask(__name__)

# @app.route('/')
# def index():
#     """Render the main game page"""
#     return render_template('index.html')

# @app.route('/play', methods=['POST'])
# def play():
#     """
#     Handle game play via AJAX request
#     """
#     # Get player's choice from JSON request
#     data = request.get_json()
#     player_choice = data.get('choice')
    
#     # Play the game
#     game_result = play_game(player_choice)
    
#     return jsonify(game_result)

# if __name__ == '__main__':
#     app.run(debug=True)

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from game import play_game  # Now Python should resolve this correctly


import sys
print("PYTHONPATH:", sys.path)
from flask import Flask, render_template, request, jsonify
from game import play_game  # Import the play_game function

# Flask App Setup
app = Flask(__name__)

@app.route('/')
def index():
    """Render the main game page"""
    return render_template('index.html')  # Ensure index.html is created in the templates folder

@app.route('/play', methods=['POST'])
def play():
    """Handle game play via AJAX request"""
    data = request.get_json()  # Get player's choice from JSON request
    player_choice = data.get('choice')
    
    # Play the game
    if player_choice not in ["rock", "paper", "scissors"]:
        return jsonify({"error": "Invalid choice!"}), 400
    
    game_result = play_game(player_choice)
    return jsonify(game_result)

if __name__ == '__main__':
    app.run(debug=True)

å
åç çß
ß© ©““””ııˆ"(ff86490bd2457a2402d0dd22246d05f4f8230068*/Users/noah21file:///Users/noah/rock-paper-scissors/src/app.py:file:///Users/noah