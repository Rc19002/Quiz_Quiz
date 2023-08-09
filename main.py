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
    question_label = Label(root, text="A story of a rubber boy.")
    question_label.grid(row=0, column=0, padx=5, pady=5)
    point_label = Label(root, text="Point: 0")
    point_label.grid(row=3, column=1, padx=5, pady=5)

    def change_text():  # changing the question Label
        if Button.counter == 0:
            question_label.config(text="a scientist is the new stone world")
        elif Button.counter == 1:
            question_label.config(text="Question 3")
        elif Button.counter == 2:
            question_label.config(text="Question 4")
        elif Button.counter == 3:
            question_label.config(text="Question 5")
        elif Button.counter == 4:
            question_label.config(text="Question 6")
        elif Button.counter == 5:
            question_label.config(text="Question 7")
        elif Button.counter == 6:
            question_label.config(text="Question 8")
        elif Button.counter == 7:
            question_label.config(text="Question 9")
        else:
            question_label.config(text="Question 10")
        if Button.counter != 1000:
            Button.counter += 1
        else:
            Button.counter = 0

    def answer_change():  # changing the answer button
        if Button.counter == 0:
            answer1_button.config(text="Dr. Stone")
            answer2_button.config(text="")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 1:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 2:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")

        elif Button.counter == 3:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 4:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 5:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 6:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 7:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        else:
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        if Button.counter != 8:
            Button.counter += 1
        else:
            Button.counter = 0
        pass

    answer1_button = ttk.Button(root, text="A. MHA")
    answer1_button.grid(row=1, column=0, padx=5, pady=5)
    answer2_button = ttk.Button(root, text="B. One Piece")
    answer2_button.grid(row=2, column=0, padx=5, pady=5)
    answer3_button = ttk.Button(root, text="C. One Punch Man")
    answer3_button.grid(row=1, column=1, padx=5, pady=5)
    answer4_button = ttk.Button(root, text="D. God of High school")
    answer4_button.grid(row=2, column=1, padx=5, pady=5)
    confirm_button = ttk.Button(root, text="Confirm", command=change_text)
    Button.counter = 0
    confirm_button.grid(row=3, column=0, padx=5, pady=5)

    point2x_button = ttk.Button(root, text="2x point")
    point2x_button.grid(row=0, column=2, padx=5, pady=5)
    hint_button = ttk.Button(root, text="Hints")
    hint_button.grid(row=1, column=2, padx=5, pady=5)
    riddle_button = ttk.Button(root, text="Riddle")
    riddle_button.grid(row=2, column=2, padx=5, pady=5)
    answer_button = ttk.Button(root, text="Skip question", command=change_text)
    answer_button.grid(row=3, column=2, padx=5, pady=5)


root.resizable(False, False)
menu()
root.mainloop()
