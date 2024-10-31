def make_window():
    import tkinter as tk
    # set IP addreses and ports
    global ip
    global port
    # define flags as global variables
    global flagSSH0
    global flagSSH1
    global flagActivate0
    global flagActivate1
    global flagOutput0
    global flagOutput1

    # set IP addresses and ports
    ip = ['192.168.1.31', '192.168.1.32']
    port = ['22', '22']

    # set GUI window
    #  window
    set_width = int(700*0.97)
    set_height = int(600*0.97)
    set_xpos = 400
    set_ypos = 150
    
    window = tk.Tk()
    window.title('Steerer controller')
    window.geometry(f'{set_width}x{set_height}+{set_xpos}+{set_ypos}')
    window.wm_minsize(width=set_width, height=set_height)
    
    # label
    magnets = ['ST1', 'ST2']
    addresses = []
    # for IP addtess
    for i in range(len(ip)):
        addresses.append(f'{ip[i]}:{port[i]}')
    
    for i in range(len(ip)):
        stLabel0 = tk.Label(window, text=magnets[i], height=3, width=7, font=(
            "Arial", 16), relief=tk.RIDGE).place(x=10+350*i, y=10)
        ipLabel1 = tk.Label(window, text=f'IP is {addresses[i]}', height=2, font=(
            "Arial", 12), relief=tk.RIDGE).place(x=10+350*i, y=90)
    # for connection
    connectLabel0 = tk.Label(window, text='Disconnected', font=("Arial", 12),
                             bg='red', width=12).place(x=105, y=10)
    
    connectLabel1 = tk.Label(window, text='Disconnected', font=("Arial", 12),
                             bg='red', width=12).place(x=455, y=10)
    # for 'Read'
    readLabel0 = tk.Label(window, text='Read', relief=tk.RIDGE,
                          width=6, height=2, font=("Arial", 12),).place(x=145, y=160)
    
    readLabel1 = tk.Label(window, text='Read', relief=tk.RIDGE,
                          width=6, height=2, font=("Arial", 12),).place(x=495, y=160)
    # for 'Output'
    outputLabel0 = tk.Label(window, text='Output', relief=tk.RIDGE,
                            width=8, font=("Arial", 12),).place(x=105, y=50)
    
    outputLabel1 = tk.Label(window, text='Output', relief=tk.RIDGE,
                            width=8, font=("Arial", 12),).place(x=455, y=50)
    # for LED
    outputLabel0 = tk.Label(window, text=' ', relief=tk.RIDGE,
                            width=2, bg='red', font=("Arial", 12),).place(x=205, y=50)
    
    outputLabel1 = tk.Label(window, text=' ', relief=tk.RIDGE,
                            width=2, bg='red', font=("Arial", 12),).place(x=555, y=50)
    # for unit
    for i in range(2):
        unitLabelV = tk.Label(window, text='V', font=(
            "Arial", 45)).place(x=265+350*i, y=300)
        for j in range(2):
            unitLabelA = tk.Label(window, text='A', font=(
                "Arial", 45)).place(x=265+350*i, y=210+225*j)
    
    # text box for displaying current and voltage, NOT writable
    ReadCurrent0 = tk.Text(font=("Arial", 45), background='#DFDFFF')
    ReadCurrent1 = tk.Text(font=("Arial", 45), background='#DFDFFF')
    ReadCurrent0.config(state=tk.DISABLED)
    ReadCurrent1.config(state=tk.DISABLED)
    ReadCurrent0.place(x=10, y=205, width=250, height=75)
    ReadCurrent1.place(x=360, y=205, width=250, height=75)
    
    ReadVoltage0 = tk.Text(font=("Arial", 45), background='#DFDFFF')
    ReadVoltage1 = tk.Text(font=("Arial", 45), background='#DFDFFF')
    ReadVoltage0.config(state=tk.DISABLED)
    ReadVoltage1.config(state=tk.DISABLED)
    ReadVoltage0.place(x=10, y=290, width=250, height=75)
    ReadVoltage1.place(x=360, y=290, width=250, height=75)
    
    # entry box for setting current, writeble
    SetCurrent0 = tk.Entry(window, font=("Arial", 45), background='#DFDFFF')
    SetCurrent1 = tk.Entry(window, font=("Arial", 45), background='#DFDFFF')
    SetCurrent0.place(x=10, y=430, width=250, height=75)
    SetCurrent1.place(x=360, y=430, width=250, height=75)
    
    # button
    # for connectioon and activate
    activate0_Button = tk.Button(
        window,
        text="Activate ST1",
        command=lambda: activate0("addr 1")
    )
    activate0_Button.place(x=10, y=130)
    
    activate1_Button = tk.Button(
        window,
        text="Activate ST2",
        command=lambda: activate1("addr 1")
    )
    activate1_Button.place(x=360, y=130)
    # for setting current
    setButton0 = tk.Button(window, text='Set', command=lambda: set0(ssh0))
    setButton0.place(x=140, y=395)
    setButton1 = tk.Button(window, text='Set', command=lambda: set1(ssh1))
    setButton1.place(x=500, y=395)
    
    window.mainloop()