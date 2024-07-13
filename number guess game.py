import tkinter as tk
from tkinter import messagebox
from random import randint

# Global variables
guesses_left = 10
number_to_guess = 0
player_name = ""
player_age = ""
player_location = ""

def check_guess():
    global guesses_left
    user_guess = entry.get()

    # Check if the user has any more guesses left
    if guesses_left == 0:
        messagebox.showinfo("Game Over", "You've run out of guesses! The number was " + str(number_to_guess))
        window.destroy()
    else:
        try:
            user_guess = int(user_guess)
            guesses_left -= 1

            # Check if user's guess is correct
            if user_guess == number_to_guess:
                messagebox.showinfo("Congratulations", "You guessed it right! The number was " + str(number_to_guess))
                window.destroy()
            else:
                if user_guess < number_to_guess:
                    messagebox.showinfo("Wrong Guess", f"Too low! You have {guesses_left} guesses left.")
                else:
                    messagebox.showinfo("Wrong Guess", f"Too high! You have {guesses_left} guesses left.")
        except ValueError:
            messagebox.showerror("Error", "Invalid Input: Please enter an integer.")
        entry.delete(0, 'end')

def new_game():
    global guesses_left, number_to_guess
    guesses_left = 10
    number_to_guess = randint(1, 100)
    messagebox.showinfo("New Game", "A new game has started! You have 10 guesses to guess the number between 1 and 100.")
    entry.delete(0, 'end')

def get_user_info():
    global player_name, player_age, player_location
    player_name = name_entry.get()
    player_age = age_entry.get()
    player_location = location_entry.get()
    if not player_name or not player_age or not player_location:
        messagebox.showerror("Error", "All fields are required.")
        return
    if not player_age.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return
    info_window.destroy()
    main_game_window()

def info_window():
    global name_entry, age_entry, location_entry, info_window
    info_window = tk.Tk()
    info_window.title("Game Information")
    info_window.geometry("300x250")
    info_window.config(bg="#1E90FF")

    # Create name label and entry
    tk.Label(info_window, text="Name:", bg="#1E90FF", fg="white").pack(padx=10, pady=5)
    name_entry = tk.Entry(info_window)
    name_entry.pack(padx=10, pady=5)

    # Create age label and entry
    tk.Label(info_window, text="Age:", bg="#1E90FF", fg="white").pack(padx=10, pady=5)
    age_entry = tk.Entry(info_window)
    age_entry.pack(padx=10, pady=5)

    # Create location label and entry
    tk.Label(info_window, text="Location:", bg="#1E90FF", fg="white").pack(padx=10, pady=5)
    location_entry = tk.Entry(info_window)
    location_entry.pack(padx=10, pady=5)

    # Create submit button
    tk.Button(info_window, text="Submit", command=get_user_info, bg="#FFD700", fg="black").pack(padx=10, pady=10)

    info_window.mainloop()

def main_game_window():
    global window, entry
    window = tk.Tk()
    window.title("Guess Game")
    window.geometry("300x250")
    window.config(bg="#1E90FF")

    # Create a label with user information
    user_info = f"Name: {player_name} | Age: {player_age} | Location: {player_location}"
    tk.Label(window, text=user_info, bg="#1E90FF", fg="white").pack(padx=10, pady=10)

    # Create a label
    tk.Label(window, text="Guess the number:", bg="#1E90FF", fg="white").pack(padx=10, pady=10)

    # Create an entry box
    entry = tk.Entry(window, width=20)
    entry.pack(padx=10)

    # Create a submit button
    tk.Button(window, text="Submit", command=check_guess, bg="#FFD700", fg="black").pack(padx=10, pady=10)

    # Create a new game button
    tk.Button(window, text="New Game", command=new_game, bg="#FFD700", fg="black").pack(padx=10, pady=10)

    new_game()
    window.mainloop()

info_window()
