def activate0():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    if variables.flagSSH0 == 1:
        exit()

    try:
        answer = subprocess.run(['addr','1'])
        print(answer)
        variables.flagActivate0 = 0
        exit()
    except Exception as e:
        variables.flagActivate0 = 1
        exit()


def activate1():
    import tkinter as tk
    import variables
    import knobs
    import subprocess

    if variables.flagSSH1 == 1:
        exit()

    try:
        answer = subprocess.run(['addr','1'])
        print(answer)
        variables.flagActivate1 = 0
        exit()
    except Exception as e:
        variables.flagActivate1 = 1
        exit()
