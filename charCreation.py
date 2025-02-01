import tkinter as tk
from tkinter import ttk
import randomRoll
import lists

def show_frame(frame):
    """Hides all frames and then displays the selected one."""
    startFrame.grid_forget()
    rollTablePage.grid_forget()
    frame.grid()

def next_page(selectedRace, selectedProfession, selectedAge):
    """Get the selected values and display them on the second page."""
    race_label.config(text=f"Valt släkte: {selectedRace.get()}")
    profession_label.config(text=f"Valt yrke: {selectedProfession.get()}")
    age_label.config(text=f"Valt ålder: {selectedAge.get()}")
    show_frame(rollTablePage)

def main():
    global root, startFrame, rollTablePage, race_label, profession_label, age_label

    root = tk.Tk()
    root.title("Drakar och Demoner")  # Set window title

    # ========== Frame 1 (First Page) ==========
    startFrame = ttk.Frame(root, padding=20)
    startFrame.grid()

    ttk.Label(startFrame, text="Välj släkte:").grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(startFrame, text="Välj yrke:").grid(column=1, row=0, padx=5, pady=5)
    ttk.Label(startFrame, text="Välj ålder:").grid(column=2, row=0, padx=5, pady=5)

    # Dropdown Menus
    selectedRace = tk.StringVar()
    dropDownSläkte = ttk.Combobox(startFrame, values=lists.races, textvariable=selectedRace)
    dropDownSläkte.grid(column=0, row=1, padx=5, pady=5)
    

    selectedProfession = tk.StringVar()
    dropdownYrke = ttk.Combobox(startFrame, values=lists.professions, textvariable=selectedProfession)
    dropdownYrke.grid(column=1, row=1, padx=5, pady=5)
    

    selectedAge = tk.StringVar()
    dropdownAge = ttk.Combobox(startFrame, values=lists.age, textvariable=selectedAge)
    dropdownAge.grid(column=2,row=1, padx=5,pady=5)
    # Buttons
    ttk.Button(startFrame, text="Exit", command=root.destroy).grid(column=0, row=5, columnspan=3, pady=10)
    # Change view to Frame2 and pass selected values
    ttk.Button(startFrame, text="Next", command=lambda: next_page(selectedRace, selectedProfession, selectedAge)).grid(column=1, row=5, columnspan=2, pady=10)

    # ========== Frame 2 (Next Page) ==========
    rollTablePage = ttk.Frame(root, padding=20)
    
    ttk.Label(rollTablePage, text="Det här är nästa sida!", font=("Arial", 14)).grid(column=0, row=0, padx=5, pady=10)

    # Labels to display selected values
    race_label = ttk.Label(rollTablePage, text="")
    race_label.grid(column=0, row=1, padx=5, pady=5)

    profession_label = ttk.Label(rollTablePage, text="")
    profession_label.grid(column=0, row=2, padx=5, pady=5)

    age_label = ttk.Label(rollTablePage, text="")
    age_label.grid(column=0, row=3,padx=5,pady=5)

    ttk.Button(rollTablePage, text="Back", command=lambda: show_frame(startFrame)).grid(column=0, row=4, padx=5, pady=5)

    # Start with the first frame
    show_frame(startFrame)
    root.mainloop()

if __name__ == "__main__":
    main()

