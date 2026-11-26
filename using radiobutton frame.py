import tkinter as tk

def submit_form():
    print("Gender:", gender_var.get())
    print("Daily Updates:", "Yes" if daily_var.get() else "No")
    print("Weekly Summary:", "Yes" if weekly_var.get() else "No")
    print("Age:", age_spinbox.get())

#def clear_form():
   #gender_var.set("")
  # daily_var.set("")
  # weekly_var.set("")

# Root window
root = tk.Tk()
root.title("User Preferences Form")
root.geometry("300x300")

# Variables
gender_var = tk.StringVar(value="Male")
daily_var = tk.IntVar()
weekly_var = tk.IntVar()


gender_frame = tk.LabelFrame(root, text="Select Gender", padx=10, pady=10)
gender_frame.pack(padx=10, pady=5, fill="x")

radiobutton=tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male")
radiobutton.pack(anchor="w")
radiobutton=tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female")
radiobutton.pack(anchor="w")
radiobutton=tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other")
radiobutton.pack(anchor="w")


subs_frame = tk.LabelFrame(root, text="Newsletter Subscription", padx=10, pady=10)
subs_frame.pack(padx=10, pady=5, fill="x")

tk.Checkbutton(subs_frame, text="Daily Updates", variable=daily_var).pack(anchor="w")
tk.Checkbutton(subs_frame, text="Weekly Summary", variable=weekly_var).pack(anchor="w")


age_frame = tk.Frame(root)
age_frame.pack(padx=10, pady=10, fill="x")

tk.Label(age_frame, text="Select Age:").pack(anchor="w")
age_spinbox = tk.Spinbox(age_frame, from_=18, to=60, width=10)
age_spinbox.pack(anchor="w")

# Submit 
tk.Button(root, text="Submit", command=submit_form).pack(pady=10)
#tk.Button(root, text="clear", command=clear_form).pack(pady=10)
root.mainloop()

