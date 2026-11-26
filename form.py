import tkinter as tk

root = tk.Tk()
root.title("Login Form")
root.geometry("300x150")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)


login_button = tk.Button(root, text="Login")
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()