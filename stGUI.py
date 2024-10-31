# %%
# import modules
import tkinter as tk
import socket
import time
import subprocess
import paramiko

from time import sleep
from tkinter import ttk
from tkinter import scrolledtext

# %%
# set IP addreses and ports
global ip
global port

ip = ['192.168.1.31', '192.168.1.32']
port = ['22', '22']

# %%
def connect_ssh0():

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=f'{ip[0]}:{port[0]}', timeout=15)
        print(f'connected to {ip[0]}:{port[0]}')
        return ssh_client
    except Exception as e:
        print('failed to connect...')
        return str(e)

# %%
def connect_ssh1():

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=f'{ip[1]}:{port[1]}', timeout=15)
        print(f'connected to {ip[1]}:{port[1]}')
        return ssh_client
    except Exception as e:
        print('failed to connect...')
        return str(e)

# %%
def activate0(command):

    ssh0 = connect_ssh0()

    try:
        stdin, stdout, stderr = ssh0.exec_command(command)
        connectLabel0 = tk.Label(window, text='Connected', font=("Arial", 12),
                                 bg='green', width=12).place(x=105, y=30)
        flagActivate0 = 0
    except Exception as e:
        flagActivate0 = 1

# %%
def activate1(command):

    ssh1 = connect_ssh1()

    try:
        stdin, stdout, stderr = ssh1.exec_command(command)
        connectLabel1 = tk.Label(window, text='Connected', font=("Arial", 12),
                                 bg='green', width=12).place(x=455, y=30)
        flagActivate1 = 0
    except Exception as e:
        flagActivate1 = 1

# %%
# set GUI window
#  window
width = 700
height = 600
xpos = 400
ypos = 150

window = tk.Tk()
window.title('Steerer controller')
window.geometry(f'{width}x{height}+{xpos}+{ypos}')

# label
magnets = ['ST1', 'ST2']
addresses = []
for i in range(len(ip)):
    addresses.append(f'{ip[i]}:{port[i]}')

for i in range(len(ip)):
    stLabel0 = tk.Label(window, text=magnets[i], height=3, width=7, font=(
        "Arial", 16), relief=tk.RIDGE).place(x=10+350*i, y=5)
    ipLabel1 = tk.Label(window, text=f'IP is {addresses[i]}', font=(
        "Arial", 12), relief=tk.RIDGE).place(x=10+350*i, y=85)

connectLabel0 = tk.Label(window, text='Disconnected', font=("Arial", 12),
                         bg='red', width=12).place(x=105, y=30)

connectLabel1 = tk.Label(window, text='Disconnected', font=("Arial", 12),
                         bg='red', width=12).place(x=455, y=30)

readLabel0 = tk.Label(window, text='Read', relief=tk.RIDGE,
                      font=("Arial", 12),).place(x=145, y=140)

readLabel1 = tk.Label(window, text='Read', relief=tk.RIDGE,
                      font=("Arial", 12),).place(x=495, y=140)

for i in range(2):
    unitLabelV = tk.Label(window, text='V', font=(
        "Arial", 45)).place(x=265+350*i, y=265)
    for j in range(2):
        unitLabelA = tk.Label(window, text='A', font=(
            "Arial", 45)).place(x=265+350*i, y=170+230*j)

# text box
ReadCurrent0 = tk.Text(background='#DFDFFF')
ReadCurrent1 = tk.Text(background='#DFDFFF')
ReadVoltage0 = tk.Text(background='#DFDFFF')
ReadVoltage1 = tk.Text(background='#DFDFFF')
SetCurrent0 = tk.Text(background='#DFDFFF')
SetCurrent1 = tk.Text(background='#DFDFFF')
ReadCurrent0.place(x=10, y=165, width=250, height=75)
ReadCurrent1.place(x=360, y=165, width=250, height=75)
ReadVoltage0.place(x=10, y=255, width=250, height=75)
ReadVoltage1.place(x=360, y=255, width=250, height=75)
SetCurrent0.place(x=10, y=395, width=250, height=75)
SetCurrent1.place(x=360, y=395, width=250, height=75)

# button
activate0_Button = tk.Button(
    window,
    text="Activate ST1",
    command=lambda: activate0("addr 1")
)
activate0_Button.place(x=10, y=110)

activate1_Button = tk.Button(
    window,
    text="Activate ST2",
    command=lambda: activate1("addr 1")
)
activate1_Button.place(x=360, y=110)

# %%
# def execute_command():
#     command = command_entry.get()
#     try:
#         # command
#         result = subprocess.run(command, shell=True,
#                                 capture_output=True, text=True)
#         output_text.config(state=tk.NORMAL)  # テキストエリアを編集可能に
#         output_text.delete("1.0", tk.END)    # 既存のテキストをクリア
#         output_text.insert(
#             tk.END, result.stdout if result.returncode == 0 else result.stderr)
#         output_text.config(state=tk.DISABLED)  # 編集不可に戻す

#     except Exception as e:
#         output_text.config(state=tk.NORMAL)
#         output_text.delete("1.0", tk.END)
#         output_text.insert(tk.END, str(e))
#         output_text.config(state=tk.DISABLED)


# # コマンド入力用エントリー
# command_entry = tk.Entry(window, width=70)
# command_entry.pack(pady=10)

# # 実行ボタン
# execute_button = tk.Button(window, text="Execute", command=execute_command)
# execute_button.pack(pady=5)

# # 結果表示用のスクロールテキスト
# output_text = scrolledtext.ScrolledText(
#     window, width=70, height=15, state=tk.DISABLED)
# output_text.pack(pady=10)

# %%
# initialize flags
flagActivate0 = 1
flagActivate1 = 1

# open window
window.mainloop()

# %%



