"""
ICT401 Assessment 3 - Word Guessing Game Graphical User Interface (GUI)
Student Name: Truong Giang Nguyen
Student ID: 202572186
Date: 14/09/2026
Description: Tkinter GUI interface for the Word Guessing Game
"""

import tkinter as tk
from tkinter import messagebox, ttk
from engine import GameEngine
import os
from datetime import datetime


class WordGuessingGameGUI:
    """
    Graphical User Interface for the Word Guessing Game using Tkinter.
    """
    
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Word Guessing Game")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        self.root.configure(bg='#f0f0f0')
        self.center_window(self.root)
        
        self.engine = GameEngine()
        self.history_file = "game_history.txt"
        self.key_buttons = {}
        
        # Ensure words directory exists
        if not os.path.exists("words"):
            os.makedirs("words", exist_ok=True)
            
        self.create_widgets()
        self.root.bind_all('<Key>', self.handle_keypress)
        self.show_difficulty_selection()

    def center_window(self, window):
        """Position a window in the center of the screen."""
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        self.main_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.header_label = tk.Label(
            self.main_frame,
            text="🎯 WORD GUESSING GAME",
            font=('Arial', 24, 'bold'),
            bg='#f0f0f0',
            fg='#2c3e50'
        )
        self.header_label.pack(pady=10)
        
        # Difficulty and status frame
        self.status_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.status_frame.pack(fill=tk.X, pady=5)
        
        self.difficulty_label = tk.Label(
            self.status_frame,
            text="Difficulty: -",
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        self.difficulty_label.pack(side=tk.LEFT, padx=5)
        
        self.score_label = tk.Label(
            self.status_frame,
            text="Score: 0",
            font=('Arial', 12),
            bg='#f0f0f0'
        )
        self.score_label.pack(side=tk.RIGHT, padx=5)
        
        # Word display
        self.word_frame = tk.Frame(self.main_frame, bg='#ffffff', relief=tk.RAISED, bd=2)
        self.word_frame.pack(fill=tk.X, pady=10)
        
        self.word_label = tk.Label(
            self.word_frame,
            text="",
            font=('Arial', 36, 'bold'),
            bg='#ffffff',
            fg='#2c3e50',
            pady=20
        )
        self.word_label.pack()
        
        # Hint
        self.hint_label = tk.Label(
            self.main_frame,
            text="Hint: -",
            font=('Arial', 12, 'italic'),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.hint_label.pack(pady=5)
        
        # Lives display
        self.lives_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.lives_frame.pack(pady=5)
        
        self.lives_label = tk.Label(
            self.lives_frame,
            text="❤️❤️❤️❤️❤️❤️",
            font=('Arial', 20),
            bg='#f0f0f0'
        )
        self.lives_label.pack()
        
        # Guessed letters
        self.guessed_label = tk.Label(
            self.main_frame,
            text="Guessed: ",
            font=('Arial', 11),
            bg='#f0f0f0',
            fg='#7f8c8d'
        )
        self.guessed_label.pack(pady=5)
        
        # Message display
        self.message_frame = tk.Frame(self.main_frame, bg='#ecf0f1', relief=tk.SUNKEN, bd=1)
        self.message_frame.pack(fill=tk.X, pady=5)
        
        self.message_label = tk.Label(
            self.message_frame,
            text="Select difficulty to start!",
            font=('Arial', 11),
            bg='#ecf0f1',
            fg='#2c3e50',
            pady=8
        )
        self.message_label.pack()
        
        # Keyboard frame
        self.keyboard_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.keyboard_frame.pack(pady=15)
        self.create_keyboard()
        
        # Control buttons
        self.control_frame = tk.Frame(self.main_frame, bg='#f0f0f0')
        self.control_frame.pack(pady=10)
        
        self.new_game_btn = tk.Button(
            self.control_frame,
            text="New Game",
            font=('Arial', 12),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=8,
            command=self.show_difficulty_selection
        )
        self.new_game_btn.pack(side=tk.LEFT, padx=10)
        
        self.difficulty_btn = tk.Button(
            self.control_frame,
            text="Change Difficulty",
            font=('Arial', 12),
            bg='#2ecc71',
            fg='white',
            padx=20,
            pady=8,
            command=self.show_difficulty_selection
        )
        self.difficulty_btn.pack(side=tk.LEFT, padx=10)
        
        self.quit_btn = tk.Button(
            self.control_frame,
            text="Quit",
            font=('Arial', 12),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=8,
            command=self.root.quit
        )
        self.quit_btn.pack(side=tk.RIGHT, padx=10)
        
    def create_keyboard(self):
        """Create the virtual keyboard buttons."""
        # Keyboard layout - QWERTY
        rows = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]
        
        for row_idx, row in enumerate(rows):
            frame = tk.Frame(self.keyboard_frame, bg='#f0f0f0')
            frame.pack(pady=3)
            
            for letter in row:
                btn = tk.Button(
                    frame,
                    text=letter,
                    font=('Arial', 12, 'bold'),
                    width=4,
                    height=1,
                    bg='#ecf0f1',
                    fg='#2c3e50',
                    relief=tk.RAISED,
                    bd=2,
                    state=tk.DISABLED,
                    command=lambda l=letter: self.handle_guess(l)
                )
                btn.pack(side=tk.LEFT, padx=2)
                self.key_buttons[letter] = btn
                
    def show_difficulty_selection(self):
        """Show difficulty selection dialog."""
        # Reset game
        self.engine = GameEngine()
        self.update_display()
        
        # Disable keyboard
        self.set_keyboard_state(False)
        
        # Create selection window
        selection = tk.Toplevel(self.root)
        selection.title("Select Difficulty")
        selection.geometry("300x400")
        selection.resizable(False, False)
        selection.transient(self.root)
        selection.grab_set()
        
        tk.Label(
            selection,
            text="🎯 Select Difficulty Level",
            font=('Arial', 16, 'bold'),
            pady=15
        ).pack()
        
        difficulties = [
            ("Easy", "easy", '#2ecc71'),
            ("Medium", "medium", '#f39c12'),
            ("Hard", "hard", '#e74c3c')
        ]
        
        for label, value, color in difficulties:
            btn = tk.Button(
                selection,
                text=label,
                font=('Arial', 14),
                bg=color,
                fg='white',
                width=15,
                pady=10,
                command=lambda d=value, w=selection: self.start_new_game(d, w)
            )
            btn.pack(pady=8)
            
        tk.Button(
            selection,
            text="Cancel",
            font=('Arial', 12),
            bg='#95a5a6',
            fg='white',
            width=15,
            pady=5,
            command=self.root.destroy
        ).pack(pady=10)

        self.center_window(selection)
        
    def start_new_game(self, difficulty, selection_window):
        """
        Start a new game with the selected difficulty.
        
        Args:
            difficulty (str): Selected difficulty
            selection_window: Difficulty selection window
        """
        selection_window.destroy()
        
        # Load word
        if not self.engine.load_word_from_file(difficulty):
            messagebox.showerror(
                "Error",
                f"Could not load word file for {difficulty} difficulty.\n"
                f"Please ensure 'words/{difficulty}.txt' exists and is properly formatted."
            )
            return
            
        # Reset keyboard
        for btn in self.key_buttons.values():
            btn.config(state=tk.NORMAL, bg='#ecf0f1')
            
        self.update_display()
        self.set_message(f"Game started! Guess a letter.", '#2c3e50')
        self.difficulty_label.config(text=f"Difficulty: {difficulty.upper()}")
        
    def handle_guess(self, letter):
        """
        Handle a letter guess from the keyboard.
        
        Args:
            letter (str): Guessed letter
        """
        if self.engine.game_over:
            return
            
        # Disable the clicked button
        self.key_buttons[letter].config(state=tk.DISABLED, bg='#bdc3c7')
        
        # Process guess
        is_valid, message = self.engine.validate_guess(letter)
        
        if is_valid:
            # Update display
            self.update_display()
            self.set_message(message, '#2c3e50')
            
            # Check game over
            state = self.engine.get_game_state()
            if state['game_over']:
                self.handle_game_end()
        else:
            self.set_message(message, '#e74c3c')
            # Re-enable button if invalid (duplicate)
            if "already guessed" in message:
                self.key_buttons[letter].config(state=tk.NORMAL, bg='#ecf0f1')

    def handle_keypress(self, event):
        """Handle a letter pressed on the physical keyboard."""
        letter = event.char.upper()
        if (
            len(letter) == 1
            and letter in self.key_buttons
            and self.key_buttons[letter]['state'] == tk.NORMAL
        ):
            self.handle_guess(letter)
                
    def update_display(self):
        """Update all display elements."""
        state = self.engine.get_game_state()
        
        # Update word display
        self.word_label.config(text=state['display_word'])
        
        # Update hint
        self.hint_label.config(text=f"Hint: {state['hint']}")
        
        # Update lives
        lives = "❤️" * state['remaining_lives'] + "🖤" * (self.engine.max_lives - state['remaining_lives'])
        self.lives_label.config(text=lives)
        
        # Update score
        self.score_label.config(text=f"Score: {state['score']}")
        
        # Update guessed letters
        guessed_text = "Guessed: " + ", ".join(sorted(state['guessed_letters'])) if state['guessed_letters'] else "Guessed: None"
        self.guessed_label.config(text=guessed_text)
        
    def set_message(self, message, color='#2c3e50'):
        """Set the message display."""
        self.message_label.config(text=message, fg=color)
        
    def set_keyboard_state(self, enabled):
        """Enable or disable all keyboard buttons."""
        state = tk.NORMAL if enabled else tk.DISABLED
        for btn in self.key_buttons.values():
            btn.config(state=state)
            
    def handle_game_end(self):
        """Handle the end of the game."""
        state = self.engine.get_game_state()
        
        # Disable keyboard
        self.set_keyboard_state(False)
        
        # Save history
        self.save_game_history()
        
        # Show result
        if state['game_won']:
            self.set_message(f"🎉 YOU WON! The word was '{state['secret_word']}'", '#27ae60')
            self.message_label.config(font=('Arial', 12, 'bold'))
        else:
            self.set_message(f"💔 GAME OVER! The word was '{state['secret_word']}'", '#e74c3c')
            self.message_label.config(font=('Arial', 12, 'bold'))
            
    def save_game_history(self):
        """Save game results to history file."""
        try:
            state = self.engine.get_game_state()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            record = f"{timestamp}|{state['difficulty']}|{state['secret_word']}|{'WON' if state['game_won'] else 'LOST'}|{state['score']}|{len(state['guessed_letters'])}\n"
            
            with open(self.history_file, 'a', encoding='utf-8') as file:
                file.write(record)
                
        except IOError:
            pass


def main():
    """Main entry point for GUI application."""
    root = tk.Tk()
    app = WordGuessingGameGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()