import re
from pprint import pprint

import wmi
import math
import uptime
import psutil

dps = psutil.disk_partitions()
c = wmi.WMI()
cpu = c.Win32_Processor()[0]
gpu = c.Win32_VideoController()[0]
bios = c.Win32_Bios()[0]
board = c.Win32_BaseBoard()[0]
users = c.Win32_UserAccount()

wmi_monitor = c.Win32_DesktopMonitor()[0]
wmi_keyboard = c.Win32_Keyboard()[0]
wmi_mouse = c.Win32_PnpEntity()[0]
wmi_networkAdapter = c.Win32_NetworkAdapter()[0]


def get_all_devices():
    return [dp.device for dp in dps]


def get_devices_space():
    result = {}
    try:
        tmp = {k: v for (k, v) in
               zip(get_all_devices(), [psutil.disk_usage(device) for device in get_all_devices()])}
        spaces = ["total", "used", "free", "percent"]
        for device in get_all_devices():
            result[device] = {k: v for (k, v) in
                              zip(spaces, [tmp.get(device).total, tmp.get(device).used, tmp.get(device).free,
                                           tmp.get(device).percent])}
    except:
        print("Failed to get disk info. Check permissions.")
    return result


def get_devices_file_system():
    return {k: v for (k, v) in zip(get_all_devices(), (device.fstype for device in dps))}


def convert_to_gb(number):
    return float('{:.3f}'.format(number / math.pow(1024, 3)))


def get_bios_info():
    keys = [x.strip() for x in re.findall('(.*?)=', str(bios))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(bios))]
    return {k: v for (k, v) in zip(keys, values)}


def get_cpu_info():
    keys = [x.strip() for x in re.findall('(.*?)=', str(cpu))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(cpu))]
    return {k: v for (k, v) in zip(keys, values)}


def get_gpu_info():
    keys = [x.strip() for x in re.findall('(.*?)=', str(gpu))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(gpu))]
    return {k: v for (k, v) in zip(keys, values)}


def get_board_info():
    keys = [x.strip() for x in re.findall('(.*?)=', str(board))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(board))]
    return {k: v for (k, v) in zip(keys, values)}


def get_time():
    time = uptime.uptime()
    days = time // (24 * 3600)
    hours = (time - days * 3600 * 24) // 3600
    minutes = (time - days * 3600 * 24 - hours * 3600) // 60
    seconds = time - days * 3600 * 24 - hours * 3600 - minutes * 60
    return {"Uptime": f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {seconds:.3f} seconds",
            "BootTime": str(uptime.boottime())}


def get_users():
    user_list = {}
    for user in users:
        keys = [x.strip() for x in re.findall('(.*?)=', str(user))]
        values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(user))]
        name = user.name
        user_list[name] = {k: v for (k, v) in zip(keys, values)}
    return user_list


def get_devices_info():
    devices = {}
    keys = [x.strip() for x in re.findall('(.*?)=', str(wmi_monitor))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(wmi_monitor))]
    monitor = {k: v for (k, v) in zip(keys, values)}
    keys = [x.strip() for x in re.findall('(.*?)=', str(wmi_keyboard))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(wmi_keyboard))]
    keyboard = {k: v for (k, v) in zip(keys, values)}
    keys = [x.strip() for x in re.findall('(.*?)=', str(wmi_mouse))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(wmi_mouse))]
    mouse = {k: v for (k, v) in zip(keys, values)}
    keys = [x.strip() for x in re.findall('(.*?)=', str(wmi_networkAdapter))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(wmi_networkAdapter))]
    network_adapter = {k: v for (k, v) in zip(keys, values)}
    devices["Monitor"] = monitor
    devices["Keyboard"] = keyboard
    devices["Mouse"] = mouse
    devices["Network Adapter"] = network_adapter
    return devices


def create_report():
    result = []
    result.append("\n---------------DISK INFO---------------\n")
    for k, v in get_devices_space().items():
        result.append(f"{k}: {v} \n")
    for k, v in get_devices_file_system().items():
        result.append(f"{k}: {v} \n")
    result.append("\n---------------BIOS INFO---------------\n")
    for k, v in get_bios_info().items():
        result.append(f"{k}: {v} \n")
    result.append("\n---------------CPU INF---------------\n")
    for k, v in get_cpu_info().items():
        result.append(f"{k}: {v} \n")
    result.append("\n---------------MOTHERBOARD INFO---------------\n")
    for k, v in get_board_info().items():
        result.append(f"{k}: {v} \n")
    result.append("\n---------------TIME INFO---------------\n")
    for k, v in get_time().items():
        result.append(f"{k}: {v} \n")
    return result


# print(c.Win32_DesktopMonitor()[0])
# print(c.Win32_Keyboard()[0])
# print(c.Win32_PnpEntity()[0])
# print(c.Win32_NetworkAdapter()[0])

# print(get_devices_info())

print(bios)
