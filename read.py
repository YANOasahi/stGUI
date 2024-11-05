def getValues0():
    import threading

    threading.Thread(target=_read0).start()


def _read0():
    import tkinter as tk
    import variables
    import knobs
    import activate

    if variables.flagSSH0 == 0:
        try:
            # read current from power supply
            stdin, stdout, stderr = activate.ssh0.exec_command('meas:curr?')
            read0_outpA = stdout.read().decode()+stderr.read().decode()
            knobs.ReadCurrent0.config(state=tk.NORMAL)
            knobs.ReadCurrent0.delete('0.0', tk.END)
            knobs.ReadCurrent0.insert(tk.END, f'{read0_outpA}')
            knobs.ReadCurrent0.config(state=tk.DISABLED)
            # read voltage from power supply
            stdin, stdout, stderr = activate.ssh0.exec_command('meas:volt?')
            read0_outpV = stdout.read().decode()+stderr.read().decode()
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
    import activate

    if variables.flagSSH1 == 0:
        try:
            # read current from power supply
            stdin, stdout, stderr = activate.ssh1.exec_command('meas:curr?')
            read0_outpA = stdout.read().decode()+stderr.read().decode()
            knobs.ReadCurrent1.config(state=tk.NORMAL)
            knobs.ReadCurrent1.delete('0.0', tk.END)
            knobs.ReadCurrent1.insert(tk.END, f'{read0_outpA}')
            knobs.ReadCurrent1.config(state=tk.DISABLED)
            # read voltage from power supply
            stdin, stdout, stderr = activate.ssh1.exec_command('meas:volt?')
            read0_outpV = stdout.read().decode()+stderr.read().decode()
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
    import tkinter as tk
    import variables
    import knobs
    import activate

    try:
        # read output status from power supply
        stdin, stdout, stderr = activate.ssh0.exec_command('outp?')
        outp0 = stdout.read().decode()+stderr.read().decode()
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
    import tkinter as tk
    import variables
    import knobs
    import activate

    try:
        # read output status from power supply
        stdin, stdout, stderr = activate.ssh1.exec_command('outp?')
        outp1 = stdout.read().decode()+stderr.read().decode()
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
