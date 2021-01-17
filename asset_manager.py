from system_info import get_system_info
from cpu_info import get_cpu_info


def get_asset_info():
    return {"system_info": get_system_info(), "cpu_info": get_cpu_info()}


if __name__ == "__main__":
    print("IT Asset Manager")
    print(get_asset_info())
