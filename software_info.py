import winapps


def get_installed_apps():
    return [app for app in winapps.list_installed()]
