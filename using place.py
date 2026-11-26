import tkinter as tk


root=tk.Tk()
root.title("place layout")
root.geometry("640x480")

label_place=tk.Label(root, text="PLACED")
label_place.place(x=100,y=20)

entry_place=tk.Entry(root)
entry_place.place(x=80,y=100)
btn_place=tk.Button(root,text="Submit")
btn_place.place(x=120,y=160)

root.mainloop()