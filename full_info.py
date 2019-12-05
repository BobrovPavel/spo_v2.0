import platform
import shutil
import time

import math
import os
import re

import psutil
import wmi
import uptime

# import wmi
from pprint import pprint

# print(platform.system())
#
# print(platform.version())
#
# print(platform.platform())
#
# print(platform.uname())
#
# print(platform.system())
#
# print(platform.processor())
#
# print(platform.machine())
#
# print(platform.architecture())
# c = wmi.WMI()
# c.Win32_ComputerSystem.methods.keys()

# total, used, free = shutil.disk_usage("d:")
#
# print("Total: %s GB" % (total / math.pow(1024, 3)))
# print("Used: %s GB" % (used / math.pow(1024, 3)))
# print("Free: %s GB" % (free / 1024 ** 3))


#
dps = psutil.disk_partitions()
c = wmi.WMI()
proc = c.Win32_Processor()[0]
bios = c.Win32_Bios()[0]
board = c.Win32_BaseBoard()[0]


# print(disk.get_devices_file_system())


class GetInfo:
    def get_all_devices(self):
        return [dp.device for dp in dps]

    def get_devices_space(self):
        tmp = {k: v for (k, v) in
               zip(self.get_all_devices(), [psutil.disk_usage(device) for device in self.get_all_devices()])}
        spaces = ["total", "used", "free", "percent"]
        result = {}
        for device in self.get_all_devices():
            result[device] = {k: v for (k, v) in
                              zip(spaces, [tmp.get(device).total, tmp.get(device).used, tmp.get(device).free,
                                           tmp.get(device).percent])}
        return result

    def get_devices_file_system(self):
        return {k: v for (k, v) in zip(self.get_all_devices(), (device.fstype for device in dps))}

    def convert_to_gb(self, number):
        return float('{:.3f}'.format(number / math.pow(1024, 3)))

    def get_bios_info(self):
        keys = [x.strip() for x in re.findall('(.*?)=', str(bios))]
        values = [x.strip() for x in re.findall('=\s+([^\n]+)[\;]', str(bios))]
        return {k: v for (k, v) in zip(keys, values)}

    def get_cpu_info(self):
        keys = [x.strip() for x in re.findall('(.*?)=', str(proc))]
        values = [x.strip() for x in re.findall('=\s+([^\n]+)[\;]', str(proc))]
        return {k: v for (k, v) in zip(keys, values)}

    def get_board_info(self):
        keys = [x.strip() for x in re.findall('(.*?)=', str(board))]
        values = [x.strip() for x in re.findall('=\s+([^\n]+)[\;]', str(board))]
        return {k: v for (k, v) in zip(keys, values)}

    def get_time(self):
        time = uptime.uptime()
        days = time // (24 * 3600)
        hours = (time - days * 3600 * 24) // 3600
        minutes = (time - days * 3600 * 24 - hours * 3600) // 60
        seconds = time - days * 3600 * 24 - hours * 3600 - minutes * 60
        return {"Uptime": f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {seconds:.3f} seconds",
                "BootTime": str(uptime.boottime())}





info = GetInfo()

print(info.get_time()["BootTime"])
print(info.get_time()["Uptime"])

