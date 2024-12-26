def set0():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    if variables.flagOutput0 == 1:
        knobs.SetCurrent0.delete(0, tk.END)
        knobs.SetCurrent0.insert(tk.END, 'OUTPUT')
        return

    command = knobs.SetCurrent0.get()
    try:
        set0_outp = subprocess.run(command)
        knobs.SetCurrent0.delete(0, tk.END)
        knobs.SetCurrent0.insert(tk.END, set0_outp)
        variables.flagSet0 = 0
    except Exception as e:
        variables.flagSet0 = 1

    if variables.flagSet0 == 1:
        knobs.SetCurrent0.delete(0, tk.END)
        knobs.SetCurrent0.insert(tk.END, 'XXX')


def set1():
    import variables
    import knobs
    import tkinter as tk
    import subprocess

    if variables.flagOutput1 == 1:
        knobs.SetCurrent1.delete(0, tk.END)
        knobs.SetCurrent1.insert(tk.END, 'OUTPUT')
        return

    command = knobs.SetCurrent1.get()
    try:
        set1_outp = subprocess.run(command)
        knobs.SetCurrent1.delete(0, tk.END)
        knobs.SetCurrent1.insert(tk.END, set1_outp)
        variables.flagSet1 = 0
    except Exception as e:
        variables.flagSet1 = 1

    if variables.flagSet1 == 1:
        knobs.SetCurrent1.delete(0, tk.END)
        knobs.SetCurrent1.insert(tk.END, 'XXX')
