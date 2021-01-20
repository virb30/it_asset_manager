from network_info import get_network_info
from disk_info import get_disk_info
from system_info import get_system_info
from cpu_info import get_cpu_info


def get_asset_info():
    asset_info = {
        "system_info": get_system_info(),
        "cpu_info": get_cpu_info(),
        "disk_info": get_disk_info(),
        "network_info": get_network_info(),
    }

    return asset_info


if __name__ == "__main__":
    print("IT Asset Manager")
    print(get_asset_info())
