def connect_ssh0():
    import subprocess
    import variables

    try:
        subprocess.run(['socat','-',f'TCP:{variables.ip[0]}:{variables.port[0]}'])
        print(f'connected to {variables.ip[0]}:{variables.port[0]}')
        variables.flagSSH0 = 0
    except Exception as e:
        print('failed to connect...')
        variables.flagSSH0 = 1
        return str(e)


def connect_ssh1():
    import subprocess
    import variables

    try:
        subprocess.run(['socat','-',f'TCP:{variables.ip[1]}:{variables.port[1]}'])
        print(f'connected to {variables.ip[1]}:{variables.port[1]}')
        variables.flagSSH1 = 0
    except Exception as e:
        print('failed to connect...')
        variables.flagSSH1 = 1
        return str(e)
