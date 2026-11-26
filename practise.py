import tkinter as tk

def icons():
    user_input= entry.get()
    text_output= text_box.get("1.0",tk.END)
    print("Entry value:",user_input)
    print("text box content:",text_output)

root=tk.Tk()
root.title("basic widgets")
root.geometry("648x480")

label=tk.Label(root,text="Welcome, to Tkinter!")
label.pack()

entry=tk.Entry(root)
entry.pack(pady=10)

text_box=tk.Text(root, height=5, width=30)
text_box.pack(pady=5)

button=tk.Button(root, text="submit", command=icons)
button.pack()

root.mainloop()

