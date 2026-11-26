import tkinter as tk

root=tk.Tk()
root.title("frame with grid")
root.geometry("640x360")

form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0)
tk.Entry(form_frame).grid(row=0, column=1)

tk.Label(form_frame, text="Email:").grid(row=1, column=0)
tk.Entry(form_frame).grid(row=1, column=1)

root.mainloop()