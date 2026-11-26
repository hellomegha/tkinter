import tkinter as tk

def validate_age(value):
    return value.isdigit() or value == ""

root = tk.Tk()
root.title("Validation Example")

age_var = tk.StringVar()

vcmd = (root.register(validate_age), '%P')

tk.Label(root, text="Enter your age:").pack()
tk.Entry(root, textvariable=age_var, validate="key", validatecommand=vcmd).pack()

root.mainloop()
