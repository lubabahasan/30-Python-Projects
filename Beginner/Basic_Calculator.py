#===================================
# GUI ~ 1hr + 26m + 2hr + 41m
#===================================

import math
import tkinter as tk
import tkinter.font as tkFont

#===================================
#       F U N C T I O N S
#===================================

def append(char):
    input_text.config(state='normal')
    input_text.insert(tk.END, char)
    input_text.config(state='disabled')

def clear():
    input_text.config(state='normal')
    input_text.delete("1.0", tk.END)
    input_text.config(state='disabled')

def backspace():
    expression = input_text.get("1.0", tk.END)[:-2]
    input_text.config(state='normal')
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, expression)
    input_text.config(state='disabled')

history = []

def update_history(expression):
    global history

    history.append(expression)
    input_prev.config(state='normal')
    input_prev.delete("1.0", tk.END)
    lines = "".join(history[-1:])
    print(lines)
    input_prev.insert(tk.END, lines)
    input_prev.config(state="disabled")

def calc():
    try:
        expression = input_text.get("1.0", tk.END)
        expression.strip()
        if '√' in expression:
            result = math.sqrt(int(expression[1:]))
        else:
            result = eval(expression.replace('x', '*').replace('×', '*').replace('÷','/').replace('√','math.sqrt'))
        update_history(expression)
        input_text.config(state='normal')
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, str(result))
        input_text.config(state="disabled")
    except:
        input_text.config(state='normal')
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, "Error")
        input_text.config(state='disabled')

#===================================
#    G U I   C O D E   B E L O W
#===================================

#Style
font = ("Fixedsys", 16)
inp_font = ("Fixedsys", 20)
inp_prev = ("Fixedsys", 14)
sticky_button = tk.W+tk.E

#Dimensions
w_height = 380
w_width = 290

#Colours
bg = 'pink'
eq_bg = "#CA456D"
border = "#600B3D"
func = "#D0A8A8"

root = tk.Tk()

geometry = f'{w_width}x{w_height}'
root.geometry(geometry)
root.configure(bg=border, padx=3, pady=3)
root.title("Basic Caculator")

#border frame
border = tk.Frame(root)
border.config(padx=8, pady=8, bg=eq_bg)

#Input Frame
input_frame = tk.Frame(border)
input_frame.config(bg=eq_bg)

#Input prev
input_prev = tk.Text(input_frame, wrap='word', height=2, font=inp_prev, bg=bg)
input_prev.pack(padx=2)
input_prev.config(state='disabled')

#Input
input_text = tk.Text(input_frame, font=font, height=5, bg=bg)
input_text.bind("<Return>", lambda event: calc())
input_text.pack(padx=2, pady=(0, 2))
input_text.config(state='disabled')

input_frame.pack(fill='x')

#Input button frame
buttonFrame = tk.Frame(border)
buttonFrame.config(bg=eq_bg, pady=5)
buttonFrame.columnconfigure(0, weight=5)
buttonFrame.columnconfigure(1, weight=5)
buttonFrame.columnconfigure(2, weight=5)
buttonFrame.columnconfigure(3, weight=5)

#Input buttons

buttons = [
    ("C", clear),
    ("√", lambda: append('√')),
    ("←", backspace),
    ("÷", lambda: append('÷')),
    ("7", lambda: append('7')),
    ("8", lambda: append('8')),
    ("9", lambda: append('9')),
    ("×", lambda: append('×')),
    ("4", lambda: append('4')),
    ("5", lambda: append('5')),
    ("6", lambda: append('6')),
    ("-", lambda: append('-')),
    ("1", lambda: append('1')),
    ("2", lambda: append('2')),
    ("3", lambda: append('3')),
    ("+", lambda: append('+')),
    (".", lambda: append('.')),
    ("0", lambda: append('0')),
    ("00", lambda: append('00')),
    ("=", calc)
]

key_bind = [
    ("<Delete>", lambda: clear()),
    ("<BackSpace>", lambda: backspace()),
    ("/", lambda: append('÷')),
    ("*", lambda: append('×')),
    ("<Return>", lambda: calc())
]

for digit in "0123456789.+-":
    root.bind(digit, lambda event, d=digit: append(d))

for key, command in key_bind:
    root.bind(key, lambda event, cmd=command: cmd())

row = col = 0

for text, command in buttons:
    if col == 4:
        col -= 1
        col %= 3
        row += 1

    btn = tk.Button(buttonFrame, text=text, font=font, bg = func if text in ['C', '√', '←'] else bg, command= command)
    if text == '=':
        btn.configure(bg=eq_bg)
    btn.grid(row=row, column=col, sticky=sticky_button, padx=2, pady=2)

    col += 1



buttonFrame.pack(fill='x')

border.pack()

root.mainloop()