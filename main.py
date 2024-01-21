import random
import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack()

        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.attempts = 0
        self.max_attempts = 6

        self.draw_hangman()

        self.word_display = tk.Label(self.master, text=self.display_word(), font=("Helvetica", 20))
        self.word_display.pack()

        self.guess_label = tk.Label(self.master, text="Enter a letter:", font=("Helvetica", 14))
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, font=("Helvetica", 18))
        self.guess_button.pack()

    def choose_word(self):
        words = ["python", "hangman", "programming", "computer", "science", "algorithm"]
        return random.choice(words)

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    def draw_hangman(self):
        self.canvas.delete("all")
        self.canvas.create_line(20, 380, 180, 380, width=2)
        self.canvas.create_line(100, 380, 100, 50, width=2)
        self.canvas.create_line(100, 50, 200, 50, width=2)
        self.canvas.create_line(200, 50, 200, 100, width=2)

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a valid single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Information", "You've already guessed that letter. Try again.")
            return

        self.guessed_letters.append(guess)

        if guess not in self.word_to_guess:
            self.attempts += 1
            self.draw_hangman()

        self.word_display.config(text=self.display_word())

        if self.display_word().replace(" ", "") == self.word_to_guess:
            messagebox.showinfo("Congratulations", f"You guessed the word: {self.word_to_guess}")
            self.reset_game()

        if self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The word was: {self.word_to_guess}")
            self.reset_game()

    def reset_game(self):
        self.word_to_guess = self.choose_word()
        self.guessed_letters = []
        self.attempts = 0
        self.word_display.config(text=self.display_word())
        self.guess_entry.delete(0, tk.END)
        self.draw_hangman()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x600")
    root.resizable(False, False)
    root.configure(bg="lightblue")
    
    game = HangmanGame(root)
 
root.mainloop()
