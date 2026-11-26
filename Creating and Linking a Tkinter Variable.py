import tkinter as tk

root=tk.Tk()

name_var=tk.StringVar()

tk.Label(root, textvariable=name_var).pack()

tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Enter your name:").pack()

root.mainloop()


