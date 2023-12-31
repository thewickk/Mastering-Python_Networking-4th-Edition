#!/usr/bin/env python

import getpass
from pexpect import pxssh

devices = { 'iosv-1': {'prompt': 'lax-edg-r1#', 'ip': '192.168.2.51'},
            'iosv-2': {'prompt': 'lax-edg-r2#', 'ip': '192.168.2.52'} }

commands = ['term length 0', 'show version', 'show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

# Starts the loop for devices
for device in devices.keys():
    ouputFilename = device + '_output.txt'
    device_prompt = devices[device]['prompt']
    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
    # Starts the loop for commands and write to output
    with open(ouputFilename, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)

    child.logout()