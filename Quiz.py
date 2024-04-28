
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
    
    {"question": "Question1",
    "options": ["Option1", "Option 2", "Option 3", "Option 4"],
    "answer": "Answer",
},

    {"question": "Question2",
    "options": ["Option1", "Option 2", "Option 3", "Option 4"],
    "answer": "Answer",
},

    {"question": "Question3",
    "options": ["Option1", "Option 2", "Option 3", "Option4"],
    "answer": "Answer",
},

    {"question": "Question4",
    "options": ["Option1", "Option 2", "Option 3","Option4"],
    "answer": "Answer",
},

    {"question": "Question5",
    "options": ["Option1", "Option 2", "Option 3", "Option4"],
    "answer": "Answer",
},

]

#scores



score = 0
question_number  = 1
total_questions = 5



# def next():


    

# Widgets


# options
def tick(option_number):
    if (option_number == 1):
        option_variable1.set("on1")
        option_variable2.set("off2")
        option_variable3.set("off3")
        option_variable4.set("off4")
 
    elif (option_number == 2):
        option_variable1.set("off1")
        option_variable2.set("on2")
        option_variable3.set("off3")
        option_variable4.set("off4")

    elif (option_number == 3):
        option_variable1.set("off1")
        option_variable2.set("off2")
        option_variable3.set("on3")
        option_variable4.set("off4")

    elif (option_number == 4):
        option_variable1.set("off1")
        option_variable2.set("off2")
        option_variable3.set("off3")
        option_variable4.set("on4")

option_variable1 = StringVar()
option_variable2 = StringVar()
option_variable3 = StringVar()
option_variable4 = StringVar()

option1 = ctk.CTkCheckBox(window, variable=option_variable1, text="Option1", onvalue="on1", offvalue="off1", command=lambda:tick(1))
option1.pack()

option2 = ctk.CTkCheckBox(window, variable=option_variable2, text="Option2", onvalue="on2", offvalue="off2", command=lambda:tick(2))
option2.pack()

option3 = ctk.CTkCheckBox(window, variable=option_variable3, text="Option3", onvalue="on3", offvalue="off3", command=lambda:tick(3))
option3.pack()

option4 = ctk.CTkCheckBox(window, variable=option_variable4, text="Option4", onvalue="on4", offvalue="off4", command=lambda:tick(4))
option4.pack()



window.mainloop()
