import knobs
import OneSec
import tkinter as tk
import beforeClose

knobs.window.protocol("WM_DELETE_WINDOW", beforeClose.before_close)
# before opening the window, run onesec()
knobs.window.after(10, OneSec.onesec)
# open window
knobs.window.mainloop()
