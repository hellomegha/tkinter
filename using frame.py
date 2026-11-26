import tkinter as tk

def submit_action():
    print("Submitted:", name_var.get(), email_var.get(), age_var.get())

def clear_action():
    name_var.set("")
    email_var.set("")
    age_var.set("")


root = tk.Tk()
root.title("User Form")
root.geometry("300x200")


name_var = tk.StringVar()
email_var = tk.StringVar()
age_var = tk.StringVar()


form_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
form_frame.pack(padx=10, pady=10, fill="x")


tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e", pady=2)
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1)


tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="e", pady=2)
tk.Entry(form_frame, textvariable=email_var).grid(row=1, column=1)


tk.Label(form_frame, text="Age:").grid(row=2, column=0, sticky="e", pady=2)
tk.Entry(form_frame, textvariable=age_var).grid(row=2, column=1)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Submit", command=submit_action).pack(side="left", padx=5)
tk.Button(button_frame, text="Clear", command=clear_action).pack(side="left", padx=5)

root.mainloop()
