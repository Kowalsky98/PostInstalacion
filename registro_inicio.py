# scripts/registro_inicio.py

import os
import sys
import winreg as reg

def add_to_startup():
    script_path = os.path.abspath(sys.argv[0])
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

    open_key = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open_key, "Win_Apps_Installer", 0, reg.REG_SZ, script_path)
    reg.CloseKey(open_key)

if __name__ == "__main__":
    add_to_startup()
