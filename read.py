def getValues0():
    import threading

    threading.Thread(target=_read0).start()


def _read0():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    if variables.flagSSH0 == 0:
        try:
            # read current from power supply
            read0_outpA = float(subprocess.run('meas:curr?'))
            knobs.ReadCurrent0.config(state=tk.NORMAL)
            knobs.ReadCurrent0.delete('0.0', tk.END)
            knobs.ReadCurrent0.insert(tk.END, f'{read0_outpA}')
            knobs.ReadCurrent0.config(state=tk.DISABLED)
            # read voltage from power supply
            read0_outpV = float(subprocess.run('meas:volt?'))
            knobs.ReadVoltage0.config(state=tk.NORMAL)
            knobs.ReadVoltage0.delete('0.0', tk.END)
            knobs.ReadVoltage0.insert(tk.END, f'{read0_outpV}')
            knobs.ReadVoltage0.config(state=tk.NORMAL)
            variables.flagRead0 = 0
        except Exception as e:
            # insert 'XXX' to text boxes if we can't read
            knobs.ReadCurrent0.config(state=tk.NORMAL)
            knobs.ReadCurrent0.delete('0.0', tk.END)
            knobs.ReadCurrent0.insert(tk.END, 'XXX')
            knobs.ReadCurrent0.config(state=tk.DISABLED)

            knobs.ReadVoltage0.config(state=tk.NORMAL)
            knobs.ReadVoltage0.delete('0.0', tk.END)
            knobs.ReadVoltage0.insert(tk.END, 'XXX')
            knobs.ReadVoltage0.config(state=tk.NORMAL)
            variables.flagRead0 = 1
    else:
        # insert 'XXX' to text boxes if ssh is disconnected
        knobs.ReadCurrent0.config(state=tk.NORMAL)
        knobs.ReadCurrent0.delete('0.0', tk.END)
        knobs.ReadCurrent0.insert(tk.END, 'XXX')
        knobs.ReadCurrent0.config(state=tk.DISABLED)

        knobs.ReadVoltage0.config(state=tk.NORMAL)
        knobs.ReadVoltage0.delete('0.0', tk.END)
        knobs.ReadVoltage0.insert(tk.END, 'XXX')
        knobs.ReadVoltage0.config(state=tk.NORMAL)
        variables.flagRead0 = 1


def getValues1():
    import threading

    threading.Thread(target=_read1).start()


def _read1():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    if variables.flagSSH1 == 0:
        try:
            # read current from power supply
            read0_outpA = float(subprocess.run('meas:curr?'))
            knobs.ReadCurrent1.config(state=tk.NORMAL)
            knobs.ReadCurrent1.delete('0.0', tk.END)
            knobs.ReadCurrent1.insert(tk.END, f'{read0_outpA}')
            knobs.ReadCurrent1.config(state=tk.DISABLED)
            # read voltage from power supply
            read0_outpV = float(subprocess.run('meas:volt?'))
            knobs.ReadVoltage1.config(state=tk.NORMAL)
            knobs.ReadVoltage1.delete('0.0', tk.END)
            knobs.ReadVoltage1.insert(tk.END, f'{read0_outpV}')
            knobs.ReadVoltage1.config(state=tk.NORMAL)
            variables.flagRead1 = 0
        except Exception as e:
            # insert 'XXX' to text boxes if we can't read
            knobs.ReadCurrent1.config(state=tk.NORMAL)
            knobs.ReadCurrent1.delete('0.0', tk.END)
            knobs.ReadCurrent1.insert(tk.END, 'XXX')
            knobs.ReadCurrent1.config(state=tk.DISABLED)

            knobs.ReadVoltage1.config(state=tk.NORMAL)
            knobs.ReadVoltage1.delete('0.0', tk.END)
            knobs.ReadVoltage1.insert(tk.END, 'XXX')
            knobs.ReadVoltage1.config(state=tk.NORMAL)
            variables.flagRead1 = 1
    else:
        # insert 'XXX' to text boxes if ssh is disconnected
        knobs.ReadCurrent1.config(state=tk.NORMAL)
        knobs.ReadCurrent1.delete('0.0', tk.END)
        knobs.ReadCurrent1.insert(tk.END, 'XXX')
        knobs.ReadCurrent1.config(state=tk.DISABLED)

        knobs.ReadVoltage1.config(state=tk.NORMAL)
        knobs.ReadVoltage1.delete('0.0', tk.END)
        knobs.ReadVoltage1.insert(tk.END, 'XXX')
        knobs.ReadVoltage1.config(state=tk.NORMAL)
        variables.flagRead1 = 1


def outputCheck0():
    import threading

    threading.Thread(target=_outpu0).start()


def _outpu0():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    try:
        # read output status from power supply
        outp0 = subprocess.run('outp?')
        if outp0 == 'on':  # output bottun will be green
            outputLabel0 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='green', font=("Arial", 12),).place(x=205, y=60)
            variables.flagOutput0 = 0
        else:  # output bottun will be red
            outputLabel0 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='red', font=("Arial", 12),).place(x=205, y=60)
            variables.flagOutput0 = 1
    except Exception as e:
        # output bottun will be red
        outputLabel0 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                width=2, bg='red', font=("Arial", 12),).place(x=205, y=60)
        variables.flagOutput0 = 1


def outputCheck1():
    import threading

    threading.Thread(target=_outpu1).start()


def _outpu1():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    try:
        # read output status from power supply
        outp1 = subprocess.run('outp?')
        if outp1 == 'on':  # output bottun will be green
            outputLabel1 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='green', font=("Arial", 12),).place(x=555, y=50)
            variables.flagOutput1 = 0
        else:  # output bottun will be red
            outputLabel1 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                    width=2, bg='red', font=("Arial", 12),).place(x=555, y=50)
            variables.flagOutput1 = 1
    except Exception as e:
        # output bottun will be red
        outputLabel1 = tk.Label(knobs.window, text=' ', relief=tk.RIDGE,
                                width=2, bg='red', font=("Arial", 12),).place(x=555, y=60)
        variables.flagOutput1 = 1
