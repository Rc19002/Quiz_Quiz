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
        ["A journey of a certain rubber boy.", "a. test", "b", "c", "d"],
        ["A scientist in a new stone world.", "a. test", "b", "c", "d"],
        ["Teen eats a cursed item and turns into a king.", "a. test", "b", "c", "d"],
        ["Family bound by the gravity of fate", "a. test", "b", "c", "d"],
        ["Lovestruck man proves himself through basketball", "a. test", "b", "c", "d"],
        ["Humanity in the brink of destruction by the gods.", "a. test", "b", "c", "d"],
        ["Man-eating giants terrorize a city.", "a. test", "b", "c", "d"],
        ["Man reincarnation turns him into a monster demon lord.", "a. test", "b", "c", "d"],
        ["Demon king reincarnation lead him to becoming a student.", "a. test", "b", "c", "d"],
        ["Boy captivated by the art of his senior gets inspired to start art.", "a. test", "b", "c", "d"]
    ]



    def make_question():
        global next_question
        question_label = Label(root, text=anime_prompt[next_question][0])
        question_label.grid(row=0, column=0, padx=5, pady=5)
        point_label = Label(root, text="Point: 0")
        point_label.grid(row=3, column=1, padx=5, pady=5)
        button = IntVar()

        answer1_button = ttk.Radiobutton(root, text=anime_prompt[next_question][1], variable=button, value=1)
        answer1_button.grid(row=1, column=0, padx=5, pady=5)
        answer2_button = ttk.Radiobutton(root, text=anime_prompt[next_question][2], variable=button, value=2)
        answer2_button.grid(row=2, column=0, padx=5, pady=5)
        answer3_button = ttk.Radiobutton(root, text=anime_prompt[next_question][3], variable=button, value=3)
        answer3_button.grid(row=1, column=1, padx=5, pady=5)
        answer4_button = ttk.Radiobutton(root, text=anime_prompt[next_question][4], variable=button, value=4)
        answer4_button.grid(row=2, column=1, padx=5, pady=5)
        next_question += 1
    confirm_button = ttk.Button(root, text="Confirm", command=make_question)
    confirm_button.grid(row=3, column=0, padx=5, pady=5)
    make_question()

    point2x_button = ttk.Button(root, text="2x point")
    point2x_button.grid(row=0, column=2, padx=5, pady=5)
    hint_button = ttk.Button(root, text="Hints")
    hint_button.grid(row=1, column=2, padx=5, pady=5)
    riddle_button = ttk.Button(root, text="Riddle")
    riddle_button.grid(row=2, column=2, padx=5, pady=5)
    answer_button = ttk.Button(root, text="Skip question")
    answer_button.grid(row=3, column=2, padx=5, pady=5)

next_question = 0
root.resizable(False, False)
menu()
root.mainloop()
