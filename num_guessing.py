import tkinter as tk
import random
from tkinter import messagebox

# Generate a random number
secret_number = random.randint(1, 100)

# Function to check guess
def check_guess():
    guess = entry.get()
    if not guess.isdigit():
        messagebox.showinfo("Error", "Please enter a valid number.")
        return
    guess = int(guess)
    if guess == secret_number:
        messagebox.showinfo("🎉 Result", f"Correct! The number was {secret_number}")
        window.destroy()
    elif guess < secret_number:
        result_label.config(text="🔼 Too low! Try again.")
    else:
        result_label.config(text="🔽 Too high! Try again.")

# GUI setup
window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("300x200")

tk.Label(window, text="Guess a number between 1 and 100").pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=5)

tk.Button(window, text="Check", command=check_guess).pack(pady=5)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
