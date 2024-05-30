# Declaration
import customtkinter as ctk

# lays out initial window
window = ctk.CTk()
window.title("History Quiz")
window.geometry("600x400")
window.resizable(True, True)

# Data - Hashmap for questions, answers as well as options
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

# Frames for start, end and main quiz
start_frame = ctk.CTkFrame(master=window, fg_color="white")
main_frame = ctk.CTkFrame(master=window, fg_color="white")
end_frame = ctk.CTkFrame(master=window, fg_color="white")

# Frames are set to not resize relative to children and fills whole screen
start_frame.pack_propagate(False)
main_frame.pack_propagate(False)
end_frame.pack_propagate(False)

start_frame.pack(fill='both', expand=True)
main_frame.pack(fill='both', expand=True)
end_frame.pack(fill='both', expand=True)

# Hides all frames but the start frame
main_frame.pack_forget()
end_frame.pack_forget()

# Brings in the global variable of score, question sets variables that pull data from the array and uses global variable question_numebr to pick index, same goes with options.
# selected variable pulls data from the option_buttons array and uses picked_button as a index parameter from the answer_check function

def answer_check(picked_button):
    global score, question_number
    question = questions[question_number]
    selected = option_buttons[picked_button]
    options = question["options"]

    if selected.cget("text") == question["answer"]:
        score += 1
        checker_label.configure(text="Correct", fg_color="green")
    else:
        checker_label.configure(text="Incorrect", fg_color="red")
    checker_label.pack()
    for i in range(4):
        option_buttons[i].configure(text=options[i], state="disabled")
    next_button.configure(state="normal")


# Forgets the start and end frame to reveal the main quiz

def Enter():
    start_frame.pack_forget()
    main_frame.pack(fill='both', expand=True)
    end_frame.pack_forget()
    implement()
# Forgets the endframe and mainframe, packs the first frame and resets the score as well as question_number
def Restart():
    global question_number, score
    question_number = 0
    score = 0
    start_frame.pack(fill='both', expand=True)
    main_frame.pack_forget()
    end_frame.pack_forget()
    implement()


# Sets a label pulling the question from the questions array and uses initial value of question_number for display
# Make a loop 4 utilising the array options to set them onto a button loop done after
# Forgets checker_label in order to have it popup later from a function
# sets the state of next button to disabled in order to prevent the user form being able to go forward without selecting an answer

def implement():
    question = questions[question_number]
    question_label.configure(text=question["Question"])
    options = question["options"]
    for i in range(4):
        option_buttons[i].configure(text=options[i], state="normal")
    checker_label.pack_forget()
    next_button.configure(state="disabled")


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

def scorelabel():
    score_label.configure(text=f"You scored: {score}/{len(questions)} good job!")

# Widgets
enter_button = ctk.CTkButton(
    master=start_frame,
    text="Start Quiz",
    command=Enter,
    border_color="black",
    border_width=1,
    fg_color="Grey",
)
enter_button.pack(pady=20)

question_label = ctk.CTkLabel(
    master=main_frame,
    width=10,
    height=10,
    text="",
    fg_color="red"
)
question_label.pack(pady=20)

# Option buttons
option_buttons = []
for i in range(4):
    option = ctk.CTkButton(
        master=main_frame,
        command=lambda i=i: answer_check(i),
        height=30,
        width=400,
        fg_color="blue",
    )
    option_buttons.append(option)
    option.pack(pady=5)

# Checker label
checker_label = ctk.CTkLabel(
    master=main_frame,
    width=100,
    height=50,
    fg_color="red",
)

# Next button
next_button = ctk.CTkButton(
    master=main_frame,

    fg_color="red",
    text="Next",
    state="disabled",
    command=next,
)

next_button.pack(pady=20)

# Restart button for end_frame
restart_button = ctk.CTkButton(
    master=end_frame,
    text="Restart Quiz",
    command=Restart,
    fg_color="blue"
)
restart_button.pack(pady=20)

# Score label for end_frame
score_label = ctk.CTkLabel(
    master=end_frame,
    text="",
    fg_color="blue",
)
score_label.pack(pady=20)




# Initial implementation
implement()

window.mainloop()