import tkinter as tk

def open_file():
    status_label.config(text="Open Clicked")

def save_file():
    status_label.config(text="Save Clicked")

def exit_app():
    root.quit()

root= tk.Tk()
root.title("Toolbar example")
root.geometry("500x400")

toolbar = tk.Frame(root, bd=1, relief="raised")
tk.Button(toolbar, text="Open", command=open_file).pack(pady=2, padx=2, side="left")
tk.Button(toolbar, text="Save", command=save_file).pack(pady=2, padx=2, side="left")
tk.Button(toolbar, text="Exit", command=exit_app).pack(pady=2, padx=2, side="left")
toolbar.pack(side="top", fill="x" )

text_area =tk.Text(root,wrap="word")
text_area.pack(expand=True, fill="both")

status_label = tk.Label(root, text="ready", relief="sunken", anchor="w")
status_label.pack(side="bottom", fill="x")

root.mainloop()