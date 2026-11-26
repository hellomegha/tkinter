
# Solution: Age and Email Validation Form

import tkinter as tk

def validate_age(value):
    return value.isdigit() or value == ""

def submit():
    age = age_var.get()
    email = email_var.get()
    error_label.config(text="")

    if not age:
        error_label.config(text="Age is required.")
    elif not email:
        error_label.config(text="Email is required.")
    elif "@" not in email or "." not in email:
        error_label.config(text="Invalid email format.")
    else:
        print("Age:", age)
        print("Email:", email)
        error_label.config(text="Form submitted successfully.", fg="green")

root = tk.Tk()
root.title("Validation Form")
root.geometry("300x220")

age_var = tk.StringVar()
email_var = tk.StringVar()

tk.Label(root, text="Enter Age:").pack(anchor="w", padx=10, pady=(10, 0))
vcmd = (root.register(validate_age), '%P')
tk.Entry(root, textvariable=age_var, validate="key", validatecommand=vcmd).pack(fill="x", padx=10)

tk.Label(root, text="Enter Email:").pack(anchor="w", padx=10, pady=(10, 0))
tk.Entry(root, textvariable=email_var).pack(fill="x", padx=10)

tk.Button(root, text="Submit", command=submit).pack(pady=10)

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()