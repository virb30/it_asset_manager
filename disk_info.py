import psutil


def get_partition_info(path):

    disk_usage = psutil.disk_usage(path)

    return {
        "path": path,
        "total": disk_usage.total,
        "used": disk_usage.used,
        "free": disk_usage.free,
        "percent": disk_usage.percent,
    }


def get_disk_info():
    partitions = psutil.disk_partitions()

    disks = []

    for partition in partitions:
        if partition.opts != "cdrom":
            disks.append(get_partition_info(partition.mountpoint))

    return disks
