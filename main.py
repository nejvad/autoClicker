from tkinter import *

master = Tk()
master.geometry("800x800")
master.title("Basic Autoclicker")

Label(master, text="Click interval").grid(row=0)

clickIntervalHours = Entry(master, width=8, justify="right")
clickIntervalHours.grid(row=2, column=0)
Label(master, text="hours").grid(row=2, column=1, pady=10, padx=(0, 30))

clickIntervalMinutes = Entry(master, width=8, justify="right")
clickIntervalMinutes.grid(row=2, column=2)
Label(master, text="minutes").grid(row=2, column=3, pady=10, padx=(8, 30))

clickIntervalSeconds = Entry(master, width=8, justify="right")
clickIntervalSeconds.grid(row=2, column=4)
Label(master, text="seconds").grid(row=2, column=5, pady=10, padx=(8, 30))

clickIntervalMilliseconds = Entry(master, width=8, justify="right")
clickIntervalMilliseconds.grid(row=2, column=6)
Label(master, text="milliseconds").grid(row=2, column=7, pady=10, padx=(8, 30))


mainloop()
