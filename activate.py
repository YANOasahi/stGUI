def activate0():
    import tkinter as tk
    import variables
    import subprocess
    import connect_ssh

    connect_ssh.connect_ssh0()

    if variables.flagSSH0 == 0:
        st1_process.stdin.write(['addr','1'])
        answer = st1_process.stdout.read()
        if answer == 'OK':
            variables.flagActivate0 = 0
        else:
            variables.flagActivate0 = 1


def activate1():
    import tkinter as tk
    import variables
    import subprocess
    import connect_ssh

    connect_ssh.connect_ssh1()

    if variables.flagSSH1 == 0:
        st2_process.stdin.write(['addr','1'])
        answer = st2_process.stdout.read()
        if answer == 'OK':
            print(answer)
            variables.flagActivate1 = 0
        else:
            variables.flagActivate1 = 1