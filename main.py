from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Quiz Quiz")


# start of the program
def menu():
    global menu_frame
    menu_frame = ttk.LabelFrame(root)
    menu_frame.grid()
    start_button = ttk.Button(menu_frame, text="Start Quiz", command=quiz)
    start_button.grid(row=0, column=0, padx=5, pady=5)


# main quiz program
def quiz():
    menu_frame.destroy()  # destroy Menu
    question_label = Label(root, text="Question")
    question_label.grid(row=0, column=0, padx=5, pady=5)

    def change_text():  # changing the question Label
        global button_counter
        if button_counter == 0:
            question_label.config(text="Question 2")
        elif button_counter == 1:
            question_label.config(text="Question 3")
        elif button_counter == 2:
            question_label.config(text="Question 4")
        elif button_counter == 3:
            question_label.config(text="Question 5")
        elif button_counter == 4:
            question_label.config(text="Question 6")
        elif button_counter == 5:
            question_label.config(text="Question 7")
        elif button_counter == 6:
            question_label.config(text="Question 8")
        elif button_counter == 7:
            question_label.config(text="Question 9")
        else:
            question_label.config(text="Question 10")
        if button_counter != 9:
            button_counter += 1
        else:
            button_counter = 0
    answer1_button = ttk.Button(root, text="A.< >", command=change_text)
    button_counter = 0
    answer1_button.grid(row=1, column=0, padx=5, pady=5)
    answer2_button = ttk.Button(root, text="B.< >", command=change_text)
    answer2_button.grid(row=2, column=0, padx=5, pady=5)
    answer3_button = ttk.Button(root, text="C.< >", command=change_text)
    answer3_button.grid(row=1, column=1, padx=5, pady=5)
    answer4_button = ttk.Button(root, text="D.< >", command=change_text)
    answer4_button.grid(row=2, column=1, padx=5, pady=5)
    confirm_button = ttk.Button(root, text="Confirm")
    confirm_button.grid(row=3, column=0, padx=5, pady=5)

    point2x_button = ttk.Button(root, text="2x point")
    point2x_button.grid(row=0, column=2, padx=5, pady=5)
    hint_button = ttk.Button(root, text="Hints")
    hint_button.grid(row=1, column=2, padx=5, pady=5)
    riddle_button = ttk.Button(root, text="Riddle")
    riddle_button.grid(row=2, column=2, padx=5, pady=5)
    answer_button = ttk.Button(root, text="Skip question")
    answer_button.grid(row=3, column=2, padx=5, pady=5)


root.resizable(False, False)
menu()
root.mainloop()

