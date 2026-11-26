import tkinter as tk

root=tk.Tk()
root.title("login form")
root.geometry("854x480")

label_username=tk.Label(root, text="USERNAME")
label_username.grid(row=0, column=0, pady=5)

entry_username=tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)


label_password=tk.Label(root, text="PASSWORD")
label_password.grid(row=1, column=0, pady=10)

entry_password=tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

login_btn=tk.Button(root, text="Submit")
login_btn.grid(row=2, columnspan=2, column=1)

root.mainloop()