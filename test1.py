from PIL import Image, ImageTk
import tkinter as tk

IMAGE_PATH = '1.jpg'


root = tk.Tk()
root.geometry("1200x800")

canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((200, 200), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Put a tkinter widget on the canvas.
button = tk.Button(root, text="Start")
button_window = canvas.create_window(10, 10, anchor=tk.NW, window=button)

root.mainloop()
