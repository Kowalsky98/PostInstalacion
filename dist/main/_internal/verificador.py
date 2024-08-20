import os

PROGRAMS = {
    "aida64": {
        "path": r"C:\Program Files (x86)\FinalWire\AIDA64 Extreme\aida64.exe"
    },
    "rustdesk": {
        "path": r"C:\Program Files\RustDesk\rustdesk.exe"
    },
    "Anydesk": {
        "path": r"C:\Program Files (x86)\AnyDesk\Anydesk.exe"
    },
    "Xprinter": {
        "path": r"C:\XINYE POS Printer Driver\XPrinter Driver V7.77\XPrinter Driver V7.77.exe"
    },
    "winrar": {
        "path": r"C:\Program Files\WinRAR\WinRAR.exe"
    },
    "Crystaldisk": {
        "path": r"C:\Program Files\CrystalDiskInfo\DiskInfo64.exe"
    },
    "Edge": {
        "path": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    },
    "Chrome": {
        "path": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    },
    "GanaT_Bolivares": {
        "path": r"C:\GanaT_Bolivares\GanaT.exe"
    },
    "GanaT_Pesos": {
        "path": r"C:\GanaT_Pesos\GanaT.exe"
    },
    "GanaT_Dolares": {
        "path": r"C:\GanaT_Dolares\GanaT.exe"
    },
    "GanaT": {
        "paths": [
            r"C:\%USERPROFILE%\Desktop\GanaT Bolivares.lnk",
            r"C:\%USERPROFILE%\Desktop\GanaT Dolares.lnk",
            r"C:\%USERPROFILE%\Desktop\GanaT Pesos.lnk",
        ]
    },
    "Accesos_Directos": {
        "paths": [
            r"C:\%USERPROFILE%\Desktop\PagoListo.lnk",
            r"C:\%USERPROFILE%\Desktop\Bemovil.lnk",
            r"C:\%USERPROFILE%\Desktop\MisMarcadores.lnk",
            r"C:\%USERPROFILE%\Desktop\SuperGana.lnk",
            r"C:\%USERPROFILE%\Desktop\Payall.lnk",
            r"C:\%USERPROFILE%\Desktop\Visitanos en Gana Loterias.lnk"
        ]
    },
    "KingDeportes": {
        "paths": [
            r"C:\%USERPROFILE%\Desktop\KingDeportes.lnk",
        ]
    }
}

def verificar_programas(programas):
    faltantes = []
    for programa in programas:
        if programa in PROGRAMS:
            info = PROGRAMS[programa]
            if "paths" in info:
                for path in info["paths"]:
                    if not os.path.exists(os.path.expandvars(path)):
                        faltantes.append(programa)
                        break
            else:
                if not os.path.exists(info["path"]):
                    faltantes.append(programa)
    return faltantes
