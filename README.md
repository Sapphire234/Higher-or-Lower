# Higher-or-Lower
A game where the players have to guess which celebrity has more Instagram followers

## About the game
The game selects two random entries from a list of 50 well-known accounts (celebrities, brands, and athletes). A short description and the location of the account is provided.
You guess by typing 1 or 2, meaning which of the accounts has a higher following. As you play the score is kept. 
When you guess incorrectly the game ends and it shows the number of followers each account has along with your final score.

## Setup
1. Ensure you have Python 3 installed.
2. Clone this repository.
3. Run the application:
   ```bash
   python main.py

## Project structure
* `main.py`: Handles the game loop, input validation, and scoring
* `game_data.py`: The list of accounts including names, follower counts, and descriptions
* `art.py`: Contains the logo and game separators
