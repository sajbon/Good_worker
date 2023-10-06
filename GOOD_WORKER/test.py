import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

def update_image(counter):
    frame = frames[counter]
    tk_image = ImageTk.PhotoImage(frame)
    label.config(image=tk_image)
    label.tk_image = tk_image
    root.after(100, update_image, (counter + 1) % len(frames))

root = tk.Tk()
root.title("Animated GIF Example")

# Load the animated GIF using Pillow
gif = Image.open("lurking.gif")

# Split the GIF into individual frames
frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]

# Create a label widget
label = tk.Label(root)
label.pack()

# Start the animation
update_image(0)

# Start the Tkinter main loop
root.mainloop()