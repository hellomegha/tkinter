import tkinter as tk

def greet():
    name = name_entry.get()
    greeting_label.config(text=f"Welcome, {name}!")

root = tk.Tk()
root.geometry("854x480")   
root.title("Greeter")

label=tk.Label(root, text="Enter your name: ")
label.grid(row=0, column=0, pady=5, padx=25)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, pady=5, padx=25)

greet_btn = tk.Button(root, text="Greet", command=greet)
greet_btn.grid(row=1, column=0, columnspan=2, pady=5, padx=25)

greeting_label = tk.Label(root, text="")
greeting_label.grid(row=2, column=0, columnspan=2, pady=5, padx=25)

root.mainloop()
