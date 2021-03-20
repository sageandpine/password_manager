from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    print(password)
    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    information = f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n"

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="OOPS!", message="Do not leave any fields blank")
    else:
        with open("data.txt", "a") as data_file:
            data_file.write(information)
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Inputs
website_input = Entry(width=48)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()
email_input = Entry(width=48)
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=24)
password_input.grid(row=3, column=1)

# Buttons
gen_pass_button = Button(width=21, text="Generate Password", command=gen_pass)
gen_pass_button.grid(pady=2, row=3, column=2)
add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()