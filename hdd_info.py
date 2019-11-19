import platform
import shutil
import math

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


import psutil

dps = psutil.disk_partitions()


class DiskInfo:

    def get_all_devices(self):
        return [dp.device for dp in dps]

    def get_devices_space(self):
        tmp = {k: v for (k, v) in
               zip(self.get_all_devices(), [psutil.disk_usage(device) for device in self.get_all_devices()])}
        spaces = ["total", "used", "free", "percent"]
        result = {}
        for device in self.get_all_devices():
            result[device] = {k: v for (k, v) in
                              zip(spaces, [tmp.get(device).total, tmp.get(device).used, tmp.get(device).free, tmp.get(device).percent])}
        return result

    def convert_to_gb(self, number):
        return float('{:.3f}'.format(number / math.pow(1024, 3)))


disk = DiskInfo()
# print(disk.convert_to_gb(disk.get_devices_space().get("D:\\").free))
#
# print(disk.get_devices_space())
# pprint(disk.get_devices_space().get("D:\\").free)
# pprint(disk.get_devices_space().get("C:\\"))
#
# print([dp.fstype + ":" + dp.device for dp in dps])

print(disk.get_devices_space())