import psutil
import cpuinfo
from get_system_info import get_system_info


if __name__ == "__main__":
    system_info = get_system_info()
    print(system_info)

    cpu = cpuinfo.get_cpu_info()
    print(cpu["brand_raw"])

    print(psutil.cpu_count(logical=True))
    print(psutil.disk_partitions(all=True))
    print(psutil.boot_time())
    # print(psutil.net_connections())
    # print(psutil.net_if_addrs())
    print(psutil.virtual_memory())

    print("IT Asset Manager")
