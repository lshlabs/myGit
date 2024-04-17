import tkinter as tk
import subprocess

def change_color_to_green():
    root.destroy()
    subprocess.run(['python3', 'test place/green.py'])

def change_color_to_red():
    root.destroy()
    subprocess.run(['python3', 'test place/red.py'])

root = tk.Tk()
root.title("Blue")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(side="right")
canvas.create_rectangle(10, 10, 390, 290, fill="blue")

label_red = tk.Label(root, text="Red", fg="red")
label_red.pack()
label_red.bind("<Button-1>", lambda e: change_color_to_red())

label_green = tk.Label(root, text="Green", fg="green")
label_green.pack()
label_green.bind("<Button-1>", lambda e: change_color_to_green())

label_blue = tk.Label(root, text="Blue", fg="blue")
label_blue.pack()

root.mainloop()
