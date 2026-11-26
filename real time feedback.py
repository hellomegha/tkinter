import tkinter as tk
def update_greeting(*args):
    greeting_var.set(f"Hello,{name_var.grt()}!")

root=tk.Tk()
name_var= tk.StringVar()

greeting_var= tk.StringVar()

name_var.trace_add("write", update_greeting)


