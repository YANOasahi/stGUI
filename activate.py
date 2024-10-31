def activate0(command):
    import tkinter as tk
    import connect_ssh
    import variables
    import knobs

    if variables.flagSSH0 == 1:
        return

    ssh0 = connect_ssh.connect_ssh0()

    try:
        stdin, stdout, stderr = ssh0.exec_command(command)
        connectLabel0 = tk.Label(knobs.window, text='Connected', font=("Arial", 12),
                                 bg='green', width=12).place(x=105, y=10)
        variables.flagActivate0 = 0
    except Exception as e:
        variables.flagActivate0 = 1


def activate1(command):
    import tkinter as tk
    import connect_ssh
    import variables
    import knobs

    if variables.flagSSH1 == 1:
        return

    ssh1 = connect_ssh.connect_ssh1()

    try:
        stdin, stdout, stderr = ssh1.exec_command(command)
        connectLabel1 = tk.Label(knobs.window, text='Connected', font=("Arial", 12),
                                 bg='green', width=12).place(x=455, y=10)
        variables.flagActivate1 = 0
    except Exception as e:
        variables.flagActivate1 = 1
