import psutil
import humanfriendly


def get_partition_info(path):

    disk_usage = psutil.disk_usage(path)

    return {
        "path": path,
        "total": humanfriendly.format_size(disk_usage.total, binary=True),
        "used": humanfriendly.format_size(disk_usage.used, binary=True),
        "free": humanfriendly.format_size(disk_usage.free, binary=True),
        "percent": disk_usage.percent,
    }


def get_disk_info():
    partitions = psutil.disk_partitions()

    disks = [
        get_partition_info(partition.mountpoint)
        for partition in partitions
        if partition.opts != "cdrom"
    ]

    return disks
