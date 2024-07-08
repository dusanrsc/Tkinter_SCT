# importing modules
import tkinter
import screen_brightness_control as sbc
import rotatescreen
import webbrowser
import pyautogui
import keyboard
import os

# importing sub-modules
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
from screen_brightness_control import get_brightness, set_brightness
from datetime import datetime

# settings section
# constants section
# hexadecimal color code constants
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"

BLACK = "#000000"
WHITE = "#FFFFFF"

BLUE = "#007AD9"
GRAY = "#E1E1E1"
ORANGE = "#FFA500"

ALPHA = GREEN

# caption constant
TITLE = "Screen Control Tool"

# screen size constants
WINDOW_WIDTH  = 352
WINDOW_HEIGHT = 152
WINDOW_HEIGHT_EXPANDED = 30

# buton size constants
BUTTON_WIDTH  = 40
BUTTON_HEIGHT = 40

# variables section
# meta data - specific variables
__version__ = "v1.1.0"
__updated__ = "07.08.2024"
__by__ = "Dusan Rosic"

# standard variables
alpha_value = float(1)
screenshot_path = "archive\\screenshots\\"

brightness_value = 100
contrast_value = 100
audio_volume = 100
topmost = False

# initializing screen for rotation
screen = rotatescreen.get_primary_display()

# creating directory for storing screenshots
os.system(f"mkdir {screenshot_path}")

# functions section
# set brightness function
def set_brightness(brightness_value):
	sbc.set_brightness(brightness_value)

# screenshot function
def screenshot_function():
	timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
	screenshot_filename = f"{timestamp}.png"

	screenshot = pyautogui.screenshot(f"{screenshot_path}screenshot_{screenshot_filename}")

# mouse position and rgb color get function
def mouse_position_and_rgb(mouse_pos=None, rgb=None):
		mouse_pos = pyautogui.position()[0], pyautogui.position()[1]
		rgb = pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1])

		return(f"{mouse_pos} {rgb}")

# updating mouse position and rgb
def update_mouse_position_and_rgb():
	label.config(text=mouse_position_and_rgb())
	label.after(200, update_mouse_position_and_rgb)

# choice color function
def choose_color():
	color_code = colorchooser.askcolor(title="Choose color")[1]
	root.config(bg=color_code)

# topmost or z-index setter function
def set_topmost():
	global topmost
	if topmost:
		topmost = False
		root.wm_attributes("-topmost", topmost)
	else:
		topmost = True
		root.wm_attributes("-topmost", topmost)

# keyboard events
# on keyboard press hotkeys
keyboard.add_hotkey("ctrl+m", lambda: root.wm_state("iconic")) 											# minimize program with ctrl+m hotkey
keyboard.add_hotkey("ctrl+n", lambda: root.wm_state("normal")) 											# normalize program with ctrl+n hotkey

