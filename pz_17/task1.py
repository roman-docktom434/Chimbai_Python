import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Event Registration Form")
root.geometry("500x500")
root.configure(bg="white")

# Мягкий шрифт
FONT_MAIN = ("Segoe UI", 11)
FONT_SUB = ("Segoe UI", 9)
ENTRY_WIDTH = 30

header = tk.Label(root, text="EVENT REGISTRATION FORM", font=("Segoe UI", 16, "bold"),
                  bg="black", fg="white")
header.pack(fill="x", pady=10)

form_frame = tk.Frame(root, bg="white")
form_frame.pack(pady=20, padx=20, fill="x")

form_frame.grid_columnconfigure(1, weight=1)
form_frame.grid_columnconfigure(2, weight=1)

# Name
tk.Label(form_frame, text="Name", font=FONT_MAIN, bg="white", anchor="w").grid(row=0, column=0, sticky="w", pady=(0,2))
first_name_entry = tk.Entry(form_frame, width=15, bg="#e5e5e5", font=FONT_MAIN, relief="flat")
first_name_entry.grid(row=0, column=1, sticky="ew", padx=(0, 10), pady=(0,2))
last_name_entry = tk.Entry(form_frame, width=15, bg="#e5e5e5", font=FONT_MAIN, relief="flat")
last_name_entry.grid(row=0, column=2, sticky="ew", pady=(0,2))
tk.Label(form_frame, text="First Name", font=FONT_SUB, bg="white", fg="grey", anchor="w").grid(row=1, column=1, sticky="w", padx=(0, 10))
tk.Label(form_frame, text="Last Name", font=FONT_SUB, bg="white", fg="grey", anchor="w").grid(row=1, column=2, sticky="w")

# Company
tk.Label(form_frame, text="Company", font=FONT_MAIN, bg="white", anchor="w").grid(row=2, column=0, sticky="w", pady=(14, 2))
company_entry = tk.Entry(form_frame, width=ENTRY_WIDTH, bg="#e5e5e5", font=FONT_MAIN, relief="flat")
company_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=(14,2))

# Email
tk.Label(form_frame, text="Email", font=FONT_MAIN, bg="white", anchor="w").grid(row=3, column=0, sticky="w", pady=(14, 2))
email_entry = tk.Entry(form_frame, width=ENTRY_WIDTH, bg="#e5e5e5", font=FONT_MAIN, relief="flat")
email_entry.grid(row=3, column=1, columnspan=2, sticky="ew", pady=(14,2))

# Phone
tk.Label(form_frame, text="Phone", font=FONT_MAIN, bg="white", anchor="w").grid(row=4, column=0, sticky="w", pady=(14, 2))
phone_area_entry = tk.Entry(form_frame, width=8, bg="#e5e5e5", font=FONT_MAIN, relief="flat")
phone_area_entry.grid(row=4, column=1, sticky="ew", pady=(14,2), padx=(0, 10))
phone_number_entry = tk.Entry(form_frame, width=18, bg="#e5e5e5", font=FONT_MAIN, relief="flat")
phone_number_entry.grid(row=4, column=2, sticky="ew", pady=(14,2))
tk.Label(form_frame, text="Area Code", font=FONT_SUB, bg="white", fg="grey", anchor="w").grid(row=5, column=1, sticky="w", padx=(0, 10))
tk.Label(form_frame, text="Phone Number", font=FONT_SUB, bg="white", fg="grey", anchor="w").grid(row=5, column=2, sticky="w")

# Subject
tk.Label(form_frame, text="Subject", font=FONT_MAIN, bg="white", anchor="w").grid(row=6, column=0, sticky="w", pady=(14, 2))
subject_combo = ttk.Combobox(form_frame, values=["Морковь", "Картошка", "Лук"],
                            width=ENTRY_WIDTH, state="readonly", font=FONT_MAIN)
subject_combo.set("Выберите услугу")
subject_combo.grid(row=6, column=1, columnspan=2, sticky="ew", pady=(14,2))

# Existing customer (radio)
tk.Label(form_frame, text="Are you an existing customer?", font=FONT_MAIN, bg="white", anchor="w").grid(row=7, column=0, sticky="w", pady=(14, 2))
customer_var = tk.IntVar(value=0)
radio_frame = tk.Frame(form_frame, bg="white")
radio_frame.grid(row=7, column=1, columnspan=2, sticky="w", pady=(14, 2))
tk.Radiobutton(radio_frame, text="Yes", value=1, variable=customer_var, bg="white", font=FONT_MAIN).pack(side="left", padx=10)
tk.Radiobutton(radio_frame, text="No", value=2, variable=customer_var, bg="white", font=FONT_MAIN).pack(side="left", padx=10)

# Кнопка REGISTER (без тени, мягкий цвет, без закругления)
register_button = tk.Button(
    root,
    text="REGISTER",
    font=("Segoe UI", 13, "bold"),
    bg="#FF6F61",  # мягкий красный
    fg="white",
    width=18,
    relief="flat",
    activebackground="#FF8A80",
    activeforeground="white"
)
register_button.pack(anchor="e", padx=40, pady=30)

root.mainloop()
