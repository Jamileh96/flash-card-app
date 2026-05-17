

# ----------------------------FLASH CARDS CREATION ------------------------------- #
import pandas
import random
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict("records")
    

    

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(card, image=card_front)
    timer = window.after(3000, flip_card)

# ----------------------------FLIP THE CARDS------------------------------- #

def flip_card():
    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"],fill="white")
# ----------------------------SAVING PROGRESS ------------------------------- #
def is_know():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
import tkinter
window = tkinter.Tk()
window.title("Flashy")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)
timer = window.after(3000, flip_card)


canvas = tkinter.Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front= tkinter.PhotoImage(file="images/card_front.png")
card_back= tkinter.PhotoImage(file="images/card_back.png")

card = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2, sticky="EW")
card_title = canvas.create_text(400,150,text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263,text="Description", font=("Arial", 60, "bold"))

wrong_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = tkinter.PhotoImage(file="images/right.png")
wrong_button = tkinter.Button(image=right_image, highlightthickness=0, command=is_know)
wrong_button.grid(row=1, column=1)


next_card()































window= window.mainloop()
