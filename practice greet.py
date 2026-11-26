import tkinter as tk

def greet():
    name = name_entry.get()
    greet_label.config(text=f"Hi, there! {name}")

root=tk.Tk()
root.title("greetings")
root.geometry("680x440")

greet_label= tk.Label(root, text="")
greet_label.grid(row=2, columnspan=2, column=1, pady=10)

top_label=tk.Label(root, text="Enter your name: ")
top_label.grid(row=0, column=0, pady=15)

name_entry=tk.Entry(root)
name_entry.grid(row=0, column=1, pady=15, padx=10)

greet_btn=tk.Button(root, text="Click", command=greet)
greet_btn.grid(row=1, columnspan=2, column=1, pady=10, padx=5)

root.mainloop()