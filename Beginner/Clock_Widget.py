#=======================
#   1 hr ~
#=======================

import tkinter as tk
import tkinter.font as tkFont
import time

t_seconds = 0
buttons = []
running = pause = False

#=======================
#   F U N C T I O N S
#=======================

def start_timer(h, m, s):

    if h.isdigit() and m.isdigit() and s.isdigit():

        global t_seconds, running

        t_seconds = int(h) * 3600 + int(m) * 60 + int(s)
        running = True
        countdown()

def stop_timer():
    global t_seconds, running, pause

    t_seconds = 0
    time_label.configure(text="0:0:0")

    buttons[1].configure(text="Pause")
    buttons[1].grid_remove()
    buttons[2].grid_remove()
    buttons[0].grid(row=0, column=1)

    running = False
    pause = False

def pause_timer():
    global t_seconds, running, buttons, pause
    running = not running

    if pause:
        buttons[1].configure(text="Pause")
        countdown()
    else:
        buttons[1].configure(text="Continue")

    pause = not pause
    

def countdown():

    global buttons, pause, t_seconds, running

    for i in range(1, 3):
        buttons[i].grid(row=0, column=i)

    val = [3600, 60, 1]
    curr_hand = [0,0,0]
    
    if running and t_seconds >= 0:

        temp_seconds = t_seconds

        for i in range(3):
            curr_hand[i] = temp_seconds//val[i]
            temp_seconds -= curr_hand[i]*val[i]
        
        timer_text = f'{curr_hand[0]}:{curr_hand[1]}:{curr_hand[2]}'
        time_label.configure(text=timer_text)
        t_seconds -= 1
        root.after(1000, countdown)

    elif t_seconds < 0:

        stop_timer()


root = tk.Tk()
root.geometry("300x400")

#=====================
#    G U I  C O D E
#=====================

#STYLE
bg = "#EAD3AC"
timer_bg = "#CDB386"
font = ("Fixedsys", 22)
time_font = ("Fixedsys", 16)

root.configure(bg=bg)

#time label
time_label = tk.Label(root, height=1, font=font, bg=bg, text="0:0:0")
time_label.pack(pady=(60, 40))

#timer frame
timer_frame = tk.Frame(root, bg=bg)    

#timer input
inputs = []
commands = ["hour", "minute", "second"]

for i in range(3):
    timer_frame.columnconfigure(i, weight=2, pad=10)
    type_label = tk.Label(timer_frame, height=1, font=time_font, bg=bg, text=commands[i])
    type_label.grid(row=0, column=i, sticky="w")
    inputs.append (tk.Spinbox(timer_frame,state="readonly", from_=0, to=99, increment=1, fg='black', font=time_font, readonlybackground=timer_bg))
    inputs[i].grid(row=1, column=i)

timer_frame.pack(padx=20)


btn_commands = [lambda: start_timer(inputs[0].get(), inputs[1].get(), inputs[2].get()), 
            lambda: pause_timer(),
            lambda: stop_timer()]

btn_text = ["Start",
            "Pause",
            "Stop"]
btn_frame = tk.Frame(root, bg=bg)    

for i in range(3):
    btn_frame.columnconfigure(i, weight=1, pad=10)
    buttons.append(tk.Button(btn_frame, text=btn_text[i], font=time_font, bg=bg, command=btn_commands[i]))
    if i == 0:
        buttons[i].grid(row=0, column=1)
    
btn_frame.pack()

#start button
# btn = tk.Button(root, text="Start", font=time_font, bg=bg, command=lambda: start_timer(inputs[0].get(), inputs[1].get(), inputs[2].get()))
# btn.pack()

# #stop button
# btn2 = tk.Button(root, text="Stop", font=time_font, bg=bg, command=stop_timer)
# btn2.pack()

# #pause button
# btn3 = tk.Button(root, text="Pause", font=time_font, bg=bg, command=pause_timer)
# btn3.pack()

root.mainloop()