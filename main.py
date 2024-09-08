# This is a sample Python script.

import tkinter as tk
import threading

import mouse

#import keyboard
import pyautogui

from pyautogui import *

app_name = "Clicker Heroes"
#search_pattern = f"*{app_name}"
#print(search_pattern)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def move_cursor_to_center():
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2
    pyautogui.moveTo(center_x, center_y, duration=0.25)


def click():
    app_window = getWindowsWithTitle(app_name)

    # Check if the window is found
    if app_window:
        app_window[0].activate()  # Activate the application window
        move_cursor_to_center()

        for _ in range(1000):
            threading.Event().wait(0.001)
            mouse.click('left')
        print("feito")


# Create the main application window
root = tk.Tk()
root.title("Game HUD")

# Create a frame to hold the HUD elements
hud_frame = tk.Frame(root)
hud_frame.pack(padx=100, pady=100)

clickButton = tk.Button(hud_frame, text="Click", command=click)
clickButton.pack(padx=5, pady=5)

# Run the application
root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
