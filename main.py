from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# With these below two variables only we are going to update the card texts.
word = "Word"
language = "French"
changed = False
times_running = 0
current_set = {}
current_random_number = 0

# --------------------------------------------------------Back End-----------------------------------------------------
# Opening the data file with the help of pandas.
# with open("french_words.csv") as file:
#     data_dict = pandas.read_csv(file)
#     # Converting the data into a dictionary. Without the orient set to records, first we will have all the 100 French
#     # words stored in a dictionary and then well will have another dictionary of English words. But if we use this
#     # function then we can create 100 dictionaries. IN each of them a French word and its English meaning would be
#     # present.
#     data_dict = data_dict.to_dict(orient="records")
#     print(data_dict)
try:
    with open("words_to_learn.csv") as file:
        data_dict = pandas.read_csv(file)
except FileNotFoundError:
    with open("french_words.csv") as file:
        data_dict = pandas.read_csv(file)
finally:
    data_dict = data_dict.to_dict(orient="records")
    print(len(data_dict))


random_choice_limit = len(data_dict)


# ---------------------------------------------------Functions-----------------------------------------------------------
# In this function only we show French word, we give 3 seconds time then we show the english word. Then we wait for the
# click on right or wrong button then the process continues.
def game():
    global word
    global language
    global card_title
    global card_word
    global card_back_img
    global card_front_img
    global changed
    global times_running
    global current_set
    global current_random_number
    global random_choice_limit

    times_running += 1

    random_number = random.randint(0, random_choice_limit)
    current_random_number = random_number

    current_set = data_dict[random_number]

    # Creating a function to show the English word.
    def english():
        global word
        global language
        global card_title
        global card_word
        global changed
        english_word = data_dict[random_number]["English"]
        word = english_word
        language = "English"
        # We are deleting the previously created text because then we will be overlapping. Also, if we don't create it
        # here it will not get updated.
        canvas.delete(card_word)
        canvas.delete(card_title)
        canvas.itemconfig(canvas_image, image=card_back_img)
        card_word = canvas.create_text(400, 263, text=word, fill="white", font="Arial 30 bold")
        card_title = canvas.create_text(400, 150, text=language, fill="white", font="Arial 20 italic")
        changed = True

    def french():
        global language
        global word
        global card_word
        global card_title
        global changed
        language = "French"
        french_word = data_dict[random_number]["French"]
        word = french_word
        canvas.delete(card_word)
        canvas.delete(card_title)
        canvas.itemconfig(canvas_image, image=card_front_img)
        card_word = canvas.create_text(400, 263, text=word, fill="black", font="Arial 30 bold")
        card_title = canvas.create_text(400, 150, text=language, fill="black", font="Arial 20 italic")
        changed = False

    if times_running == 1:
        french()
        # Giving three second time with this function. Then we are calling the English function to show the english
        # word.
        window.after(3000, english)
    else:
        if changed:
            french()
            # Giving three second time with this function. Then we are calling the English function to show the english
            # word.
            window.after(3000, english)


french_list = []
english_list = []

for thing in data_dict:
    word = thing["French"]
    french_list.append(word)
for thing in data_dict:
    word = thing["English"]
    english_list.append(word)

new_dict = {}


def correct():
    global random_choice_limit
    global new_dict
    game()
    random_choice_limit -= 1
    data_dict.remove(current_set)

    data = pandas.DataFrame(data_dict)
    data.to_csv("words_to_learn.csv")


def wrong():
    game()


# -------------------------------------------------User Interface ------------------------------------------------------
# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas. Using it to put an image on to the screen.
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Text in canvas
card_title = canvas.create_text(400, 150, text=language, font="Arial 20 italic")
card_word = canvas.create_text(400, 263, text=word, font="Arial 30 bold")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
# Right Button
correct_image = PhotoImage(file="right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=correct)
correct_button.grid(row=1, column=0)
# Wrong Button
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=1)

# If we don't call the function here then while we are starting the program, just the words, "Title" and "Word" will be
# only displayed because it is the starting.
game()

window.mainloop()
