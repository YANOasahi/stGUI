import time
import read
import knobs
import tkinter as tk


def onesec():
    # read current from power supply in every 1 second
    read.getValues0()
    read.getValues1()
    read.outputCheck0()
    read.outputCheck1()
    time.sleep(1)
    knobs.window.after(1000, onesec)
