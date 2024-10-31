def set0():
    import tkinter as tk
    import variables
    import knobs
    import activate

    if variables.flagOutput0 == 1:
        knobs.SetCurrent0.delete(0, tk.END)
        knobs.SetCurrent0.insert(tk.END, 'OUTPUT')
        return

    command = knobs.SetCurrent0.get()
    try:
        stdin, stdout, stderr = activate.ssh0.exec_command(command)
        set0_outp = stdout.read().decode()+stderr.read().decode()
        knobs.SetCurrent0.delete(0, tk.END)
        knobs.SetCurrent0.insert(tk.END, f'{set0_outp}')
        variables.flagSet0 = 0
    except Exception as e:
        variables.flagSet0 = 1

    if variables.flagSet0 == 1:
        knobs.SetCurrent0.delete(0, tk.END)
        knobs.SetCurrent0.insert(tk.END, 'XXX')


def set1():
    import variables
    import knobs
    import activate
    import tkinter as tk

    if variables.flagOutput1 == 1:
        knobs.SetCurrent1.delete(0, tk.END)
        knobs.SetCurrent1.insert(tk.END, 'OUTPUT')
        return

    command = knobs.SetCurrent1.get()
    try:
        stdin, stdout, stderr = activate.ssh1.exec_command(command)
        set1_outp = stdout.read().decode()+stderr.read().decode()
        knobs.SetCurrent1.delete(0, tk.END)
        knobs.SetCurrent1.insert(tk.END, f'{set1_outp}')
        variables.flagSet1 = 0
    except Exception as e:
        variables.flagSet1 = 1

    if variables.flagSet1 == 1:
        knobs.SetCurrent1.delete(0, tk.END)
        knobs.SetCurrent1.insert(tk.END, 'XXX')
