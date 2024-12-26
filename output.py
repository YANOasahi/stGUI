def output0():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    if variables.flagActivate0 == 1:
        exit()

    try:
        outp0 = subprocess.run('outp on')
        if outp0 == 'on':
            outputLabel0= tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='green', font=("Arial", 12),).place(x=205, y=60)
            variables.flagOutput0 = 0
        else:
            outputLabel0 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='red', font=("Arial", 12),).place(x=555, y=60)
            variables.flagOutput0 = 1    
    except Exception as e:
        variables.flagOutput0 = 1


def output1():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    if variables.flagActivate1 == 1:
        return

    try:
        outp1 = subprocess.run('outp on')
        if outp1 == 'on':
            outputLabel1 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='green', font=("Arial", 12),).place(x=205, y=60)
            variables.flagOutput1 = 0
        else:
            outputLabel1 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='red', font=("Arial", 12),).place(x=555, y=60)
            variables.flagOutput1 = 1
    except Exception as e:
        variables.flagOutput1 = 1
