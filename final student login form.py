import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def validate_inputs(name, age, email, gender, password, address, city, state, pincode, phone, dob, country, terms_accepted):
    if not all([name, age, email, gender, password, address, city, state, pincode, phone, dob, country, terms_accepted]):
        return "All fields are required."
    if not age.isdigit():
        return "Age must be a number."
    if "@" not in email or "." not in email:
        return "Invalid email format."
    return None

def clear_form():
    name_var.set("")
    age_var.set("")
    email_var.set("")
    gender_var.set("Male")
    password_var.set("")
    address_var.set("")
    city_var.set("")
    state_var.set("")
    pincode_var.set("")
    phone_var.set("")
    dob_var.set("")
    country_var.set("India")
    terms_var.set(False)
    

def save_to_file(data):
    with open("registrations.txt", "a") as file:
        file.write(data + "\n")

def register_student():
    name = name_var.get()
    age = age_var.get()    
    email = email_var.get()
    gender=gender_var.get()
    password = password_var.get()
    address = address_var.get()
    city = city_var.get()
    state = state_var.get()
    pincode = pincode_var.get()
    phone = phone_var.get()
    dob = dob_var.get()
    country = country_var.get()
    terms_accepted = terms_var.get()

    error = validate_inputs(name, age, email, gender, password, address, city, state, pincode, phone, dob, country, terms_accepted)
    if error:
        messagebox.showerror("Validation Error", error)
        return

    entry = f"{name}, {age}, {gender}, {email}, {password}, {address}, {city}, {state}, {pincode}, {phone}, {dob}, {country}, {terms_accepted}"
    save_to_file(entry)
    messagebox.showinfo("Success", "Student registered successfully.")
    clear_form()

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("848x430")

name_var = tk.StringVar()
age_var = tk.StringVar()
gender_var = tk.StringVar(value="Male")
password_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
city_var = tk.StringVar()
state_var = tk.StringVar()
pincode_var = tk.StringVar()
phone_var = tk.StringVar()
dob_var = tk.StringVar()
country_var = tk.StringVar(value="India")
terms_var = tk.BooleanVar(value=False)


form_frame = tk.LabelFrame(root, text ="Personal Details", padx=10, pady=10)
form_frame.pack(fill="both", padx=20, pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1, pady=10)

tk.Label(form_frame, text="Age:").grid(row=1, column=0, padx=10, sticky="e")
tk.Entry(form_frame, textvariable=age_var).grid(row=1, column=1, pady=10)


tk.Label(form_frame, text="Email").grid(row=2, column=0, sticky="e")
ttk.Entry(form_frame, textvariable=email_var).grid(row=2, column=1, pady=10)

tk.Label(form_frame, text="DOB:").grid(row=3, column=0, sticky="e")
tk.Entry(form_frame, textvariable=dob_var).grid(row=3, column=1, pady=10)

tk.Label(form_frame, text="Gender:").grid(row=4, column=0, sticky="e")
gender_frame = tk.Frame(form_frame)
gender_frame.grid(row=4, column=1, pady=5, sticky="w")
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left")
tk.Radiobutton(gender_frame, text="other", variable=gender_var, value="other").pack(side="left")

frame2 =tk.LabelFrame(root, text="address & other", padx=10, pady=10)
frame2.pack(fill="x", padx=20, pady=10)

tk.Label(frame2, text="address").grid(row=0, column=0, sticky="e")
tk.Entry(frame2, textvariable=address_var).grid(row=0, column=1, pady=10)

tk.Label(frame2, text="city").grid(row=1, column=0, sticky="e")
tk.Entry(frame2, textvariable=city_var).grid(row=1, column=1, pady=10)

tk.Label(frame2, text="state").grid(row=7, column=0, sticky="e")
ttk.Entry(frame2, textvariable=state_var).grid(row=7, column=1, pady=10)

tk.Label(frame2, text="pincode").grid(row=8, column=0, sticky="e")
tk.Entry(frame2, textvariable=pincode_var).grid(row=8, column=1, pady=10)

tk.Label(frame2, text="phone:").grid(row=9, column=0, sticky="e")
tk.Entry(frame2, textvariable=phone_var).grid(row=9, column=1, pady=10)

#tk.Label(frame2, text="dob:").grid(row=10, column=0, sticky="e")
#tk.Entry(frame2, textvariable=dob_var).grid(row=10, column=1, pady=10)

tk.Label(frame2, text="country:").grid(row=11, column=0, sticky="e")
tk.Entry(frame2, textvariable=country_var).grid(row=11, column=1, pady=10)

button_frame = tk.LabelFrame(root, text="terms&condition", pady=10, padx=10)
button_frame.pack(fill="x", padx=20, pady=20)

terms = tk.Checkbutton(button_frame, text="I accept the terms and conditions", variable=terms_var)
terms.pack(pady=10, side="left")
tk.Button(button_frame, text="Register", command=register_student, bg="yellow").pack(side="left", padx=10, pady=15)
tk.Button(button_frame, text="Clear", command=clear_form, bg="red").pack(side="left", padx=10, pady=15)
 
root.mainloop()
