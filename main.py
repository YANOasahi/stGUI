import knobs
import OneSec
import tkinter as tk

# before opening the window, run onesec()
knobs.window.after(10, OneSec.onesec)
# open window
knobs.window.mainloop()
