def connect_ssh0():
    import subprocess
    import variables
    
    st1_process = subprocess.Popen(['socat','-',f'TCP:{variables.ip[0]}:{variables.port[0]},connect-timeout=3'])
    print(st1_process)
    if st1_process.returncode==0:
        print(f'connected to {variables.ip[0]}:{variables.port[0]}')
        variables.flagSSH0 = 0
    else:
        print('failed to connect...')
        variables.flagSSH0 = 1
       

def connect_ssh1():
    import subprocess
    import variables

    st2_process = subprocess.Popen(['socat','-',f'TCP:{variables.ip[1]}:{variables.port[1]},connect-timeout=3'])
    print(st2_process)
    if st2_process.returncode==0:
        print(f'connected to {variables.ip[1]}:{variables.port[1]}')
        variables.flagSSH1 = 0
    else:
        print('failed to connect...')
        variables.flagSSH1 = 1
