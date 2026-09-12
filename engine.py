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