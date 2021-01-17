import platform


def get_system_info():
    uname = platform.uname()
    return {
        "arch": uname.machine,
        "system": f"{uname.system} {uname.release}",
        "build": uname.version,
        "name": uname.node,
    }
