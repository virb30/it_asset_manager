import psutil
import cpuinfo


def get_cpu_info():
    cpu = cpuinfo.get_cpu_info()

    return {
        "cpu_brand": cpu["brand_raw"],
        "cpu_count": psutil.cpu_count(),
        "cpu_freq": psutil.cpu_freq(),
    }
