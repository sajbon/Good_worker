import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import pygetwindow as gw
import threading
import time


class Surveillance:
    def __init__(self, root):
        self.root = root
        # Load the animated GIF using Pillow
        self.gif = Image.open("lurking.gif")
        self.gif1 = Image.open("working.gif")

        # Split the GIF into individual frames
        self.frames = [frame.copy() for frame in ImageSequence.Iterator(self.gif)]
        self.frames1 = [frame.copy() for frame in ImageSequence.Iterator(self.gif1)]

        # Create a label widget
        self.label = tk.Label(self.root)
        self.label.pack(ipadx=300, ipady=0)
        self.label1 = tk.Label(self.root)
        self.label1.pack(ipadx=300, ipady=400)

        # Start the animation
        self.counter = 0
        self.update_image(self.counter)

        # Initialize current_url
        self.current_url = ""

        # Start a separate thread for website checking
        self.website_check_thread = threading.Thread(
            target=self.website_check(), args=(self.label, self.label1)
        )
        self.website_check_thread.daemon = (
            True  # Allow the thread to exit when the main program exits
        )
        self.website_check_thread.start()

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

    def website_check(self, label, label1):
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
                print("Open Google Chrome for proper use of GOOD_WORKER")
                self.current_url = ""

            my_string = str.lower(self.current_url)
            my_substring = "instagram"

            if my_string.__contains__(my_substring):
                print("Ty kurwo do roboty")
                # label.destroy()
                # label1.destroy()

            time.sleep(3)
