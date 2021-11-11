from tkinter import *
import tkinter as tk
import string
import random
import pyperclip
import sqlite3



def password_generator():
    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(char, 18))
    pyperclip.copy(password)
    user = accentry.get("1.0", END)
    pswdlbl["text"] = f"{password}"
    conn = sqlite3.connect("sample.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO account values (?, ?)", (user, password))
    cur.close()
    conn.commit()
    conn.close()

def see_password():
    password = ""
    user = accentry.get("1.0", END)
    conn = sqlite3.connect("sample.db")
    cur = conn.cursor()
    cur.execute('Select * from account')
    for row in cur:
        if row[0] == user:
           accpasslbl["text"]=f"{row[1]}" 
           pyperclip.copy(row[1])
    cur.close()
    conn.commit()
    conn.close()

def tryn():
    accpasslbl["text"] = "hello"

#the main window
root = tk.Tk()

#title of the main window
root.title("Password Manager")


#size of the main window
root.geometry("800x500")


#first message to the user
welcomelbl = tk.Label(text="Welcome to your password manager")
welcomelbl.pack()


#Enter account name
acclbl = tk.Label(text="Account: ")
acclbl.place(x = 30, y = 50)
accentry = tk.Text(bd = 5, height=1, width=30)
accentry.place(x=100, y =45)
accbtn = tk.Button(text="Generate password", command=password_generator)
accbtn.place(x=30, y = 95)


#See password of already existing account
seepwdbtn = tk.Button(text="See password", command=see_password)
seepwdbtn.place(x=35, y=130)
accpasslbl = tk.Label()
accpasslbl.place(x = 220, y=135)



#Retrieve string
pswdlbl = tk.Label()
pswdlbl.place(x = 520, y = 50)




root.mainloop()
