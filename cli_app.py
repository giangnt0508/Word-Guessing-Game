"""
ICT401 Assessment 3 - Word Guessing Game Command Line Interface (CLI)
Student Name: Truong Giang Nguyen
Student ID: 202572186
Date: 14/09/2026
Description: Text-based terminal interface for the Word Guessing Game
"""

from engine import GameEngine
import os
import sys
from datetime import datetime

class CLIApp:
    def __init__(self):
        """Initialize the CLI application."""
        self.engine = GameEngine()
        self.history_file = "game_history.txt"

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        """Print the game header."""
        print("========================================================")
        print("       WELCOME TO THE WORD GUESSING GAME")
        print("========================================================")
        print()
        

    def select_difficulty(self) -> str:
        """ Let the user select a difficulty level. """
        while True:
            print("\nSelect Difficulty:")
            print("  1. Easy")
            print("  2. Medium") 
            print("  3. Hard")
            print("  4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "4":
                print("\nThank you for playing! Goodbye!")
                sys.exit(0)
            elif choice == "1":
                return "easy"
            elif choice == "2":
                return "medium"
            elif choice == "3":
                return "hard"
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                
    def play_game(self):
        """Main game loop."""
        while True:
            self.clear_screen()
            self.print_header()

            # Select difficulty
            difficulty = self.select_difficulty()

            # Game ended - show results
            self.clear_screen()
            self.print_header()
            self.print_game_state()

            # Save history
            self.save_game_history()
            
            # Ask to play again
            print("\n" + "----------------------------------------------------------")
            play_again = input("Play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("\nThank you for playing! Goodbye!")
                break

    def save_game_history(self):
        """Save game results to history file."""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        except IOError:
            print("Warning: Could not save game history.")
            
    def run(self):
        """Run the CLI application."""
        try:
            # Ensure words directory exists
            if not os.path.exists("words"):
                print("ERROR: 'words' directory not found!")
                print("Please create the directory and add word files.")
                input("Press Enter to exit...")
                return
                
            self.play_game()
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Goodbye!")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            input("Press Enter to exit...")


if __name__ == "__main__":
    app = CLIApp()
    app.run()