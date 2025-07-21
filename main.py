import json
from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

letter_list = [password_list.append(choice(letters)) for char in range(randint(8, 10))]
symbol_list = [password_list.append(choice(symbols)) for sym in range(randint(2, 4))]
number_list = [password_list.append(choice(numbers)) for num in range(randint(2, 4))]

shuffle(password_list)

password = "".join(password_list)

def generate_password():
    global password
    password_entry.delete(0,END)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    save_password = password_entry.get()
    new_data = {
        website: {
            "Email":email,
            "Password":save_password
        }
    }
    if website == "" or save_password == "":
        messagebox.showinfo(title="OOPS",message="You should not leave any of the fields empty!!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:  {email}"
                                                              f"\nPassword: {save_password} \nIs it okay to save?")
        if is_ok:
            try:
                with open("new_data.json","r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("new_data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("new_data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# --------------------------DETAIL SEARCH------------------------------ #
def search():
    keyword = website_entry.get()
    try:
        with open("new_data.json","r") as data_file:
            search_data = json.load(data_file)
            if keyword in search_data:
                messagebox.showinfo(title=f"{keyword}", message=f"Email: {search_data[keyword]["Email"]}\n"
                                                                f"Password: {search_data[keyword]["Password"]}")
            else:
                messagebox.showinfo(title=f"{keyword}", message=f"There are no details available for the current entry..")
    except FileNotFoundError:
            messagebox.showinfo(title=f"{keyword}", message=f"There are no details available for the current entry..")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file="logo.png") # ----- GET YOUR OWN LOGO ------ #
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
website_entry = Entry(width=55)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()
search_button = Button(text="Search",width=14,command=search)
search_button.grid(column=2,row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
email_entry = Entry(width=55)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"alanjohn@useless.com")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)
password_entry = Entry(width=36)
password_entry.grid(column=1,row=3)
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=46,command=save)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()