keyboard.add_hotkey("ctrl+e", lambda: root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")) 				# quit program with ctrl+q hotkey
keyboard.add_hotkey("ctrl+c", lambda: root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT_EXPANDED}")) 		# quit program with ctrl+q hotkey
keyboard.add_hotkey("ctrl+z", lambda: set_topmost()) 													# toggle on/off topmost function with hotkey
keyboard.add_hotkey("ctrl+alt+q",  lambda: root.destroy()) 												# quit program with ctrl+alt+q hotkey

keyboard.add_hotkey("ctrl+alt+s", screenshot_function) 													# taking screenshot with ctrl+alt+s hotkey
keyboard.add_hotkey("ctrl+alt+up", lambda: screen.set_landscape()) 										# landscape with ctrl+alt+up hotkey
keyboard.add_hotkey("ctrl+alt+down", lambda: screen.set_landscape_flipped()) 							# landscape flipped with ctrl+alt+down hotkey
keyboard.add_hotkey("ctrl+alt+left", lambda: screen.set_portrait()) 									# portrait with ctrl+alt+left hotkey
keyboard.add_hotkey("ctrl+alt+right", lambda: screen.set_portrait_flipped()) 							# portrait flipped with ctrl+alt+right hotkey

# creating main app windows
# main window configurations
root = Tk()
root.config(bg=BLUE)
root.title(f"{TITLE} | {__version__}")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.resizable(False, False)
root.wm_attributes("-alpha", alpha_value)

# menubar section
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
settings_menu = Menu(menubar, tearoff=0)
help_menu = Menu(menubar, tearoff=0)

# creating sub-menu
# sub-menu for help section
# sub-menu for all shortcuts
sub_menu = Menu(help_menu, tearoff=0)
sub_menu.add_command(label="Expand                      Ctrl+E", command=lambda: root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"))
sub_menu.add_command(label="Collapse                    Ctrl+C", command=lambda: root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT_EXPANDED}"))
sub_menu.add_separator()
sub_menu.add_command(label="Topmost                   Ctrl+Z", command=lambda: set_topmost())
sub_menu.add_separator()
sub_menu.add_command(label="Minimize                   Ctrl+M", command=lambda: root.wm_state("iconic"))
sub_menu.add_command(label="Normalize                 Ctrl+N", command=lambda: root.wm_state("normal"))
sub_menu.add_separator()
sub_menu.add_command(label="Screenshot                Ctrl+Alt+S", command=screenshot_function)
sub_menu.add_separator()
sub_menu.add_command(label="Screen °0                   Ctrl+Alt+↑", command=lambda: screen.set_landscape())
sub_menu.add_command(label="Screen °90                 Ctrl+Alt+→", command=lambda: screen.set_portrait_flipped())
sub_menu.add_command(label="Screen °180               Ctrl+Alt+↓", command=lambda: screen.set_landscape_flipped())
sub_menu.add_command(label="Screen °270               Ctrl+Alt+←", command=lambda: screen.set_portrait())
sub_menu.add_separator()
sub_menu.add_command(label="Quit                            Ctrl+Alt+Q", command=lambda: root.destroy())

# sub-menu for about section
sub_menu2 = Menu(help_menu, tearoff=0)
sub_menu2.add_command(label=f"By: {__by__}")
sub_menu2.add_separator()
sub_menu2.add_command(label=f"Application: {TITLE}")
sub_menu2.add_command(label=f"Version: {__version__}")
sub_menu2.add_command(label=f"Updated: {__updated__}")
sub_menu2.add_separator()
sub_menu2.add_command(label=f"My Instagram", command=lambda: webbrowser.open("https://www.instagram.com/dusanrsc/"))
sub_menu2.add_command(label=f"My GitHub", command=lambda: webbrowser.open("https://www.github.com/dusanrsc/"))

# sub-menu for setting section
# sub-menu for colors
sub_menu3 = Menu(settings_menu, tearoff=0)
sub_menu3.add_command(label=" Choice  ", command=choose_color)
sub_menu3.add_separator()
sub_menu3.add_command(label="", foreground=WHITE, background=RED, command=lambda: root.config(bg=RED))
sub_menu3.add_separator()
sub_menu3.add_command(label="", foreground=WHITE, background=GREEN, command=lambda: root.config(bg=GREEN))
sub_menu3.add_separator()
sub_menu3.add_command(label="(default) ", foreground=WHITE, background=BLUE, command=lambda: root.config(bg=BLUE))
sub_menu3.add_separator()
sub_menu3.add_command(label="", foreground=BLACK, background=ORANGE, command=lambda: root.config(bg=ORANGE))
sub_menu3.add_separator()
sub_menu3.add_command(label="", foreground=WHITE, background=BLACK, command=lambda: root.config(bg=BLACK))
sub_menu3.add_separator()
sub_menu3.add_command(label="", foreground=BLACK, background=WHITE, command=lambda: root.config(bg=WHITE))

# add a menu item to the settings menu
settings_menu.add_command(label="Expand                            Ctrl+E", command=lambda: root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"))
settings_menu.add_command(label="Collapse                          Ctrl+C", command=lambda: root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT_EXPANDED}"))
settings_menu.add_separator()
settings_menu.add_command(label="Topmost                         Ctrl+Z", command=lambda: set_topmost())
settings_menu.add_separator()
settings_menu.add_cascade(label="Color", menu=sub_menu3)
settings_menu.add_separator()
settings_menu.add_command(label="Quit                                 Ctrl+Alt+Q", command=lambda: root.destroy())

# add a menu item to the help menu
help_menu.add_cascade(label="All Shortcuts", menu=sub_menu)
help_menu.add_cascade(label="About", menu=sub_menu2)

# add the file menu to the menubar
menubar.add_cascade(label="Settings", menu=settings_menu)

# add the help menu to the menubar
menubar.add_cascade(label="Help", menu=help_menu)

# frames section
# frame for text
text_frame = Frame(root, background=GRAY)
text_frame.place(x=124, y=30, width=226, height=120)

# sliders section
# slider for brightness adjustment
set_brightness_slider = ttk.Scale(root, from_=0, to=100, length=348, orient=HORIZONTAL, command=set_brightness)
set_brightness_slider.set(brightness_value)
set_brightness_slider.place(x=2, y=2)

# buttons section
# button for screen rotation angel 0
screen_rotation_0 = ttk.Button(root, text="0", command=lambda: screen.set_landscape())
screen_rotation_0.place(x=42, y=30, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# button for screen rotation angel 90
screen_rotation_90 = ttk.Button(root, text="90", width=5, command=lambda: screen.set_portrait_flipped())
screen_rotation_90.place(x=82, y=70, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# button for screen rotation angel 180
screen_rotation_180 = ttk.Button(root, text="180", width=5, command=lambda: screen.set_landscape_flipped())
screen_rotation_180.place(x=42, y=110, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# button for screen rotation angel 270
screen_rotation_270 = ttk.Button(root, text="270", width=5, command=lambda: screen.set_portrait())
screen_rotation_270.place(x=2, y=70, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# screenshot button
screenshot_button = ttk.Button(root, text="Shoot", width=5, command=screenshot_function)
screenshot_button.place(x=42, y=70, width=BUTTON_WIDTH, height=BUTTON_HEIGHT)

# label section
# label for displaying mouse position and rgb colour
label = Label(text_frame, text=None, background=GRAY)
label.grid(row=0, column=0)

# update function section
# calling update mouse function
update_mouse_position_and_rgb()

# running main app loop - starting the program
root.mainloop()
