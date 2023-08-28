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
        ["A journey of a certain rubber boy.", "a. MHA", "b. One Piece", "c. One Punch Man", "d. God Of High School",
         2],
        ["A scientist in a new stone world.", "a. Dr. Stone", "b. New Game", "c. Dr.Rock", "d. Stone World", 1],
        ["Teen eats a cursed item and turns into a king.", "a. Demon Slayer", "b. Dark Karate", "c. Jujutsu Kaisen",
         "d. Code Geass", 3],
        ["Family bound by the gravity of fate", "a. Hunter Hunter", "b. Dragon Ball Z", "c. Inazuma 11",
         "d. JoJo’s Bizarre Adventure", 4],
        ["Lovestruck man proves himself through basketball", "a. Slam Dunk", "b. Kuroko no Basket", "c. Fruit Basket",
         "d. Dribble", 1],
        ["Humanity in the brink of destruction by the gods.", "a. God Of High school", "b. Saint Young Man",
         "c. Record Of Ragnarok", "d. Overlord", 3],
        ["Man-eating giants terrorize a city.", "a. Hell's Paradise", "b. Attack On Titan", "c. Promised Neverland",
         "d. Giant Killing", 2],
        ["Man reincarnation turns him into a monster demon lord.", "a. Mushoku Tensei",
         "b. That Time I Got Reincarnated as a Slime", "c. Overlord", "d. Goblin Slayer", 2],
        ["Demon king reincarnation lead him to becoming a student.", "a. Seven Deadly Sin", "b. Demon Lord Daimao",
         "c. How Not To Summon A Demon Lord", "d. Misfit Of Demon king Academy", 4],
        ["Boy captivated by the art of his senior gets inspired to start art.", "a. Kill La Kill",
         "b. Honey and Clover", "c. Blue Period", "d. Opus Color", 3]
    ]
    question_frame = ttk.Frame(root)
    question_frame.grid(row=0, column=0)

    def make_question():
        global next_question
        global point
        global button
        try:
            question_label = Label(question_frame, text=anime_prompt[next_question][0])
            question_label.grid(row=0, column=0, padx=5, pady=5)

            answer1_button = ttk.Radiobutton(question_frame, text=anime_prompt[next_question][1], variable=button,
                                             value=1)
            answer1_button.grid(row=1, column=0, padx=5, pady=5)
            answer2_button = ttk.Radiobutton(question_frame, text=anime_prompt[next_question][2], variable=button,
                                             value=2)
            answer2_button.grid(row=2, column=0, padx=5, pady=5)
            answer3_button = ttk.Radiobutton(question_frame, text=anime_prompt[next_question][3], variable=button,
                                             value=3)
            answer3_button.grid(row=1, column=1, padx=5, pady=5)
            answer4_button = ttk.Radiobutton(question_frame, text=anime_prompt[next_question][4], variable=button,
                                             value=4)
            answer4_button.grid(row=2, column=1, padx=5, pady=5)

            next_question += 1

        except IndexError:
            point_label = ttk.Label(question_frame, text="Total Point:\n{}".format(point))
            point_label.grid(row=3, column=2)
            answer.append(point_label)

    def clear_frame():
        # destroy all widgets from frame
        for widget in question_frame.winfo_children():
            widget.destroy()
        check_answer()
        make_question()

    def check_answer():
        global point
        if button.get() == anime_prompt[next_question - 1][5]:
            point += 1

    confirm_button = ttk.Button(root, text="Confirm", command=clear_frame)
    confirm_button.grid(row=3, column=0, padx=5, pady=5)
    make_question()




button = IntVar()
point = 0
next_question = 0
root.resizable(False, False)
menu()
root.mainloop()
