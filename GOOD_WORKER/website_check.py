import pygetwindow as gw
import time


def website_check():
    while True:
        # Find the active Chrome window by checking for "Google Chrome" in the title
        chrome_window = None
        for window in gw.getAllTitles():
            if "Google Chrome" in window:
                chrome_window = gw.getWindowsWithTitle(window)[0]
                break

        # Get the URL from the window's title (which usually contains the URL)
        if chrome_window:
            current_url = chrome_window.title
            print("Current URL:", current_url)
        else:
            print("Google Chrome window not found.")

        my_string = str.lower(current_url)
        my_substring = "instagram"

        if my_string.__contains__(my_substring):
            var = 1
            print("Do roboty")
        else:
            var = 0

        time.sleep(1)
