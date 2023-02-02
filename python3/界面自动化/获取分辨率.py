import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.quit()

print("Screen Resolution: {0}x{1}".format(screen_width, screen_height))
