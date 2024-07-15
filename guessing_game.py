import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODIGY INFOTECH - Guessing Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(root, text="Guessing Game", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(root, text="I have generated a random number between 1 and 100.")
        self.instruction_label.pack(pady=5)

        self.guess_label = tk.Label(root, text="Enter your guess:")
        self.guess_label.pack(pady=5)

        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess < 1 or guess > 100:
                messagebox.showerror("Error", "Please enter a number between 1 and 100.")
                return

            self.attempts += 1

            if guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You've guessed the number {self.number_to_guess} correctly in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter an integer.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
