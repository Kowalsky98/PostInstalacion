# modules/instalador.py

import subprocess
import os

INSTALLERS = {
    "aida64": "C:\\Win_Apps\\aida64.exe",
    "rustdesk": "C:\\Win_Apps\\rustdesk.exe",
    "Anydesk": "C:\\Win_Apps\\AnyDesk.exe",
    "Xprinter": "C:\\Win_Apps\\XPrinter.exe",
    "winrar": "C:\\Win_Apps\\winrar.exe",
    "Crystaldisk": "C:\\Win_Apps\\CrystalDisk.exe",
    "Edga": "C:\\Win_Apps\\MicrosoftEdgeSetup.exe",
    "Chrome": "C:\\Win_Apps\\Chrome.exe"
}

def instalar_programa(programa):
    installer_path = INSTALLERS.get(programa)
    if installer_path and os.path.exists(installer_path):
        try:
            subprocess.run([installer_path, "/S"], check=True)  # Suponiendo que el instalador soporta instalación silenciosa con /S
            print(f"{programa} instalado exitosamente.")
            return True
        except subprocess.CalledProcessError:
            print(f"Error al instalar {programa}.")
            return False
    else:
        print(f"Instalador para {programa} no encontrado.")
        return False
