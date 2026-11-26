import tkinter as tk
from tkinter import messagebox
 
def about():
    messagebox.showinfo("about", "This is a simple menu bar example")
    
root=tk.Tk()
root.title("menu bar example")
root.geometry("480x360")

menu_bar = tk.Menu(root)


file_menu = tk.Menu(menu_bar, tearoff=0)

file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
root.mainloop