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

    anime_prompt = [
            ["A journey of a certain rubber boy.", "a", "b", "c", "d", "b"],
            ["A scientist in a new stone world.", "a", "b", "c", "d", "a"],
            ["Teen eats a cursed item and turns into a king.", "a", "b", "c", "d", "c"],
            ["Family bound by the gravity of fate", "a", "b", "c", "d", "d"],
            ["Lovestruck man proves himself through basketball", "a", "b", "c", "d", "a"],
            ["Humanity in the brink of destruction by the gods.", "a", "b", "c", "d", "c"],
            ["Man-eating giants terrorize a city.", "a", "b", "c", "d", "b"],
            ["Man reincarnation turns him into a monster demon lord.", "a", "b", "c", "d", "a"],
            ["Demon king reincarnation lead him to becoming a student.", "a", "b", "c", "d", "d"],
            ["Boy captivated by an art of his senior gets inspired to start art.", "a", "b", "c", "d", "c"]
        ]

    for question in anime_prompt:
        question_label = Label(root, text=question[0])
        question_label.grid(row=0, column=0, padx=5, pady=5)
        point_label = Label(root, text="Point: 0")
        point_label.grid(row=3, column=1, padx=5, pady=5)
        button = IntVar()
        answer1_button = ttk.Radiobutton(root, text=question[0], variable=button, value=1)
        answer1_button.grid(row=1, column=0, padx=5, pady=5)
        answer2_button = ttk.Radiobutton(root, text="B. One Piece", variable=button, value=2)
        answer2_button.grid(row=2, column=0, padx=5, pady=5)
        answer3_button = ttk.Radiobutton(root, text="C. One Punch Man", variable=button, value=3)
        answer3_button.grid(row=1, column=1, padx=5, pady=5)
        answer4_button = ttk.Radiobutton(root, text="D. God of High school", variable=button, value=4)
        answer4_button.grid(row=2, column=1, padx=5, pady=5)
        confirm_button = ttk.Button(root, text="Confirm")
        Button.counter = 0
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
