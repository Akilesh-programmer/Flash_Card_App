from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# With these below two variables only we are going to update the card texts.
word = "Word"
language = "French"


# ---------------------------------------------------Functions-----------------------------------------------------------
# This is a function to generate a random french card. It will get activated when we click on right or wrong button.
def generate_random_word():
    global card_word
    global card_title
    global word
    global language
    random_number = random.randint(0, 100)
    french_word = data[random_number]["French"]
    word = french_word
    canvas.delete(card_word)
    card_word = card_word = canvas.create_text(400, 263, text=word, font="Arial 30 bold")


# -------------------------------------------------User Interface ------------------------------------------------------
# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas. Using it to put an image on to the screen.
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Text in canvas
card_title = canvas.create_text(400, 150, text=language, font="Arial 20 italic")
card_word = canvas.create_text(400, 263, text=word, font="Arial 30 bold")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
# Right Button
correct_image = PhotoImage(file="right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=generate_random_word)
correct_button.grid(row=1, column=0)
# Wrong Button
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_random_word)
wrong_button.grid(row=1, column=1)


# --------------------------------------------------------Back End-----------------------------------------------------
# Opening the data file with the help of pandas.
with open("french_words.csv") as file:
    data = pandas.read_csv(file)
    # Converting the data into a dictionary. Without the orient set to records, first we will have all the 100 French
    # words stored in a dictionary and then well will have another dictionary of English words. But if we use this
    # function then we can create 100 dictionaries. IN each of them a French word and its English meaning would be
    # present.
    data = data.to_dict(orient="records")
    print(data)

# If we don't call the function here then while we are starting the program, just the words, "Title" and "Word" will be
# only displayed because it is the starting.
generate_random_word()

window.mainloop()
