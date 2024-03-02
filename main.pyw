# importing modules
import tkinter
import screen_brightness_control as sbc
import rotatescreen
import pyautogui
import keyboard
import ctypes
import time
import sys
import os

# importing sub-modules
from tkinter import *
from tkinter import ttk
from screen_brightness_control import get_brightness, set_brightness

# settings
# constants
# hexadecimal color code constants
BLUE = "#007AD9"
GRAY = "#E1E1E1"

# caption constant
TITLE = "Screen Control Tool"

# screen size constants
SCREEN_WIDTH  = 352
SCREEN_HEIGHT = 180

BUTTON_WIDTH  = 40
BUTTON_HEIGHT = 40

# variables
# specific thunder version variable for version control
__version__ = "v1.0"
path = "screenshot.png"
alpha_value = float(1)

brightness_value = 100
audio_volume = 100

# initializing screen for rotation
screen = rotatescreen.get_primary_display()
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# functions
# expand root function
def expand_root():
	root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

def collapse_root():
	root.geometry(f"{SCREEN_WIDTH}x58")

# set brightness function
def set_brightness(brightness_value):
	sbc.set_brightness(brightness_value)

# set audio volume function
def set_audio_volume(audio_volume):
	pass

# screenshot function
def screenshot_function():
	root.wm_state('iconic')				# hiding maing application windows
	time.sleep(0.5)						# for half seccond
	screenshot = pyautogui.screenshot()	# taking screenshot
	screenshot.save(path)				# saving screenshot
	root.wm_state('normal')				# restoring main application windows as normal

# on keyboard press
keyboard.add_hotkey('ctrl+alt+s', screenshot_function) # taking screenshot with ctrl+alt+s hotkey

# creating main app windows
# main window configurations
root = Tk()
root.config(bg=BLUE)
root.title(f"{TITLE} | {__version__}")
root.geometry(f"{SCREEN_WIDTH}x58")
root.resizable(False, False)
root.wm_attributes("-alpha", alpha_value)

# menubar section
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
settings_menu = Menu(menubar, tearoff=0)

# add a menu item to the menu
settings_menu.add_command(label='Expand', command=expand_root)
settings_menu.add_command(label='Collapse', command=collapse_root)

# add the settings menu to the menubar
menubar.add_cascade(label="Settings", menu=settings_menu)

# frames section
# frame for buttons
buttons_frame = Frame(root, background=BLUE)
buttons_frame.place(x=2, y=58, width=120, height=120)

# frame for text
text_frame = Frame(root, background=GRAY)
text_frame.place(x=124, y=58, width=226, height=120)

# sliders section
# slider for brightness adjustment
set_brightness_slider = ttk.Scale(root, from_=0, to=100, length=348, orient=HORIZONTAL, command=set_brightness)
set_brightness_slider.set(brightness_value)
set_brightness_slider.place(x=2, y=2)

# slider for audio volume adjustment
set_audio_volume_slider = ttk.Scale(root, from_=0, to=100, length=348, orient=HORIZONTAL, command=set_audio_volume)
set_brightness_slider.set(audio_volume)
set_audio_volume_slider.place(x=2, y=30)

# buttons section
# button for screen rotation angel 0
screen_rotation_0 = ttk.Button(buttons_frame, text="0", command=lambda: screen.set_landscape())
screen_rotation_0.place(x=40, y=0, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# button for screen rotation angel 90
screen_rotation_90 = ttk.Button(buttons_frame, text="90", width=5, command=lambda: screen.set_portrait_flipped())
screen_rotation_90.place(x=80, y=40, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# button for screen rotation angel 180
screen_rotation_180 = ttk.Button(buttons_frame, text="180", width=5, command=lambda: screen.set_landscape_flipped())
screen_rotation_180.place(x=40, y=80, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# button for screen rotation angel 270
screen_rotation_270 = ttk.Button(buttons_frame, text="270", width=5, command=lambda: screen.set_portrait())
screen_rotation_270.place(x=0, y=40, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# screenshot button
screenshot_button = ttk.Button(buttons_frame, text="Shoot", width=5, command=screenshot_function)
screenshot_button.place(x=40, y=40, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# label method
label = Label(text_frame, text=f"", background=GRAY)
label.grid(row=0, column=0)

# if label have text statement
if bool(label["text"]) == True:
	pass
else:
	pass

# running main app loop - starting the program
root.mainloop()