import psutil


def get_memory_info():

    return {
        "total": psutil.virtual_memory()[0],
    }
