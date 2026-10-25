import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk

def on_click():
    label.config(text="You interacted with the app!")

root = tk.Tk()
root.title("My First Python App")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to my app!", font=("Arial", 16))
label.pack(pady=20)

# FIXED: Removed the custom colors that break on Mac
button = tk.Button(root, text="Click Me!", command=on_click)
button.pack(pady=10)

root.mainloop()




