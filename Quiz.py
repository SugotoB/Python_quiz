
# Imports needed libraries and modules

import customtkinter as ctk
import pygame
pygame.mixer.init()


# Initialize main window
window = ctk.CTk()
window.title("History Quiz")
window.geometry("600x500")
window.resizable(False, False)



# Data - List of dictionaries for questions, answers, and options
questions = [
    {"Question": "Who created the lightbulb?",
     "options": ["Thomas Edison", "Bob Marley", "Joseph Joestar", "Isaac Newton"],
     "answer": "Thomas Edison"},
    {"Question": "What year did the Great Depression start?",
     "options": ["1969", "1826", "1991", "1929"],
     "answer": "1929"},
    {"Question": "Who was the president of Great Britain during WW2?",
     "options": ["Charlie Demelio", "Dio Brando", "Benjamin Franklin", "Winston Churchill"],
     "answer": "Winston Churchill"},
    {"Question": "What year did WW2 start?",
     "options": ["1756", "1982", "1939", "1919"],
     "answer": "1939"},
    {"Question": "What year did Captain Cook land on Australia?",
     "options": ["1669", "200 BC", "2001", "1770"],
     "answer": "1770"},
]

# Variable declarations
score = 0
question_number = 0

# Colour palette
background_color = "#f0f0f0" 
button_color = "#007ACC"
button_hover_color = "#005A9E"
text_color = "#333333"

# Frames for start, end and main quiz
start_frame = ctk.CTkFrame(master=window, fg_color=background_color)
main_frame = ctk.CTkFrame(master=window, fg_color=background_color)
end_frame = ctk.CTkFrame(master=window, fg_color=background_color)

# Frames are set to not resize relative to children and fill the whole screen
start_frame.pack_propagate(False)
main_frame.pack_propagate(False)
end_frame.pack_propagate(False)

start_frame.pack(fill='both', expand=True)
main_frame.pack(fill='both', expand=True)
end_frame.pack(fill='both', expand=True)

# Hides all frames but the start frame
main_frame.pack_forget()
end_frame.pack_forget()

# Sound function assigns sound as the command from pygame and assigns the file parameter for later use.
def play_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.play()

# Function to check the answer, it checks the text of the selected option and pulls data from the array to verify, award scores and changes feedback accordingly.
def answer_check(picked_button):
    global score, question_number
    question = questions[question_number]
    selected = option_buttons[picked_button]

    if selected.cget("text") == question["answer"]:
        score += 1
        checker_label.configure(text="Correct! Nice job!", fg_color="green")
        play_sound("Correct Nice job .wav")
    else:
        checker_label.configure(text="Incorrect. Better luck next time!", fg_color="red")
        play_sound("Incorrect Better luc.wav")
    checker_label.pack(pady=10)
    for i in range(4):
        option_buttons[i].configure(state="disabled")
    next_button.configure(state="normal")

# Function to start the quiz, forgets everything but the main quiz frame
def Enter():
    start_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)
    end_frame.pack_forget()
    implement()

# Function to restart the quiz, resets score and forgets everything but the start frame
def Restart():
    global question_number, score
    question_number = 0
    score = 0
    start_frame.pack(fill='both', expand=True)
    main_frame.pack_forget()
    end_frame.pack_forget()
    implement()

# Function to implement the question and options, data is pulled from the array and a loop is done in a range of 4 in order to generate option buttons.
def implement():
    question = questions[question_number]
    question_label.configure(text=question["Question"], text_color=text_color)
    options = question["options"]
    for i in range(4):
        option_buttons[i].configure(text=options[i], state="normal")
    checker_label.pack_forget()
    next_button.configure(state="disabled")

# Function to move to the next question, updates global number and thus modifies the option and question from using a different index value.
def next():
    global question_number
    question_number += 1
    if question_number < len(questions):
        implement()
    else:
        start_frame.pack_forget()
        main_frame.pack_forget()
        end_frame.pack(fill='both', expand=True)
        scorelabel()

# Function to display the score, changes text of the score_label
def scorelabel():
    score_label.configure(text=f"You scored: {score}/{len(questions)}! Good job!")

# Widgets - makes objects for the code that are going to be displayed.
title_label = ctk.CTkLabel(
    master=start_frame,
    text="Welcome to the History Quiz!",
    font=("Lexend", 32),
    text_color=text_color
)
title_label.pack(pady=40)

enter_button = ctk.CTkButton(
    master=start_frame,
    text="Start Quiz",
    command=Enter,
    border_color="black",
    border_width=1,
    fg_color=button_color,
    hover_color=button_hover_color,
    font=("Lexend", 20),
    width=200,
    height=50
)
enter_button.pack(pady=20)

question_label = ctk.CTkLabel(
    master=main_frame,
    text="",
    text_color=text_color,
    font=("Lexend", 22)
)
question_label.pack(pady=20)

# generates option buttons
# Option buttons
option_buttons = []
for i in range(4):
    option = ctk.CTkButton(
        master=main_frame,
        command=lambda i=i: answer_check(i),
        height=35,
        width=400,
        fg_color=button_color,
        hover_color=button_hover_color,
        font=("Lexend", 18)
    )
    option_buttons.append(option)
    option.pack(pady=10)

# Checker label
checker_label = ctk.CTkLabel(
    master=main_frame,
    corner_radius=5,
    text="",
    width=150,
    height=50,
    font=("Lexend", 16)
)
checker_label.pack(pady=10)

# Next button
next_button = ctk.CTkButton(
    master=main_frame,
    fg_color=button_color,
    hover_color=button_hover_color,
    text="Next",
    state="disabled",
    command=next,
    font=("Lexend", 20),
    width=150,
    height=50
)
next_button.pack(pady=20)

score_label = ctk.CTkLabel(
    master=end_frame,
    text="",
    text_color=text_color,
    font=("Lexend", 22)
)
score_label.pack(pady=20)

# Restart button for end_frame
restart_button = ctk.CTkButton(
    master=end_frame,
    text="Restart Quiz",
    command=Restart,
    fg_color=button_color,
    hover_color=button_hover_color,
    font=("Lexend", 20),
    width=200,
    height=50
)
restart_button.pack(pady=40)

# Score label for end_frame


# Centering widgets in start_frame
title_label.pack(anchor='center')
enter_button.pack(anchor='center')

# Centering widgets in end_frame
score_label.pack(anchor='center')
restart_button.pack(anchor='center')

# Initial implementation, calls the previously defined function to make an initial generation of the quiz
implement()

window.mainloop()