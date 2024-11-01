def read0():
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
        return


def read1():
    import tkinter as tk
    import variables
    import knobs
    import activate

    if variables.flagSSH1 == 0:
        try:
            # read current from power supply
            stdin, stdout, stderr = activate.ssh0.exec_command('meas:curr?')
            read0_outpA = stdout.read().decode()+stderr.read().decode()
            knobs.ReadCurrent1.config(state=tk.NORMAL)
            knobs.ReadCurrent1.delete('0.0', tk.END)
            knobs.ReadCurrent1.insert(tk.END, f'{read0_outpA}')
            knobs.ReadCurrent1.config(state=tk.DISABLED)
            # read voltage from power supply
            stdin, stdout, stderr = activate.ssh0.exec_command('meas:volt?')
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
        return


def outputCheck0():
    import tkinter as tk
    import variables
    import knobs
    import activate

    try:
        # read output status from power supply
        stdin, stdout, stderr = activate.ssh0.exec_command('outp?')
        read0_outpA = stdout.read().decode()+stderr.read().decode()
        variables.flagOutput0 = 0
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
        return
