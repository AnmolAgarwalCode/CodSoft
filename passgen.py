import random
import string
import tkinter as tk
from tkinter import messagebox as msg

def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        msg.showerror("Oops!", "Please enter a valid password length (greater than 0).")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    characters = ''.join(random.sample(characters, len(characters))) 

    password = (random.choice(string.ascii_lowercase) +
                random.choice(string.ascii_uppercase) +
                random.choice(string.digits) +
                random.choice(string.punctuation) +
                ''.join(random.choice(characters) for _ in range(length - 4)))

    password = ''.join(random.sample(password, len(password)))  

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(fg="dark green")  

def accept_password():
    username = username_entry.get()
    password = password_entry.get()
    msg.showinfo("Welcome!", f"Hello {username}! Your password has been generated.\n\nUsername: {username}\nPassword: {password}")

root = tk.Tk()
root.title('Secure Password Generator')

title_label = tk.Label(root, text='Password Generator', font=('Helvetica', 20, 'bold'), fg='blue')
title_label.pack(pady=20)

username_frame = tk.Frame(root)
username_frame.pack(pady=5)

tk.Label(username_frame, text='Username:', font=('Helvetica', 14, 'bold')).pack(side=tk.LEFT)
username_entry = tk.Entry(username_frame, width=20, font=('Helvetica', 14))
username_entry.pack(side=tk.RIGHT)

tk.Label(root, text='Password Length:', font=('Helvetica', 14, 'bold')).pack()
length_entry = tk.Entry(root, width=10, font=('Helvetica', 14))
length_entry.pack(pady=5)

password_entry = tk.Entry(root, width=30, font=('Helvetica', 14), borderwidth=2, justify="center")
password_entry.pack(pady=5)

generate_button = tk.Button(root, text='Generate Password', command=generate_password, font=('Helvetica', 12), bg='blue', fg='white')
generate_button.pack(pady=10)

accept_button = tk.Button(root, text='Accept', command=accept_password, font=('Helvetica', 12))
accept_button.pack(pady=5)

reject_button = tk.Button(root, text='Create My Own Password', command=root.quit, font=('Helvetica', 12))
reject_button.pack(pady=5)

root.mainloop()
