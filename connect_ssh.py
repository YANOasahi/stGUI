def connect_ssh0():
    import paramiko# type: ignore
    import variables

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(
            hostname=f'{variables.ip[0]}', port=f'{variables.port[0]}', timeout=2)
        print(f'connected to {variables.ip[0]}:{variables.port[0]}')
        variables.flagSSH0 = 0
        return ssh_client
    except Exception as e:
        print('failed to connect...')
        variables.flagSSH0 = 1
        return str(e)


def connect_ssh1():
    import paramiko # type: ignore
    import variables

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(
            hostname=f'{variables.ip[1]}', port=f'{variables.port[1]}', timeout=2)
        print(f'connected to {variables.ip[1]}:{variables.port[1]}')
        variables.flagSSH1 = 0
        return ssh_client
    except Exception as e:
        print('failed to connect...')
        variables.flagSSH1 = 1
        return str(e)
