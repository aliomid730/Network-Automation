#!/usr/bin/env python

from netmiko import ConnectHandler
from hosts import *

with open('template_config') as f:
    lines = f.read().splitlines()
print(lines)

all_devices = [s1, s2, s3, s4, s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
