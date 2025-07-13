#==========================
#   Started: 3
#==========================

import tkinter as tk
from PIL import ImageTk, Image
import random
import pygame
import sys
import os


root = tk.Tk()
root.title("Gift For You")

#==========================
#    F U N C T I O N S
#==========================

def animate_gif(canvas, frames, frame_index, image_item, delay):
    canvas.itemconfig(image_item, image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    canvas.after(delay, animate_gif, canvas, frames, frame_index, image_item, delay)

def extract_frames(path):
    global candle_frames

    gifImage = Image.open(path)
    try:
        while True:
            candle_frames.append(ImageTk.PhotoImage(gifImage.copy()))
            gifImage.seek(len(candle_frames)) 
    except EOFError:
        pass

def initiate():
    global cake_png

    message = tk.Label(root, height=2, text=msg, font=msg_font, bg=bg)
    message.pack()

    canvas = tk.Canvas(root, width=450, height=400, bg=bg, highlightthickness=0)
    canvas.pack()

    cake_png = tk.PhotoImage(file = ("Cake.png"))
    image = canvas.create_image(220, 270, image=cake_png)

    extract_frames(("Candle.gif"))

    x_center = 250
    cake_width = 240  
    x_min = x_center - cake_width // 2

    y_start = 90       
    row_height = 6     
    candles_per_row = min(10, candle_no)
    spacing = cake_width // candles_per_row

    for i in range(candle_no):
        row = i // candles_per_row
        col = i % candles_per_row
        y_base = y_start + row * row_height

        # Spread evenly and jitter a little
        x = x_min + col * spacing + random.randint(-5, 5)
        y = y_base + random.randint(0, 2)

        animation_delay = random.randint(100, 200)
        candle_item = canvas.create_image(x, y, image=candle_frames[0])
        animate_gif(canvas, candle_frames, 0, candle_item, animation_delay)

def get_age():
    global candle_no

    age = age_input.get().strip()

    try:
        if age.isalpha():
            raise Exception("I SAID AGE DUMMY")
        candle_no = int(age)
        if candle_no > 100:
            raise Exception("YOU'RE OLD AS HEXK\n T - T")
        elif candle_no < 1:
            raise Exception("YOU HAVE NOT\nBEEN BORN YET\n ;` - ';")
        inp_status.set("YAY")
        root.after(1000, update_display)
    except ValueError as v:
        inp_status.set("THAT AIN'T NO NUMBER\n ಠ_ಠ")
    except Exception as e:
        inp_status.set(e)
        


def update_display():
    instr.pack_forget()
    age_input.pack_forget()
    enter.pack_forget()
    instr2.pack_forget()

    pygame.mixer.init()
    pygame.mixer.music.load(("birthday.mp3"))
    pygame.mixer.music.play()

    initiate()


#===============================
#   G U I  C O D E  B E L O W   
#===============================

#Style
bg = "#84ADCB"
buttonc = "#648CA9"
font = ("Fixedsys", 14)
inp_font = ("Fixedsys", 18)
msg_font = ("Fixedsys", 24)

#Dimensions
w = 500
h = 720

#Var
msg = "Happy Birthday!"
candle_no = 0
inp_status = tk.StringVar()
candle_frames = []

# --------------------------

geo = str(w)+"x"+str(h)
root.geometry(geo)
root.configure(bg=bg, pady=70)

#input instruction
instr = tk.Label(root, text="Enter your age:", font=msg_font, bg=bg)
instr.pack(pady=20)

age_input = tk.Entry(root, font=inp_font, bg=bg)
age_input.pack(pady=(0,10), padx=100)

#Enter button
enter = tk.Button(root, text="Enter", font=inp_font, fg='black', bg=buttonc, command=get_age)
enter.pack(pady=(0, 15), padx=16)
root.bind("<Return>", lambda event, cmd=get_age: cmd())

#input status
instr2 = tk.Label(root, textvariable=inp_status, font=msg_font, bg=bg)
instr2.pack(pady=20)

root.mainloop()