import tkinter as tk

root=tk.Tk()
root.title("User form")
root.geometry("300x200")

def submit_action():
    print("submitted:", name_var.get(), email_var.get(), age_var.get())

def clear_action():
    name_var.set("")
    email_var.set("")
    age_var.set("")


name_var=tk.StringVar()
email_var=tk.StringVar()
age_var=tk.StringVar()

form_frame = tk.Frame(root, relief="groove", bd=2, padx=10, pady=10)
form_frame.pack(pady=10, padx=10, fill="x")
##NAME
label_name=tk.Label(form_frame, text="Name:")
label_name.grid(row=0, column=0)

entry_name=tk.Entry(form_frame, textvariable=name_var)
entry_name.grid(row=0, column=1)

#Email
label_email=tk.Label(form_frame, text="Email:")
label_email.grid(row=1, column=0)

entry_name=tk.Entry(form_frame, textvariable=email_var)
entry_name.grid(row=1, column=1)

#age
label_age=tk.Label(form_frame, text="Age:")
label_age.grid(row=2, column=0)

entry_name=tk.Entry(form_frame, textvariable=age_var)
entry_name.grid(row=2, column=1)

button_frame=tk.Button(root)
button_frame.pack(pady=10)

button=tk.Button(button_frame, text="submit", command=submit_action)
button.pack(side="left", padx=10)

button=tk.Button(button_frame, text="clear", command=clear_action )
button.pack(side="left", padx=10)

root.mainloop()