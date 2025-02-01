import tkinter as tk
from tkinter import ttk

def valj_alternativ(event):
    valt_varde = dropdown.get()
    label.config(text=f"Du valde: {valt_varde}")

root = tk.Tk()
root.title("Dropdown-meny i Tkinter")

# Skapa en Frame för layout
frame = ttk.Frame(root, padding=20)
frame.grid()

# Skapa en label
label = ttk.Label(frame, text="Välj ett alternativ:")
label.grid(column=0, row=0, padx=5, pady=5)

# Skapa en lista med alternativ
alternativ = ["Äpple", "Banan", "Körsbär", "Druvor"]

# Skapa en dropdown-meny (Combobox)
dropdown = ttk.Combobox(frame, values=alternativ)
dropdown.grid(column=1, row=0, padx=5, pady=5)

# Förval (valfri)
dropdown.current(0)  # Sätter första alternativet som standard

# Koppla en funktion när man väljer ett alternativ
dropdown.bind("<<ComboboxSelected>>", valj_alternativ)

# Skapa en label för att visa valt alternativ
label = ttk.Label(frame, text="")
label.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

root.mainloop()
