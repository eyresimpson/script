import tkinter as tk
from tkinter import messagebox


def on_key_press(event):
    messagebox.showinfo("消息", "Hello World")
    root.destroy()


root = tk.Tk()
root.bind("<Control-KeyPress-m>", on_key_press)
root.mainloop()
