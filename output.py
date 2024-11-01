def output0():
    import tkinter as tk
    import variables
    import knobs
    import activate

    if variables.flagActivate0 == 1:
        return

    try:
        stdin, stdout, stderr = activate.ssh0.exec_command('outp on')
        outp0 = stdout.read().decode()+stderr.read().decode()
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
        outp1 = stdout.read().decode()+stderr.read().decode()
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
