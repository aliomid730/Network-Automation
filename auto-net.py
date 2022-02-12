#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.0.61',
    'username': 'itadmin',
    'password': 'L3tM3!nPaccw0rd@123',
}

iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.0.59',
    'username': 'itadmin',
    'password': 'L3tM3!nPaccw0rd@123',
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.0.56',
    'username': 'itadmin',
    'password': 'L3tM3!nPaccw0rd@123',
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.0.58',
    'username': 'itadmin',
    'password': 'L3tM3!nPaccw0rd@123',
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.0.57',
    'username': 'itadmin',
    'password': 'L3tM3!nPaccw0rd@123',
}


with open('vlans.txt') as f:
    lines = f.read().splitlines()
print(lines)


all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)
