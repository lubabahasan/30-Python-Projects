#===================================
# GUI + Logic ~ 4hrs
#===================================

import tkinter as tk
import tkinter.font as tkFont
import random
import time

moves = ["Rock", "Paper", "Scissor"]

#===================================
#        F U N C T I O N S
#===================================

def game_end():
    game_text_label.pack_forget()
    comp_move_label.pack_forget()
    instr.pack_forget()
    buttonFrame.pack_forget()

def update_display():
    opponent_move.set("   ...   ")
    root.update_idletasks()
    root.after(1000, set_score())

def set_score():
    opponent_move.set(random.choice(moves))

    p = player_move.get()
    c = opponent_move.get()

    if p == c:
        pass
    elif (p == "Rock" and c == "Paper") or (p == "Paper" and c == "Scissor") or (p == "Scissor" and c == "Rock"):
        temp = comp_score.get()
        temp += 1
        comp_score.set(temp)
    else:
        temp = player_score.get()
        temp += 1
        player_score.set(temp)

    p = player_score.get()
    c = comp_score.get()

    if c == 10 or p == 10:
        if c == 10:
            game_status.set("G A M E  O V E R")
            g_status_label.config(fg=lose)
        else:
            game_status.set("Y O U  W I N !")
            g_status_label.config(fg=win)

        btn1.config(state="disabled")
        btn2.config(state="disabled")
        btn3.config(state="disabled")
        game_end()

#===================================
#    G U I   C O D E   B E L O W
#===================================

#Style
font = ("Fixedsys", 14)
stat_font = ("Fixedsys", 18)
sticky_button = tk.W+tk.E

#Dimensions
w_height = 450
w_width = 350
inp_height = 5

#Colours
bg = "#A9F39A"
button_bg = "#80C672"
win = "#375A18"
lose = "#72363D"

root = tk.Tk()

geometry = f'{w_width}x{w_height}'
root.geometry(geometry)
root.configure(bg=bg)
root.title("Rock Paper Scissors")

#Var
opponent_move = tk.StringVar()
player_move = tk.StringVar()
comp_score = tk.IntVar(value=0)
player_score = tk.IntVar(value=0)
game_status = tk.StringVar()

#Scores:
score_frame = tk.Frame(root)
score_frame.configure(bg=bg)
score_frame.columnconfigure(0, weight=1)
score_frame.columnconfigure(1, weight=1)
score_frame.columnconfigure(2, weight=1)
score_frame.columnconfigure(3, weight=1)

comp_label = tk.Label(score_frame, text='Computer:', font=font, bg=bg)
comp_label.grid(row=0, column=0, sticky=tk.E)

comp_score_label = tk.Label(score_frame, textvariable=comp_score, font=font, bg=bg)
comp_score_label.grid(row=0, column=1, sticky=tk.W)

player_label = tk.Label(score_frame, text='Player:', font=font, bg=bg)
player_label.grid(row=0, column=2, sticky=tk.E)

player_score_label = tk.Label(score_frame, textvariable=player_score, font=font, bg=bg)
player_score_label.grid(row=0, column=3, sticky=tk.W)

score_frame.pack(fill='x')

#Game Text
game_text_label = tk.Label(root, text="Computer's move:", font=font, bg=bg)
game_text_label.pack(pady=(40, 10))

#Computer's choice
comp_move_label = tk.Label(root, textvariable=opponent_move, font=font, bg=bg)
comp_move_label.pack(pady=(25, 25))

#Input instruction
instr = tk.Label(root, text="Choose your move:", font=font, bg=bg)
instr.pack(pady=(10, 10))

#Input button frame
buttonFrame = tk.Frame(root)
buttonFrame.configure(bg=bg)
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)

#Input buttons
btn1 = tk.Button(buttonFrame, text="Rock", font=font, bg=button_bg, command=lambda: (player_move.set("Rock"), update_display()))
btn1.grid(row=0, column=0, sticky=sticky_button, padx=2, pady=2)

btn2 = tk.Button(buttonFrame, text="Paper", font=font, bg=button_bg, command=lambda: (player_move.set("Paper"), update_display()))
btn2.grid(row=0, column=1, sticky=sticky_button, padx=2, pady=2)

btn3 = tk.Button(buttonFrame, text="Scissor", font=font, bg=button_bg, command=lambda: (player_move.set("Scissor"), update_display()))
btn3.grid(row=0, column=2, sticky=sticky_button, padx=2, pady=2)

buttonFrame.pack()

#Game status
g_status_label = tk.Label(root, textvariable=game_status, font=stat_font, bg=bg)
g_status_label.pack(pady=20)

root.mainloop()