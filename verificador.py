# modules/verificador.py

import os
import winreg as reg

PROGRAMS = {
    "aida64": {
        "path": "C:\\Program Files (x86)\\FinalWire\\AIDA64 Extreme\\aida64.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\aida64"
    },
    "rustdesk": {
        "path": "C:\\Program Files\\RustDesk\\rustdesk.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\rustdesk"
    },
    "Anydesk":{
        "path": "C:\\Program Files (x86)\AnyDesk\\Anydesk.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\aida64"
    },
    "Xprinter":{
        "path": "C:\\XINYE POS Printer Driver\\XPrinter Driver V7.77\\XPrinter Driver V7.77.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Xprinter"
    },
    "winrar":{
        "path": "C:\\Program Files\\WinRAR\\WinRAR.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Winrar"
    },
    "Crystaldisk":{
        "path": "C:\\Program Files\\CrystalDiskInfo\\DiskInfo64.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\CrystalDisk"
    },
    "Edge":{
        "path": "C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Edge"
    },
    "Chrome":{
        "path": "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe",
        "registry_key": r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Chrome"
    }
}

def verificar_programas():
    faltantes = []
    for programa, info in PROGRAMS.items():
        if not os.path.exists(info["path"]) and not verificar_registro(info["registry_key"]):
            faltantes.append(programa)
    return faltantes

def verificar_registro(registry_key):
    try:
        reg.OpenKey(reg.HKEY_LOCAL_MACHINE, registry_key, 0, reg.KEY_READ)
        return True
    except FileNotFoundError:
        return False
