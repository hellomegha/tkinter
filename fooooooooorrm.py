import tkinter as tk
from tkinter import messagebox, ttk

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    address = entry_address.get()
    city = entry_city.get()
    state = entry_state.get()
    zip_code = entry_zip.get()
    phone = entry_phone.get()
    dob = entry_dob.get()
    country = country_var.get()
    terms_accepted = terms_var.get()

    if not all([name, email, password, gender, address, city, state, zip_code, phone, dob, country]) or country == "Select Country":
        messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
    elif not terms_accepted:
        messagebox.showwarning("Terms Not Accepted", "You must accept the terms and conditions.")
    else:
        messagebox.showinfo("Success", f"Registered Successfully!\n"
                                       f"Name: {name}\nEmail: {email}\nPhone: {phone}\n"
                                       f"DOB: {dob}\nGender: {gender}\nCountry: {country}\n"
                                       f"Address: {address}, {city}, {state} - {zip_code}")

# Helper to add labeled entry
def add_labeled_entry(parent, label_text, show=None):
    frame = tk.Frame(parent)
    frame.pack(fill="x", pady=3)
    tk.Label(frame, text=label_text, width=15, anchor="w").pack(side="left")
    entry = tk.Entry(frame, show=show) if show else tk.Entry(frame)
    entry.pack(fill="x", expand=True)
    return entry

# Main window
root = tk.Tk()
root.title("Three-Frame Register Form")
root.geometry("500x650")
root.resizable(False, False)

# ===== Frame 1: Personal Details =====
frame1 = tk.LabelFrame(root, text="Personal Details", padx=10, pady=10)
frame1.pack(fill="x", padx=20, pady=10)

entry_name = add_labeled_entry(frame1, "Name:")
entry_email = add_labeled_entry(frame1, "Email:")
entry_password = add_labeled_entry(frame1, "Password:", show="*")

gender_frame = tk.Frame(frame1)
gender_frame.pack(fill="x", pady=3)
tk.Label(gender_frame, text="Gender:", width=15, anchor="w").pack(side="left")
gender_var = tk.StringVar()
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")
tk.Radiobutton(gender_frame, text="Other", variable=gender_var, value="Other").pack(side="left")

# ===== Frame 2: Address & Contact =====
frame2 = tk.LabelFrame(root, text="Address & Contact", padx=10, pady=10)
frame2.pack(fill="x", padx=20, pady=10)

entry_address = add_labeled_entry(frame2, "Address:")
entry_city = add_labeled_entry(frame2, "City:")
entry_state = add_labeled_entry(frame2, "State:")
entry_zip = add_labeled_entry(frame2, "Zip Code:")
entry_phone = add_labeled_entry(frame2, "Phone:")
entry_dob = add_labeled_entry(frame2, "Date of Birth:")

country_frame = tk.Frame(frame2)
country_frame.pack(fill="x", pady=3)
tk.Label(country_frame, text="Country:", width=15, anchor="w").pack(side="left")
country_var = tk.StringVar()
country_combo = ttk.Combobox(country_frame, textvariable=country_var, state="readonly")
country_combo['values'] = ["Select Country", "India", "USA", "UK", "Canada", "Australia", "Other"]
country_combo.current(0)
country_combo.pack(fill="x", expand=True)

# ===== Frame 3: Other =====
frame3 = tk.LabelFrame(root, text="Terms & Submit", padx=10, pady=10)
frame3.pack(fill="x", padx=20, pady=10)

terms_var = tk.BooleanVar()
terms_check = tk.Checkbutton(frame3, text="I accept the Terms and Conditions", variable=terms_var)
terms_check.pack(pady=5)

submit_btn = tk.Button(frame3, text="Submit", command=submit_form, bg="green", fg="white", width=15)
submit_btn.pack(pady=10)

root.mainloop()
