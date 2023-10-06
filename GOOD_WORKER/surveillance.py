import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygetwindow as gw
import threading
import time
from tkinter import messagebox
from tkinter import PhotoImage


class Surveillance:
    def __init__(self, root):
        self.root = root

        # Load the animated GIF using Pillow and Images
        self.gif = Image.open("lurking.gif")
        self.gif1 = Image.open("working.gif")
        self.image = PhotoImage(file="work.jpg")

        # Split the GIF into individual frames
        self.frames = [frame.copy() for frame in ImageSequence.Iterator(self.gif)]
        self.frames1 = [frame.copy() for frame in ImageSequence.Iterator(self.gif1)]

        # Create a label widget
        self.label = tk.Label(self.root)
        self.label.pack(ipadx=300, ipady=0)
        self.label1 = tk.Label(self.root)
        self.label1.pack(ipadx=300, ipady=400)

        # Initialize current_url
        self.current_url = ""

        # Create a variable to be passed to the website_check function
        self.my_substring = "instagram"

        # Start a separate thread for website checking
        self.website_check_thread = threading.Thread(target=self.website_check)
        self.website_check_thread.daemon = (
            True  # Allow the thread to exit when the main program exits
        )
        self.website_check_thread.start()

        # Start the animation
        self.update_image(0)

        # Pop up window with warning if user is about to shut down the app
        if root.protocol("WM_DELETE_WINDOW"):
            root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_image(self, counter):
        frame = self.frames[counter]
        frame1 = self.frames1[counter]
        tk_image = ImageTk.PhotoImage(frame)
        tk_image1 = ImageTk.PhotoImage(frame1)
        self.label.config(image=tk_image)
        self.label1.config(image=tk_image1)
        self.label.tk_image = tk_image
        self.label1.tk_image = tk_image1
        self.root.after(100, self.update_image, (counter + 1) % len(self.frames))

    def website_check(self):
        while True:
            # Find the active Chrome window by checking for "Google Chrome" in the title
            chrome_window = None
            for window in gw.getAllTitles():
                if "Google Chrome" in window:
                    chrome_window = gw.getWindowsWithTitle(window)[0]
                    break

            # Get the URL from the window's title (which usually contains the URL)
            if chrome_window:
                self.current_url = chrome_window.title
                print("Current URL:", self.current_url)
            else:
                print("Google Chrome window not found.")

            my_string = str.lower(self.current_url)

            if my_string.__contains__(self.my_substring):
                Surveillance.open_popup(self)

                self.root.deiconify()
                self.root.attributes("-topmost", True)

                time.sleep(1)

            else:
                time.sleep(1)
                self.root.iconify()

                # self.update_image()

            time.sleep(3)

    def on_closing(self):
        if messagebox.askokcancel(
            "Quit", "What are you doing, don't even think about it. Get back to work..."
        ):
            self.root.destroy()

    def open_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("WARNING!")
        popup.attributes("-topmost", True)

        image_label = tk.Label(popup, image=self.image)
        image_label.pack()

        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)
