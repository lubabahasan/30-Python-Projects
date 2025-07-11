#Logic + debugging ~ 2.5 hrs


words = ["apple", "table", "chair", "music", "pizza", "house", "smile", "tiger", "magic", "bread", "cloud", "river", "dance", "water", "stone", "green", "orange", "banana", "melon", "cherry", "grapes", "window", "bottle", "blanket", "monster", "circus", "journey", "lantern", "dolphin", "glasses", "mirror", "tunnel", "garden", "pillow", "rocket", "basket", "desert", "planet", "galaxy", "comet", "orbit", "crystal", "whisper", "thunder", "rainbow", "shadow", "silence", "spider", "castle", "forest", "jungle", "magnet", "marble", "pencil", "eraser", "camera", "button", "magnet", "cactus", "hammer", "ladder", "wallet", "jacket", "island", "anchor", "pirate", "dragon", "unicorn", "phoenix", "griffin", "chimera", "mermaid", "kraken", "minotaur", "avalanche", "nightmare", "symphony", "labyrinth", "triangle", "whispering", "kangaroo", "astronaut", "crocodile", "chocolate", "fortune", "eclipse", "balloon", "shadowy", "mystery", "jellyfish", "vampire", "zombie", "werewolf", "puzzle", "warrior", "ninja", "samurai", "castle", "knight", "queen", "crown", "kingdom", "crystal", "potion", "scroll", "beacon", "silence", "candle", "breeze", "whisper", "melody", "rhythm", "harmony", "painting", "sculpture", "artist", "canvas", "theater", "costume", "mask", "treasure", "compass", "lantern", "journal", "voyage", "explorer", "legend", "myth", "talisman", "echo", "silence", "prophecy", "relic", "enigma", "cipher"]

import random

curr_word = words[random.randint(0, len(words)-1)]
curr_word = curr_word.lower()
word = curr_word

show_word = " _ " * len(curr_word)
print("Guess the word: " + show_word)

show_word = list("_"*len(curr_word))
curr_word = list(curr_word)

hangman = "HANGMAN"
hangman_count = 0

while(True):

    letter = input("Enter a letter: ")
    letter = letter.lower()

    if letter <= "z" and letter >= "a":
        if letter in curr_word:
            for i in range (len(curr_word)):
                if curr_word[i] == letter:
                    show_word[i] = letter

            for i in range (len(curr_word)):
                if curr_word[i] == letter:
                    curr_word[i] = '-'

            print("Correct Guess!")
            for letter in show_word:
                print(" " + letter + " ",end="")
            print("")

            if curr_word.count('-') == len(curr_word):
                print("\nC O N G R A T U L A T I O N S!")
                print("You have guessed the word correctly ^^")
                break

        else:
            hangman_count += 1

            if hangman_count == len(hangman):
                print("G A M E  O V E R")
                print("The word was: " + word)
                break
            else:
                for i in range (0, hangman_count):
                    print(hangman[i],end="")
                print("")
    else:
        print("Please enter a valid letter in English!")

