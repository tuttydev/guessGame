import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    global guesses_left
    user_guess = entry.get()
    
    if guesses_left == 0:
        messagebox.showinfo("Game Over", "You've run out of guesses! The number was " + str(number_to_guess))
        window.destroy()
    else:
        try:
            user_guess = int(user_guess)
            guesses_left -= 1

            if user_guess == number_to_guess:
                messagebox.showinfo("Congratulations", "You guessed it right! The number was " + str(number_to_guess))
                window.destroy()
            else:
                if user_guess < number_to_guess:
                    messagebox.showinfo("Wrong Guess", "Too low! You have " + str(guesses_left) + " guesses left.")
                else:
                    messagebox.showinfo("Wrong Guess", "Too high! You have " + str(guesses_left) + " guesses left.")
        except:
            messagebox.showerror("Error", "Invalid Input")
    
    entry.delete(0, 'end')

def reset_game():
    global number_to_guess, guesses_left
    number_to_guess = random.randint(1, 100)
    guesses_left = 5
    messagebox.showinfo("New Game", "A new game has started! You have 5 guesses.")
    
def quit_game():
    window.destroy()

number_to_guess = random.randint(1, 100)
guesses_left = 5

window = tk.Tk()
window.title("tuttyDev Guessing Game 2024")
window.configure(bg='lightblue')

label = tk.Label(window, text="Guess the number (1-100):", bg='lightblue')
label.pack()

entry = tk.Entry(window)
entry.pack()

submit_button = tk.Button(window, text="Submit", command=check_guess)
submit_button.pack()

reset_button = tk.Button(window, text="Reset Game", command=reset_game)
reset_button.pack()

quit_button = tk.Button(window, text="Quit Game", command=quit_game)
quit_button.pack()

window.geometry("300x200") 
window.resizable(False,False)

window.mainloop()
