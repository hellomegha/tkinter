import tkinter as tk

def build_form(parent):
    tk.Label(parent, text="Username").pack()
    tk.Entry(parent).pack()
    tk.Button(parent, text="Login", command=handle_login).pack()

def handle_login():
    print("Login clicked")

root = tk.Tk()
build_form(root)
root.mainloop()
