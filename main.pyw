# importing modules
import tkinter
import screen_brightness_control as sbc
import rotatescreen
import pyautogui
import keyboard
import datetime
import time
import os

# importing sub-modules
from tkinter import *
from tkinter import ttk
from screen_brightness_control import get_brightness, set_brightness
from datetime import datetime

# settings
# constants
# hexadecimal color code constants
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"

BLACK = "#000000"
WHITE = "#FFFFFF"

BLUE = "#007AD9"
GRAY = "#E1E1E1"

ALPHA = GREEN

# caption constant
TITLE = "Screen Control Tool"

# screen size constants
SCREEN_WIDTH  = 352
SCREEN_HEIGHT = 208

BUTTON_WIDTH  = 40
BUTTON_HEIGHT = 40

# variables
__version__ = "v1.0"
alpha_value = float(1)
screenshot_path = "archive\\screenshots\\"

brightness_value = 100
contrast_value = 100
audio_volume = 100

# initializing screen for rotation
screen = rotatescreen.get_primary_display()

# creating directory for storing screenshots
os.system(f"mkdir {screenshot_path}")

# functions
# set brightness function
def set_brightness(brightness_value):
	sbc.set_brightness(brightness_value)

# set contrast function
def set_contrast(contrast_value):
	pass

# set audio volume function
def set_audio_volume(audio_volume):
	pass

# screenshot function
def screenshot_function():
	timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
	screenshot_filename = f"{timestamp}.png"

	screenshot = pyautogui.screenshot(f"{screenshot_path}screenshot_{screenshot_filename}")

# mouse position and rgb color get function
def mouse_position_and_rgb(mouse_pos=None, rgb=None):
		mouse_pos = pyautogui.position()[0], pyautogui.position()[1]
		rgb = pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1])

		return(f" {mouse_pos} {rgb}")

# updating mouse position and rgb
def update_mouse_mouse_position_and_rgb():
	label.config(text=mouse_position_and_rgb())
	label.after(200, update_mouse_mouse_position_and_rgb)

# on keyboard press hotkeys
keyboard.add_hotkey("ctrl+m",  lambda: root.wm_state("iconic")) # minimize program with ctrl+m hotkey
keyboard.add_hotkey("ctrl+n",  lambda: root.wm_state("normal")) # normalize program with ctrl+n hotkey

keyboard.add_hotkey("ctrl+e",  lambda: root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")) # quit program with ctrl+q hotkey
keyboard.add_hotkey("ctrl+c",  lambda: root.geometry(f"{SCREEN_WIDTH}x86")) # quit program with ctrl+q hotkey
keyboard.add_hotkey("ctrl+q",  lambda: root.destroy()) # quit program with ctrl+q hotkey

keyboard.add_hotkey("ctrl+alt+s", screenshot_function) # taking screenshot with ctrl+alt+s hotkey
keyboard.add_hotkey("ctrl+alt+up", lambda: screen.set_landscape()) # landscape with ctrl+alt+up hotkey
keyboard.add_hotkey("ctrl+alt+down", lambda: screen.set_landscape_flipped()) # landscape flipped with ctrl+alt+down hotkey
keyboard.add_hotkey("ctrl+alt+left", lambda: screen.set_portrait()) # portrait with ctrl+alt+left hotkey
keyboard.add_hotkey("ctrl+alt+right", lambda: screen.set_portrait_flipped()) # portrait flipped with ctrl+alt+right hotkey

# creating main app windows
# main window configurations
root = Tk()
root.config(bg=BLUE)
root.title(f"{TITLE} | {__version__}")
root.geometry(f"{SCREEN_WIDTH}x86")
root.resizable(False, False)
root.wm_attributes("-alpha", alpha_value)

# menubar section
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar, tearoff=0)
help_menu = Menu(menubar, tearoff=0)

# add a menu item to the file menu
file_menu.add_command(label="Expand                       Ctrl+E", command=lambda: root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"))
file_menu.add_command(label="Collapse                     Ctrl+C", command=lambda: root.geometry(f"{SCREEN_WIDTH}x86"))
file_menu.add_separator()
file_menu.add_command(label="Quit                            Ctrl+Q", command=lambda: root.destroy())

# add a menu item to the help menu
help_menu.add_command(label="Hotkeys", command=lambda: print("I already told ya!"))
help_menu.add_command(label="About", command=lambda: print("I already told ya!"))

# add the file menu to the menubar
menubar.add_cascade(label="File", menu=file_menu)

# add the help menu to the menubar
menubar.add_cascade(label="Help", menu=help_menu)

# frames section
# frame for buttons
buttons_frame = Frame(root, background=BLUE)
buttons_frame.place(x=2, y=86, width=120, height=120)

# frame for text
text_frame = Frame(root, background=GRAY)
text_frame.place(x=124, y=86, width=226, height=120)

# sliders section
# slider for brightness adjustment
set_brightness_slider = ttk.Scale(root, from_=0, to=100, length=348, orient=HORIZONTAL, command=set_brightness)
set_brightness_slider.set(brightness_value)
set_brightness_slider.place(x=2, y=2)

# slider for contrast adjustment
set_contrast_slider = ttk.Scale(root, from_=0, to=100, length=348, orient=HORIZONTAL, command=set_contrast)
set_contrast_slider.set(contrast_value)
set_contrast_slider.place(x=2, y=30)

# slider for audio volume adjustment
set_audio_volume_slider = ttk.Scale(root, from_=0, to=100, length=348, orient=HORIZONTAL, command=set_audio_volume)
set_audio_volume_slider.set(audio_volume)
set_audio_volume_slider.place(x=2, y=58)

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

# label section
# label for displaying mouse position and rgb colour
label = Label(text_frame, text=None, background=GRAY)
label.grid(row=0, column=0)

# calling update mouse function
update_mouse_mouse_position_and_rgb()

# running main app loop - starting the program
root.mainloop()