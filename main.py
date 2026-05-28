import os
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
WORDS = "/data/french_words.csv"
dir_path = os.path.dirname(os.path.realpath(__file__)) # get the path of the current file

def right():
    """
    when the user clicks the right button, do something
    """
    pass
def wrong():
    """
    when the user clicks the wrong button, do something
    """
    pass

# UI setup
def create_window():
    """
    create a window, set a title, set the size, and set the padding
    """
    window.title("Flashy") # set the title of the window
    window.config(padx=50, pady=50) # set the padding of the window
    window.tk.call("tk_setPalette", BACKGROUND_COLOR) # set the background color of the window
def create_canvas(card_side, title, word):
    """
    create a canvas
    """
    global canvas, title_text, word_title
    card_img = PhotoImage(file=dir_path + f"/images/card_{card_side}.png") # create an image

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0) # create a canvas
    canvas.card_img = card_img # assign the image to a variable
    canvas.create_image(400, 263, image=card_img) # place the image

    title_text = canvas.create_text(400, 150, text=title, fill="black", font=(FONT_NAME, 40, "italic"))
    word_title = canvas.create_text(400, 263, text=word, fill="black", font=(FONT_NAME, 60, "bold"))

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
create_canvas("front", "French", "Word") # call the function to create the canvas
create_btns() # call the function to create the buttons
window.mainloop() # continuously run the program