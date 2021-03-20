from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Nailed it!", message=f"Website: {email} Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No entry found, please add one")

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
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
                    "email": email,
                    "password": password,
                }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS!", message="Do not leave any fields blank")

# Turn data into a json to store it then back to a dictionary to recall it
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                # Updating old data with new data
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving Updated data
                json.dump(data, data_file, indent=4)
        finally:
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
website_input = Entry(width=24)
website_input.grid(row=1, column=1)
website_input.focus()
email_input = Entry(width=48)
email_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=24)
password_input.grid(row=3, column=1)

# Buttons
search_button = Button (width=21, text="Search", command=find_password)
search_button.grid(pady=2, row=1, column=2)
gen_pass_button = Button(width=21, text="Generate Password", command=gen_pass)
gen_pass_button.grid(pady=2, row=3, column=2)
add_button = Button(text="Add", width=46, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()