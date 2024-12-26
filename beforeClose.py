def before_close():
    import variables
    import activate
    import knobs
    import tkinter as tk
    import subprocess

    if variables.flagSSH0 == 0:
        try:
            # read current from power supply
            read0_outpA = subprocess.run('meas:curr?')
            if read0_outpA == '0.0':
                knobs.window.destroy()
            else:
                noticeLabel1 = tk.Label(knobs.window, text='You can\'t close window now.', font=(
                    "Arial", 16), bg='red', relief=tk.RIDGE).place(x=10, y=540)
                noticeLabel2 = tk.Label(knobs.window, text='Make current 0 A first.', font=(
                    "Arial", 16), bg='red', relief=tk.RIDGE).place(x=10, y=570)
                pass
        except Exception as e:
            noticeLabel1 = tk.Label(knobs.window, text='Check connection.', font=(
                "Arial", 16), bg='red', relief=tk.RIDGE).place(x=50, y=520)
            pass
    else:
        noticeLabel1 = tk.Label(knobs.window, text='Check connection.', font=(
            "Arial", 16), bg='red', relief=tk.RIDGE).place(x=50, y=520)
        pass
