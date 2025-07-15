#=======================
#   1 hr ~
#=======================

import tkinter as tk
import tkinter.font as tkFont
import time

#=======================
#   F U N C T I O N S
#=======================

def start_timer(h, m, s):

    if h.isdigit() and m.isdigit() and s.isdigit():

        t_seconds = int(h) * 3600 + int(m) * 60 + int(s)

        val = [3600, 60, 1]
        curr_hand = [0,0,0]
        
        while t_seconds != 0:

            temp_seconds = t_seconds

            for i in range(3):
                curr_hand[i] = temp_seconds//val[i]
                temp_seconds -= curr_hand[i]*val[i]
            
            timer_text = f'{curr_hand[0]}:{curr_hand[1]}:{curr_hand[2]}'
            time_label.configure(text=timer_text)
            root.update_idletasks()
            time.sleep(1)
            t_seconds -= 1
            print(timer_text)
    else:
        pass

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
for i in range(3):
    timer_frame.columnconfigure(i, weight=2, pad=10)

#timer input
inputs = []
commands = ["hour", "minute", "second"]

for i in range(3):
    type_label = tk.Label(timer_frame, height=1, font=time_font, bg=bg, text=commands[i])
    type_label.grid(row=0, column=i, sticky="w")
    inputs.append (tk.Spinbox(timer_frame,state="readonly", from_=0, to=99, increment=1, fg='black', font=time_font, readonlybackground=timer_bg))
    inputs[i].grid(row=1, column=i)

timer_frame.pack(padx=20)

#start button
btn = tk.Button(root, text="Start", font=time_font, bg=bg, command=lambda: start_timer(inputs[0].get(), inputs[1].get(), inputs[2].get()))
btn.pack(pady=20)

root.mainloop()