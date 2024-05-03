
#Declaration
from tkinter import *
import customtkinter as ctk

#Layout
window = ctk.CTk()
window.title  = "History Quiz"
window.geometry("600x400")
window.resizable("false", "false")

#Data - Hashmap for questions, answers as well as options
questions = [
    
    {"Question": "Who created the lightbulb?",
    "options": ["Thomas Edison", "Bob Marley", "Joseph Joestar", "Isaac Newton"],
    "answer": "Answer",
},

    {"Question": "When did the Great Depression start?",
    "options": ["Option1", "Option 2", "Option 3", "Option 4"],
    "answer": "Answer",
},

    {"Question": "Who was the president of Great Britain during WW2?",
    "options": ["Option1", "Option 2", "Option 3", "Option4"],
    "answer": "Answer",
},

    {"Question": "What year did WW2 start?",
    "options": ["Option1", "Option 2", "Option 3","Option4"],
    "answer": "Answer",
},

    {"Question": "When did Captain Cook land?",
    "options": ["Option1", "Option 2", "Option 3", "Option4"],
    "answer": "Answer",
},

]

# variables
score = 0
question_number = 1




# functions

# Checks answer
def answer_check(picked_button):
    question = questions[question_number]

    if option_buttons[picked_button].cget("text") == question["answer"]:
        print ("correct")

    else:
        print("incorrect")

# Displays text from the array onto the buttons

def options_implement(): 
    question = questions[question_number]
    question_label.configure(text = question("Question"))
    options = question("options")
    
    for i in range(4):
      option_buttons[i].configure(text=options[i])
      
      
      


# Frames

start_frame = ctk.CTkFrame(master=window,
                          width= 500,
                          height=400)

main_frame = ctk.CTkFrame(master=window,
                          width= 600,
                          height=500,
                          fg_color="tan",
)

end_frame  = ctk.CTkFrame(master=window,
                          width=500,
                          height=400)

main_frame.pack(expand=True)




# Widgets


question_label = ctk.CTkLabel(
    master=main_frame,
    text="indian",
    width=10,
    height=10,
    bg_color="red"
)
options_implement()
# options buttons

option_buttons = []

for i in range(4):
    option = ctk.CTkButton(
        master=main_frame,
        command=lambda i=i: answer_check(i)
    )
    option.pack()
    option_buttons.append(option)

# checker
checker_label = ctk.CTkLabel(
    master=main_frame,
    width=100,
    height=10,
    bg_color="red",
)

# next button

window.mainloop()
