from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

saved_websites = []
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LOWERS = "abcdefghijklmnopqrstuvwxyz"
UPPERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
SYMBOLS = "!@#$%^&()*"


def generate():
    gen_pass = []
    pass_length = random.randint(8, 15)
    options = (LOWERS, UPPERS, NUMBERS, SYMBOLS)
    for _ in range(0, pass_length):
        chance = random.choice(options)
        gen_pass.append(random.choice(chance))
    new_pass = str(' '.join(gen_pass))
    new_pass = new_pass.replace(" ", "")
    password_entry.insert(0, new_pass)
    pyperclip.copy(new_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    new_data = {
        web_entry.get(): {
            "email": user_entry.get(),
            "password": password_entry.get()
        }
    }
    if len(password_entry.get()) == 0 or len(user_entry.get()) == 0 or len(web_entry.get()) == 0:
        messagebox.showinfo(title="Danger Danger!", message="Please make sure you entered a field")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()


def search():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        for site in data:
            if site == web_entry.get():
                info = data[site]
                messagebox.showinfo(title=web_entry.get(), message=f"Email:{info['email']}\nPassword:{info['password']}"
                                    )
                pyperclip.copy(info['password'])
                notfound = False
            else:
                notfound = True
    if notfound:
        messagebox.showinfo(title="Not found", message="Sorry can't find that website")
# ---------------------------- UI SETUP ------------------------------- #
WIN = Tk()
HEIGHT, WIDTH = 200, 200
WIN.title("Password Manager")
WIN.config(pady=20, padx=20)
canvas = Canvas(width=WIDTH, height=HEIGHT)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
web_label = Label(text="Website:")
web_label.grid(sticky="E", column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(sticky="E", column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(sticky="E", column=0, row=3)

# entries
web_entry = Entry(width=50)
web_entry.grid(sticky="W", column=1, row=1, columnspan=2)
web_entry.focus()
user_entry = Entry(width=50)
user_entry.grid(sticky="W", column=1, row=2, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(sticky="W", column=1, row=3)
# buttons
generate_button = Button(text="Generate password", command=generate)
generate_button.grid(sticky="W", column=2, row=3, columnspan=2)
save_button = Button(text="Save Password", width=36, command=save_pass)
save_button.grid(sticky="W", column=1, row=4, columnspan=2)
lookup_button = Button(text="Lookup Password", command=search)
lookup_button.grid(sticky="W", column=2, row=1, columnspan=2)

WIN.mainloop()
