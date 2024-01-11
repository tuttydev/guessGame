import tkinter as tk
from tkinter import messagebox
from random import randint

# Global variables
guesses_left = 10
number_to_guess = 0
player_name = ""
player_age = ""
player_location = ""

# Function to check user input
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
                    messagebox.showinfo("Wrong Guess", "Too low! You have " + str(guesses_left) + " guesses left.")
                else:
                    messagebox.showinfo("Wrong Guess", "Too high! You have " + str(guesses_left) + " guesses left.")
        except:
            messagebox.showerror("Error", "Invalid Input")

    entry.delete(0, 'end')

# Function to start a new game
def new_game():
    global guesses_left, number_to_guess
    guesses_left = 10
    number_to_guess = randint(1, 100)
    messagebox.showinfo("New Game", "A new game has started! You have 10 guesses to guess the number between 1 and 100.")
    entry.delete(0, 'end')

# Function to get user information
def get_user_info():
    global player_name, player_age, player_location
    player_name = name_entry.get()
    player_age = age_entry.get()
    player_location = location_entry.get()
    info_window.destroy()
    new_game()

# Create the information window
info_window = tk.Tk()
info_window.title("Game Information")
info_window.geometry("300x200")
info_window.config(bg="#1E90FF") # Set background color

# Create name label and entry
name_label = tk.Label(info_window, text="Name:", bg="#1E90FF", fg="white")
name_label.pack(padx=10, pady=5)
name_entry = tk.Entry(info_window)
name_entry.pack(padx=10, pady=5)

# Create age label and entry
age_label = tk.Label(info_window, text="Age:", bg="#1E90FF", fg="white")
age_label.pack(padx=10, pady=5)
age_entry = tk.Entry(info_window)
age_entry.pack(padx=10, pady=5)

# Create location label and entry
location_label = tk.Label(info_window, text="Location:", bg="#1E90FF", fg="white")
location_label.pack(padx=10, pady=5)
location_entry = tk.Entry(info_window)
location_entry.pack(padx=10, pady=5)

# Create submit button
submit_btn = tk.Button(info_window, text="Submit", command=get_user_info, bg="#FFD700", fg="black")
submit_btn.pack(padx=10, pady=10)

# Run the information window's event loop
info_window.mainloop()

# Create the main window
window = tk.Tk()
window.title("Guess Game")
window.geometry("300x200")
window.config(bg="#1E90FF") # Set background color

# Create a label with user information
user_info_label = tk.Label(window, text="Name: " + player_name + " | Age: " + player_age + " | Location: " + player_location, bg="#1E90FF", fg="white")
user_info_label.pack(padx=10, pady=10)

# Create a label
label = tk.Label(window, text="Guess the number:", bg="#1E90FF", fg="white")
label.pack(padx=10, pady=10)

# Create an entry box
entry = tk.Entry(window, width=20)
entry.pack(padx=10)

# Create a submit button
submit_btn = tk.Button(window, text="Submit", command=check_guess, bg="#FFD700", fg="black")
submit_btn.pack(padx=10, pady=10)

# Create a new game button
new_game_btn = tk.Button(window, text="New Game", command=new_game, bg="#FFD700", fg="black")
new_game_btn.pack(padx=10)

# Start the game
new_game()

# Run the main event loop
window.mainloop()
