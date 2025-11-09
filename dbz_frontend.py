import tkinter as tk
from tkinter import Listbox

# Read the characters from the text file
with open('characters.md', 'r') as f:
    characters = f.readlines()

# Create the main window
root = tk.Tk()
root.title("Dragon Ball Z Characters")
root.configure(bg='orange')  # Dragon Ball Z theme color (orange like Goku's gi)

# Add title label
title_label = tk.Label(root, text="DRAGONBALL Z", font=('Arial', 24, 'bold'), bg='orange', fg='black')
title_label.pack(pady=10)

# Create a listbox to display the characters
listbox = Listbox(root, bg='lightyellow', fg='black', font=('Arial', 12))
for char in characters:
    listbox.insert(tk.END, char.strip())

listbox.pack(pady=20, padx=20)

# Run the application
root.mainloop()