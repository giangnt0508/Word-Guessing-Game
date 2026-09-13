"""
ICT401 Assessment 3 - Word Guessing Game Engine
Student Name: Truong Giang Nguyen
Student ID: 202572186
Date: 14/09/2026
Description: Core game logic engine
"""
import random
import os
from typing import Dict, List, Tuple, Optional


class GameEngine:
    def __init__(self):
        """Initialize the game engine with default values."""
        self.secret_word = ""
        self.word_hint = ""
        self.guessed_letters = []
        self.remaining_lives = 6
        self.score = 0
        self.game_over = False
        self.game_won = False
        self.difficulty = ""
        self.max_lives = 6
        
    def load_word_from_file(self, difficulty: str = "easy") -> bool:
        """
        Load a random word and its hint from the appropriate difficulty file
        Args: difficulty (str): Difficulty level - "easy", "medium", or "hard"
        Returns: bool
        """
        self.difficulty = difficulty.lower()
        file_path = f"words/{self.difficulty}.txt"
        
        try:
            if not os.path.exists(file_path):
                return False
                
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
            if not lines:
                return False
                
            # Parse lines with format: word|hint
            words_list = []
            for line in lines:
                line = line.strip()
                if '|' in line:
                    parts = line.split('|', 1)
                    if len(parts) == 2:
                        word = parts[0].strip().upper()
                        hint = parts[1].strip()
                        if word and hint:  # Ensure both are non-empty
                            words_list.append((word, hint))

            if not words_list:
                return False

            # Select random word
            self.secret_word, self.word_hint = random.choice(words_list)
            self.reset_game()
            return True
            
        except Exception:
            return False
    
    def reset_game(self):
        """Reset game state for a new game."""
        self.guessed_letters = []
        self.remaining_lives = self.max_lives
        self.game_over = False
        self.game_won = False
        self.score = 0
        
    def get_display_word(self) -> str:
        """Get the hidden word display with underscores for unguessed letters"""
        if not self.secret_word:
            return ""
            
        display = []
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display.append(letter)
            else:
                display.append("_")
        return " ".join(display)
    
    def validate_guess(self, guess: str) -> Tuple[bool, str]:
        """
        Validate and process a letter guess
        Args: guess (str): The guessed letter
        Returns: Tuple[bool, str]: (is_valid, message)
        """
        if self.game_over:
            return False, "Game is already over. Start a new game"
            
        # Validate input
        if not guess:
            return False, "Please enter a letter."
            
        guess = guess.strip().upper()
        
        if len(guess) != 1:
            return False, "Please enter a single letter."
            
        if not guess.isalpha():
            return False, "Please enter a letter (A-Z)."
            
        if guess in self.guessed_letters:
            return False, f"You already guessed '{guess}'. Try another letter."
            
        # Process valid guess
        self.guessed_letters.append(guess)

        if guess in self.secret_word:
            # +10 for each time the guessed letter appears in the word
            matches = self.secret_word.count(guess)
            self.score += matches * 10

            word_completed = True # Check if word is complete

            # Check each letter in the secret word
            for letter in self.secret_word:
                if letter not in self.guessed_letters:
                    word_completed = False
                    break

            if word_completed:
                self.game_over = True
                self.game_won = True
                return True, f"Congratulations! You won! The word was '{self.secret_word}'."
            return True, f"Correct! '{guess}' appears {matches} time(s) in the word."
        else:
            # Wrong guess
            self.remaining_lives -= 1
            if self.remaining_lives <= 0:
                self.game_over = True
                self.game_won = False
                return True, f"Game Over! The word was '{self.secret_word}'. Better luck next time!"
            return True, f"Wrong! '{guess}' is not in the word. {self.remaining_lives} lives remaining."
    
    def get_game_state(self) -> Dict:
        """ Get the current game state as a dictionary. """
        return {
            "secret_word": self.secret_word,
            "hint": self.word_hint,
            "guessed_letters": self.guessed_letters.copy(),
            "remaining_lives": self.remaining_lives,
            "score": self.score,
            "game_over": self.game_over,
            "game_won": self.game_won,
            "display_word": self.get_display_word(),
            "difficulty": self.difficulty
        }