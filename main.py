from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    box_password.delete(first=30)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 6)
    nr_symbols = random.randint(1, 2)
    nr_numbers = random.randint(1, 2)
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    box_password.insert(0, password)
    pyperclip.copy(password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = box_website.get()
    email = box_email.get()
    password = box_password.get()
    if password=="" or website=="" or email=="":
        messagebox.showwarning(message="please do not leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the detailed entered :\nEmail:{email}"
                                                    f"\n Password: {password}\n Is it ok to save")
        if is_ok:
            with open("data.txt", 'a') as f:
                f.write(f"{website}|{email}|{password}\n")
                box_email.delete(first=0,last=30)
                box_password.delete(first=0,last=30)
                box_website.delete(first=0,last=30)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager app")
# window.minsize(height=400,width=400)
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
image_logo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0,column=1)
label_website = Label(text="Website:")
label_website.grid(row=1,column=0)
label_website.focus()
label_email = Label(text="Email/Username:")
label_email.grid(row=2,column=0)
label_password = Label(text="Password:")
label_password.grid(row=3,column=0)
box_website = Entry(width=35)
box_website.grid(row=1,column=1,columnspan=2)
box_website.config()
box_email = Entry(width=35)

box_email.grid(row=2,column=1,columnspan=2)
box_password = Entry(width=21)
box_password.grid(row=3,column=1)
password_gen = Button(text="Gernerate")
password_gen.grid(row=3,column=2)
password_gen.config(command=create_password)
add_pass = Button(text="Add",width=36)
add_pass.grid(row=4,column=1,columnspan=2)
add_pass.config(command=save)










window.mainloop()