# =====================================
#       Logic + debugging ~ 2.5 hrs
#       GUI ~ 25 + 2hr + 22 + min
# =====================================

import random
import tkinter as tk
import tkinter.font as tkFont

words = ["apple", "table", "chair", "music", "pizza", "house", "smile", "tiger", "magic", "bread", "cloud", "river", "dance", "water", "stone", "green", "orange", "banana", "melon", "cherry", "grapes", "window", "bottle", "blanket", "monster", "circus", "journey", "lantern", "dolphin", "glasses", "mirror", "tunnel", "garden", "pillow", "rocket", "basket", "desert", "planet", "galaxy", "comet", "orbit", "crystal", "whisper", "thunder", "rainbow", "shadow", "silence", "spider", "castle", "forest", "jungle", "magnet", "marble", "pencil", "eraser", "camera", "button", "magnet", "cactus", "hammer", "ladder", "wallet", "jacket", "island", "anchor", "pirate", "dragon", "unicorn", "phoenix", "griffin", "chimera", "mermaid", "kraken", "minotaur", "avalanche", "nightmare", "symphony", "labyrinth", "triangle", "whispering", "kangaroo", "astronaut", "crocodile", "chocolate", "fortune", "eclipse", "balloon", "shadowy", "mystery", "jellyfish", "vampire", "zombie", "werewolf", "puzzle", "warrior", "ninja", "samurai", "castle", "knight", "queen", "crown", "kingdom", "crystal", "potion", "scroll", "beacon", "silence", "candle", "breeze", "whisper", "melody", "rhythm", "harmony", "painting", "sculpture", "artist", "canvas", "theater", "costume", "mask", "treasure", "compass", "lantern", "journal", "voyage", "explorer", "legend", "myth", "talisman", "echo", "silence", "prophecy", "relic", "enigma", "cipher"]

curr_word = random.choice(words).lower()
word = curr_word
curr_word = list(curr_word)
show_word = ["_"] * len(curr_word)

hangman = "HANGMAN"
hangman_count = 0

text = "Guess the word:"

def game_end():
    hangman_label.pack_forget()
    status_label.pack_forget()
    instr.pack_forget()
    letter_input.pack_forget()
    enter.pack_forget()

def update_display():
    word_display.set(" ".join(show_word))
    hangman_display.set("" + hangman[:hangman_count])
    game_text.set(text)


def get_letter():
    global hangman_count
    global text
    global show_word

    letter = letter_input.get('1.0', tk.END).strip().lower()
    letter_input.delete("1.0", tk.END)

    if letter.isalpha() and len(letter)==1:
        if letter in curr_word:
            status_text.set("Correct Guess!")

            for i in range(len(curr_word)):
                if curr_word[i] == letter:
                    show_word[i] = letter

            for i in range (len(curr_word)):
                if curr_word[i] == letter:
                    curr_word[i] = '-'

            if curr_word.count('-') == len(curr_word):
                text = "That's it!"
                game_status.set("CONGRATULATIONS!")
                g_status_label.config(fg=correct)
                enter.config(state="disabled")
                game_end()

        else:
            hangman_count += 1
            status_text.set("Oops, wrong guess...")

            if hangman_count == len(hangman):
                text = "The word was:"
                show_word = list(word)
                game_status.set("G A M E  O V E R")
                g_status_label.config(fg=wrong, font=(custom_font, 18, 'bold'))

                enter.config(state="disabled")
                game_end()

    elif not letter.isalpha():
        status_text.set("Please enter a valid letter in English!")

    else:
        status_text.set("Please enter a single letter!")

    if curr_word.count('-') != len(curr_word) or hangman_count != len(hangman):
        update_display()


# ================================================================== #
#                   G U I   C O D E   B E L O W
# ================================================================== #

root = tk.Tk()

#font
custom_font = "Fixedsys"

#colours
bg = "#4F6EAB"
textc = '#D8DEE9'
correct = '#A3BE8C'
wrong = '#BF616A'
hangmanc = '#EBCB8B'
buttonc = '#D08770'

#GUI window setup
root.geometry("400x520") #window dimensions
root.configure(bg=bg)
root.title("Hangman Game") #game title

#CONST
game_text = tk.StringVar()
word_display = tk.StringVar()
hangman_display = tk.StringVar()
status_text = tk.StringVar()
game_status = tk.StringVar()

#game text
game_text_label = tk.Label(root, textvariable=game_text, font=(custom_font,18), fg='black', bg=bg)
game_text_label.pack(pady=(70, 10))

#Show word
word_label = tk.Label(root, textvariable=word_display, font=(custom_font,16), fg=textc, bg=bg)
word_label.pack(pady=(0, 15))

#show hangman
hangman_label = tk.Label(root, textvariable=hangman_display, font=(custom_font,18), fg=hangmanc, bg=bg)
hangman_label.pack(pady=(0, 15))

#show status text
status_label = tk.Label(root, textvariable=status_text, font=(custom_font,14), bg=bg)
status_label.pack(pady=(0, 15))

#input instruction
instr = tk.Label(root, text="Enter a letter: ", font=(custom_font,14), fg='black', bg=bg)
instr.pack(pady=5)
#input
letter_input = tk.Text(root, height=1, font=(custom_font,16), fg=textc, bg=bg)
letter_input.pack(pady=(0,10), padx=80)

#Enter button
enter = tk.Button(root, text="Enter", font=(custom_font,13), fg='black', bg=buttonc, command=get_letter)
enter.pack(pady=(0, 15), padx=16)

#game status
g_status_label = tk.Label(root, textvariable=game_status, font=(custom_font,18), fg=textc, bg=bg)
g_status_label.pack(pady=20)

update_display()

root.mainloop()


