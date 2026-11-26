import tkinter as tk

def toggle_password():
    if show_var.get():
        pwd_entry.config(show="")
    else:
        pwd_entry.config(show="*")

def check_password(*args):
    if pwd_var.get():
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

def submit_password():
    print("Submitted Password: ", pwd_var.get())

root = tk.Tk()
root.title("password box")
root.geometry("640x360")

pwd_var=tk.StringVar()
pwd_var.trace_add("write", check_password)

show_var=tk.BooleanVar()

label=tk.Label(root,text="Enter Password:")
label.grid(row=0, column=0, pady=10, padx=5)


pwd_entry = tk.Entry(root, textvariable=pwd_var, show="*")
pwd_entry.grid(row=0, column=1, padx=10, pady=10)

checkbox=tk.Checkbutton(root, text="show", variable=show_var, command=toggle_password)
checkbox.grid(row=1, column=1, padx=15, pady=10)

submit_btn=tk.Button(root, text="submit", state="disabled", command="submit_password")
submit_btn.grid(row=2, columnspan=2, pady=10)

root.mainloop()


