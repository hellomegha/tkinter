import tkinter as tk

Valid_username="Pritha"
Valid_password="pooh"

def validate_fields(*args):
    if username_var.get() and pwd_var.get():
        btn.config(state="normal")
    else:
        btn.config(state="disabled")


def  login():
    username= username_entry.get()
    password= pwd_entry.get()

    if username==Valid_username and password==Valid_password:
        msg_label.config(text="login successful")

    else:
        msg_label.config(text="login unsuccessful")

root=tk.Tk()
root.title("login table")
root.geometry("640x360")

username_var= tk.StringVar()
pwd_var= tk.StringVar()

username_var.trace_add("write", validate_fields)
pwd_var.trace_add("write", validate_fields)

#username
label= tk.Label(root, text="USERNAME")
label.grid(row=0, column=0, pady=10)

username_entry=tk.Entry(root, textvariable=username_var)
username_entry.grid(row=0, column=1, pady=10, padx=10)

#Password
label=tk.Label(root, text="PASSWORD")
label.grid(row=1, column=0, padx=10, pady=10)

pwd_entry=tk.Entry(root, textvariable=pwd_var)
pwd_entry.grid(row=1, column=1, padx=10, pady=10)

btn=tk.Button(root, text="login", state="disabled")
btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

msg_label=tk.Label(root, text="")
msg_label.grid(row=3, columnspan=2)

root.mainloop()


