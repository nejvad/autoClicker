import threading
from tkinter import *
from tkinter import ttk

import keyboard
import pydirectinput


def auto_click():
    keyboard_inp = key_input.get()
    if keyboard.read_key() == keyboard_inp:

        while True:
            click_speed = click_input.get()
            pydirectinput.PAUSE = float(click_speed)
            pydirectinput.click()


master = Tk()
master.geometry("300x400")
master.title("Basic Autoclicker")

click_input = Entry(master, width=30)
click_input.pack()

key_input = Entry(master, width=30)
key_input.pack()

start_button = ttk.Button(master, text="Start", command=threading.Thread(target=auto_click).start)
start_button.pack()

stop_button = ttk.Button(master, text="Close", command=master.destroy)
stop_button.pack()


if __name__ == "__main__":
    mainloop()
