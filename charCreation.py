import tkinter as tk
from tkinter import ttk
import randomRoll
import lists





def main():
    root = tk.Tk()
    root.title("Dragons and Demons")  # Set window title

    frm = ttk.Frame(root, padding=20)
    frm.grid()

    # Labels for the dropdown menus
    ttk.Label(frm, text="Select Race:").grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(frm, text="Select Profession:").grid(column=1, row=0, padx=5, pady=5)
    ttk.Button(frm, text="Random", command=randomRoll.randomSläkte).grid(column=0, row=2, padx=5,pady=5)
    ttk.Button(frm, text="Random", command=randomRoll.randomYrke).grid(column=1, row=2, padx=5,pady=5)


    # Create dropdown menus 
    dropDownSläkte = ttk.Combobox(frm, values=lists.races)
    dropDownSläkte.grid(column=0, row=1, padx=5, pady=5)

    dropdownYrke = ttk.Combobox(frm, values=lists.professions)
    dropdownYrke.grid(column=1, row=1, padx=5, pady=5)


    # Exit button
    ttk.Button(frm, text="Exit", command=root.destroy).grid(column=0, row=5, columnspan=3, pady=10)
    ttk.Button(frm, text="Nästa").grid(column=1, row=5, columnspan=2, pady=10)
    root.mainloop()




if __name__ == "__main__":
    main()
