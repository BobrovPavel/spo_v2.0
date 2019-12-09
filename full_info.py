import re
import wmi
import math
import uptime
import psutil

dps = psutil.disk_partitions()
c = wmi.WMI()
proc = c.Win32_Processor()[0]
bios = c.Win32_Bios()[0]
board = c.Win32_BaseBoard()[0]


def get_all_devices():
    return [dp.device for dp in dps]


def get_devices_space():
    tmp = {k: v for (k, v) in
           zip(get_all_devices(), [psutil.disk_usage(device) for device in get_all_devices()])}
    spaces = ["total", "used", "free", "percent"]
    result = {}
    for device in get_all_devices():
        result[device] = {k: v for (k, v) in
                          zip(spaces, [tmp.get(device).total, tmp.get(device).used, tmp.get(device).free,
                                       tmp.get(device).percent])}
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
    keys = [x.strip() for x in re.findall('(.*?)=', str(proc))]
    values = [x.strip('"') for x in re.findall('=\s+([^\n]+)[\;]', str(proc))]
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
