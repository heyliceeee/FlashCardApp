import os
import time
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
WORDS = "/data/french_words.csv"
LEARN = "/data/words_learn.csv"
dir_path = os.path.dirname(os.path.realpath(__file__)) # get the path of the current file


def right():
    """
    when the user clicks the right button, remove the current word from the dictionary and show the next card
    """
    global translations_dict, current_index

    if not translations_dict:
        return # if the dictionary is empty, do nothing

    translations_dict.pop(current_index) # remove the current word from the dictionary
    export_words_learn()  # export the words that I need to learn to a csv
    next_card() # call the function to show the next card
def wrong():
    next_card() # call the function to show the next card
def next_card():
    """
    show the next card
    """
    global current_card, current_index

    if not translations_dict: # if the dictionary is empty
        if os.path.exists(dir_path + LEARN): # check if the file exists
            os.remove(dir_path + LEARN) # remove the file

        create_card("front", "Congratulates", "You finished! 🥳", "black") # show the front card
        wrong_btn.config(state="disabled")
        right_btn.config(state="disabled")
        return

    else: # if the dictionary is not empty
        current_card = get_random_word(translations_dict) # get a random word from the dictionary
        current_index = translations_dict.index(current_card) # get the index of the current word in the dictionary

        first_language_name = list(current_card.keys())[0] # get the first key of the dictionary
        second_language_name = list(current_card.keys())[1] # get the second key of the dictionary

        create_card("front", first_language_name, current_card[first_language_name], "black") # show the front card
        window.after(3000, lambda: create_card("back", second_language_name, current_card[second_language_name], "white")) # show the back card after 3 seconds
def get_random_word(dict):
    """
    get a random word from the dictionary
    :param dict: dictionary
    :return: random word
    """
    return random.choice(dict)
def export_words_learn():
    """
    export the words that I need to learn to a csv
    """
    global translations_dict

    try:
        df = pd.DataFrame.from_dict(translations_dict) # convert the dictionary to a dataframe
        df.to_csv(dir_path + "/data/words_learn.csv", index=False) # export the dataframe to a csv file

    except Exception as e:
        print(f"Error saving CSV: {e}")

# UI setup
def create_window():
    """
    create a window, set a title, set the size, and set the padding
    """
    window.title("Flashy") # set the title of the window
    window.config(padx=50, pady=50) # set the padding of the window
    window.tk.call("tk_setPalette", BACKGROUND_COLOR) # set the background color of the window
def create_card(card_side, title, word, font_color):
    """
    create a canvas
    """
    global canvas, title_text, word_title
    card_img = PhotoImage(file=dir_path + f"/images/card_{card_side}.png") # create an image

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0) # create a canvas
    canvas.card_img = card_img # assign the image to a variable
    canvas.create_image(400, 263, image=card_img) # place the image

    title_text = canvas.create_text(400, 150, text=title, fill=font_color, font=(FONT_NAME, 40, "italic"))
    word_title = canvas.create_text(400, 263, text=word, fill=font_color, font=(FONT_NAME, 60, "bold"))

    canvas.grid(column=0, row=0, columnspan=2) # place the canvas on the window
def create_btns():
    """
    create the buttons, set the text, and place them on the window
    """
    global wrong_btn, right_btn

    wrong_img = PhotoImage(file=f"{dir_path}/images/wrong.png")
    wrong_btn = Button(image=wrong_img, command=wrong, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, highlightthickness=0) # create the button
    wrong_btn.image = wrong_img
    wrong_btn.grid(column=0, row=1) # place the button on the window

    right_img = PhotoImage(file=f"{dir_path}/images/right.png")
    right_btn = Button(image=right_img, command=right, bg=BACKGROUND_COLOR, highlightthickness=0)  # create the button
    right_btn.image = right_img
    right_btn.grid(column=1, row=1)  # place the button on the window

window = Tk() # create a window
create_window() # call the function to create the window
create_btns() # call the function to create the buttons

if os.path.exists(dir_path + LEARN) and os.path.getsize(dir_path + LEARN) > 0: # check if the file exists and is not empty
    df = pd.read_csv(dir_path + LEARN) # read the csv file

else: # if the file does not exist or is empty
    df = pd.read_csv(dir_path + WORDS)  # read the csv file

translations_dict = df.to_dict(orient="records") # convert the dataframe to a dictionary

next_card() # call the function to show the next card

window.mainloop() # continuously run the program