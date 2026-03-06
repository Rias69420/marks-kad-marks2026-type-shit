# Es izvelejos lietot CSV, jo  tas ir vieglāks par XML, un ir vieglāk salasams, un ir lidzīgs JSON failiem. Un tie bija uzdevuma nosacijumi lietot CSV failu formatu.
import csv
import tkinter as tk
from tkinter import ttk, messagebox

FILE = "metals.csv"

# Load CSV data
def load_data():
    for row in tree.get_children():
        tree.delete(row)

    with open(FILE, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        for line in reader:
            tree.insert("", tk.END, values=line)


# Add band
def add_band():
    band = band_entry.get()
    album = album_entry.get()
    year = year_entry.get()
    power = power_var.get()

    if band == "" or album == "" or year == "":
        messagebox.showwarning("Error", "Fill all fields")
        return

    new_row = [band, album, year, power]

    with open(FILE, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)

    load_data()

    band_entry.delete(0, tk.END)
    album_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)


# Window
root = tk.Tk()
root.title("Power Metal Database")
root.geometry("720x480")
root.configure(bg="#111111")

# Style
style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview",
                background="#1a1a1a",
                foreground="white",
                rowheight=25,
                fieldbackground="#1a1a1a")

style.configure("Treeview.Heading",
                background="#8b0000",
                foreground="white",
                font=("Arial", 10, "bold"))

style.configure("TLabel",
                background="#111111",
                foreground="white")

style.configure("TButton",
                background="#8b0000",
                foreground="white")

style.map("TButton",
          background=[("active", "#b30000")])

# Title
title = tk.Label(root,
                 text="Nu tas relaxing music",
                 bg="#111111",
                 fg="#ff3333",
                 font=("Arial", 18, "bold"))

title.pack(pady=10)

# Table
tree = ttk.Treeview(root,
                    columns=("Band", "Album", "Year", "PowerMetal"),
                    show="headings")

tree.heading("Band", text="Band")
tree.heading("Album", text="Album")
tree.heading("Year", text="Year")
tree.heading("PowerMetal", text="Power Metal")

tree.column("Band", width=180)
tree.column("Album", width=220)
tree.column("Year", width=80)
tree.column("PowerMetal", width=100)

tree.pack(pady=15)

# Form
form = ttk.Frame(root)
form.pack(pady=10)

ttk.Label(form, text="Band").grid(row=0, column=0, padx=8, pady=6)
band_entry = ttk.Entry(form)
band_entry.grid(row=0, column=1)

ttk.Label(form, text="Album").grid(row=1, column=0, padx=8, pady=6)
album_entry = ttk.Entry(form)
album_entry.grid(row=1, column=1)

ttk.Label(form, text="Year").grid(row=2, column=0, padx=8, pady=6)
year_entry = ttk.Entry(form)
year_entry.grid(row=2, column=1)

power_var = tk.BooleanVar()
ttk.Checkbutton(form, text="Power Metal", variable=power_var).grid(row=3, columnspan=2)

# Buttons
buttons = ttk.Frame(root)
buttons.pack(pady=10)

ttk.Button(buttons, text="Load Data", command=load_data).grid(row=0, column=0, padx=10)
ttk.Button(buttons, text="Add Band", command=add_band).grid(row=0, column=1, padx=10)

root.mainloop()