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
        ["A journey of a certain rubber boy.", "a. MHA", "b. One Piece", "c. One Punch Man", "d. God Of High School"],
        ["A scientist in a new stone world.", "a. Dr. Stone", "b. New Game", "c. Dr.Rock", "d. Stone World"],
        ["Teen eats a cursed item and turns into a king.", "a. Demon Slayer", "b. Dark Karate", "c. Jujutsu Kaisen", "d. Code Geass"],
        ["Family bound by the gravity of fate", "a. Hunter Hunter", "b. Dragon Ball Z", "c. Inazuma 11", "d. JoJo’s Bizarre Adventure"],
        ["Lovestruck man proves himself through basketball", "a. Slam Dunk", "b. Kuroko no Basket", "c. Fruit Basket", "d. Dribble"],
        ["Humanity in the brink of destruction by the gods.", "a. God Of High school", "b. Saint Young Man", "c. Record Of Ragnarok", "d. Overlord"],
        ["Man-eating giants terrorize a city.", "a. Hell's Paradise", "b. Attack On Titan", "c. Promised Neverland", "d. Giant Killing"],
        ["Man reincarnation turns him into a monster demon lord.", "a. Mushoku Tensei", "b. That Time I Got Reincarnated as a Slime", "c. Overlord", "d. Goblin Slayer"],
        ["Demon king reincarnation lead him to becoming a student.", "a. Seven Deadly Sin", "b. Demon Lord Daimao", "c. How Not To Summon A Demon Lord", "d. Misfit Of Demon king Academy"],
        ["Boy captivated by the art of his senior gets inspired to start art.", "a. Kill La Kill", "b. Honey and Clover", "c. Blue Period", "d. Opus Color"]
    ]



    def make_question():
        global next_question
        question_label = Label(root, text=anime_prompt[next_question][0])
        question_label.grid(row=0, column=0, padx=5, pady=5)
        point = 0
        point_label = Label(root, text="Point: {}".format(point))
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


next_question = 0
root.resizable(False, False)
menu()
root.mainloop()
