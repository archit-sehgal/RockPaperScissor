import random
import tkinter as tk

a = tk.Tk()
a.title("Rock, Paper, Scissors")
a.geometry("500x300")

bg_color = "#f5f5f5"
button_color = "#4caf50" 
text_color = "#333333"
font_style = ("Helvetica", 14, "bold")

choices = ["rock", "paper", "scissor"]
userScore = 0
CompScore = 0
Comp_Choice = ""


def checkScore():
    global userScore, CompScore
    user_Choice = uC.get()
    try:
        user_Choice = int(user_Choice)
        user_Choice = choices[user_Choice]
    except (ValueError, IndexError):
        user_Choice = "Invalid Choice!"

    if user_Choice == Comp_Choice:
        score.config(text="Match Draw", fg="blue")
    elif (user_Choice == "rock" and Comp_Choice == "paper") or \
         (user_Choice == "paper" and Comp_Choice == "scissor") or \
         (user_Choice == "scissor" and Comp_Choice == "rock"):
        CompScore += 1
        score.config(text=f"Your Score: {userScore}\nComputer's Score: {CompScore}", fg="red")
    else:
        userScore += 1
        score.config(text=f"Your Score: {userScore}\nComputer's Score: {CompScore}", fg="green")

def FindChoice():
    global Comp_Choice
    user_Choice = uC.get()
    Comp_Choice = random.choice(choices)
    try:
        user_Choice = int(user_Choice)
        user_Choice = choices[user_Choice]
    except (ValueError, IndexError):
        user_Choice = "Invalid Choice!"
    checkScore()
    CCLabel.config(text=f"Computer's Choice: {Comp_Choice}", fg="blue")
    UserChoiceLabel.config(text=f"Your Choice: {user_Choice}", fg="green")


master = tk.Label(
    a, text="ROCK, PAPER, SCISSORS (Choose:\n0 for Rock\n1 for Paper\n2 for Scissors)",
    font=font_style, bg=bg_color, fg=text_color
)

uCLabel = tk.Label(
    a, text="Enter your Choice: ", font=font_style, bg=bg_color, fg=text_color
)

uC = tk.Entry(a, borderwidth=2, relief="ridge", font=font_style)

CCLabel = tk.Label(
    a, text="", font=font_style, bg=bg_color, fg=text_color
)

btn = tk.Button(
    a, text="Play", command=FindChoice, bg=button_color, font=font_style, fg="white"
)

UserChoiceLabel = tk.Label(
    a, text="", font=font_style, bg=bg_color, fg=text_color
)

score = tk.Label(
    a, text=f"Your Score: {userScore}\nComputer's Score: {CompScore}",
    font=("Helvetica", 16), bg=bg_color, fg=text_color
)

# Grid Layout
score.grid(row=6, column=0, columnspan=2)
master.grid(row=0, column=0, columnspan=2)
uCLabel.grid(row=1, column=0, sticky="w")
uC.grid(row=1, column=1, sticky="w")
UserChoiceLabel.grid(row=2, column=0, columnspan=2)
CCLabel.grid(row=3, column=0, columnspan=2)
btn.grid(row=5, column=0, columnspan=2)

# Start the tkinter main loop
a.mainloop()
