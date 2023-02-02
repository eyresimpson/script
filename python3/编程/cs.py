import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

name = simpledialog.askstring("Name", "Enter your name:")
phone = simpledialog.askstring("Phone", "Enter your phone number:")
address = simpledialog.askstring("Address", "Enter your address:")

print("Name: ", name)
print("Phone: ", phone)
print("Address: ", address)
