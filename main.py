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
    question_label = Label(root, text="A story of a rubber boy")
    question_label.grid(row=0, column=0, padx=5, pady=5)
    point_label = Label(root, text="Point: 0")
    point_label.grid(row=3, column=1, padx=5, pady=5)

    def change_text():  # changing the question Label
        if Button.counter == 0:
            question_label.config(text="a scientist is the new stone world")
            answer1_button.config(text="Dr. Stone")
            answer2_button.config(text="New Game")
            answer3_button.config(text="Dr. Rock")
            answer4_button.config(text="Stone World")
        elif Button.counter == 1:
            question_label.config(text="Teen eats a cursed item and turn into a King")
            answer1_button.config(text="Demon Slayer")
            answer2_button.config(text="Dark Karate")
            answer3_button.config(text="Jujutsu Kaisen")
            answer4_button.config(text="Code Geass")
        elif Button.counter == 2:
            question_label.config(text="Family bound by the gravity of fate")
            answer1_button.config(text="Hunter Hunter")
            answer2_button.config(text="Dragon ball Z")
            answer3_button.config(text="Inazuma 11")
            answer4_button.config(text="JoJo's Bizarre Adventure")
        elif Button.counter == 3:
            question_label.config(text="Lovestruck man proves himself through basketball")
            answer1_button.config(text="Slam Dunk")
            answer2_button.config(text="Kuroko no Basket")
            answer3_button.config(text="Fruit Basket")
            answer4_button.config(text="Dribble")
        elif Button.counter == 4:
            question_label.config(text="Humankind in a brink of destruction by gods")
            answer1_button.config(text="God Of High school")
            answer2_button.config(text="Saint Young Man")
            answer3_button.config(text="Record Of Ragnarok")
            answer4_button.config(text="Overlord")
        elif Button.counter == 5:
            question_label.config(text="Man-eating Giants terrorize cities")
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Attack On Titan")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 6:
            question_label.config(text="Question 8")
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        elif Button.counter == 7:
            question_label.config(text="Question 9")
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        else:
            question_label.config(text="Question 10")
            answer1_button.config(text="Question 2")
            answer2_button.config(text="Question 2")
            answer3_button.config(text="Question 2")
            answer4_button.config(text="Question 2")
        if Button.counter != 1000:
            Button.counter += 1
        else:
            Button.counter = 0

    def point_system():
        point = 0
        Button.counter = 0
        if Button.counter in range 0
        point_label.config(text="Point:{}". format(point))

    button = IntVar()
    answer1_button = ttk.Radiobutton(root, text="A. MHA", variable=button, value=1)
    answer1_button.grid(row=1, column=0, padx=5, pady=5)
    answer2_button = ttk.Radiobutton(root, text="B. One Piece", variable=button, value=2)
    answer2_button.grid(row=2, column=0, padx=5, pady=5)
    answer3_button = ttk.Radiobutton(root, text="C. One Punch Man", variable=button, value=3)
    answer3_button.grid(row=1, column=1, padx=5, pady=5)
    answer4_button = ttk.Radiobutton(root, text="D. God of High school", variable=button, value=4)
    answer4_button.grid(row=2, column=1, padx=5, pady=5)
    confirm_button = ttk.Button(root, text="Confirm", command=lambda: [(change_text(), point_system())])
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
