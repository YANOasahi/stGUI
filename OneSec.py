import time
import read
import knobs
import tkinter as tk


def onesec():
    # read current from power supply in every 1 second
    read.read0()
    read.read1()
    read.outputCheck0()
    time.sleep(1)
    knobs.window.after(1000, onesec)
