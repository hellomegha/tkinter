import tkinter as tk

root=tk.Tk()
root.title("frame setting")

Top_frame=tk.Frame(root)
Top_frame.pack()

bottom_frame = tk.Frame(root)
bottom_frame.pack()

label=tk.Label(Top_frame, text="top section").grid()
tk.Button(bottom_frame,text="click me").grid()

root.mainloop()