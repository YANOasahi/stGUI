def output0():
    import tkinter as tk
    import variables
    import knobs
    import activate

    if variables.flagActivate0 == 1:
        return

    try:
        stdin, stdout, stderr = activate.ssh0.exec_command('outp on')
        outputLabel0 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                width=2, bg='green', font=("Arial", 12),).place(x=205, y=50)
        variables.flagOutput0 = 0
    except Exception as e:
        variables.flagOutput0 = 1


def output1():
    import tkinter as tk
    import variables
    import knobs
    import activate

    if variables.flagActivate1 == 1:
        return

    try:
        stdin, stdout, stderr = activate.ssh1.exec_command('outp on')
        outputLabel0 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                width=2, bg='green', font=("Arial", 12),).place(x=205, y=50)
        variables.flagOutput1 = 0
    except Exception as e:
        variables.flagOutput1 = 1
