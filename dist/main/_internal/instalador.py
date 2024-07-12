import subprocess
import shutil
import os

def instalar_programa(programa):
    INSTALL_COMMANDS = {
        "aida64": r"C:\Windows\SysWOW64\Win_Apps\aida64.exe /Silent",
        "rustdesk": r"C:\Windows\SysWOW64\Win_Apps\rustdesk.exe",
        "Anydesk": r"C:\Windows\SysWOW64\Win_Apps\AnyDesk.exe",
        "Xprinter": r"C:\Windows\SysWOW64\Win_Apps\XPrinter.exe /SILENT",
        "winrar": r"C:\Windows\SysWOW64\Win_Apps\winrar.exe",
        "Crystaldisk": r"C:\Windows\SysWOW64\Win_Apps\CrystalDisk.exe /SILENT",
        "Edge": r"C:\Windows\SysWOW64\Win_Apps\MicrosoftEdgeSetup.exe",
        "Chrome": r"C:\Windows\SysWOW64\Win_Apps\Chrome.exe",
        "GanaT": r"cmd /c C:\Windows\SysWOW64\Win_Apps\Taquilla.bat",
        "Accesos_Directos": r"cmd /c C:\Windows\SysWOW64\Win_Apps\AccesosDirectos.bat",
        "Folders": r"cmd /c C:\Windows\SysWOW64\Win_Apps\Videos.bat"
    }
    
    COPY_DIRECTORIES = {
        "GanaT_Bolivares": (r"C:\Windows\SysWOW64\Win_Apps\GanaT_Bolivares", r"C:\GanaT_Bolivares"),
        "GanaT_Pesos": (r"C:\Windows\SysWOW64\Win_Apps\GanaT_Pesos", r"C:\GanaT_Pesos"),
        "GanaT_Dolares": (r"C:\Windows\SysWOW64\Win_Apps\GanaT_Dolares", r"C:\GanaT_Dolares")
    }
    
    if programa in INSTALL_COMMANDS:
        install_command = INSTALL_COMMANDS[programa]
        print(f"Instalando {programa}...")
        result = subprocess.run(install_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"{programa} instalado exitosamente.")
        else:
            print(f"Error al instalar {programa}. Código de salida: {result.returncode}")
            print(result.stderr.decode())
    
    elif programa in COPY_DIRECTORIES:
        source, destination = COPY_DIRECTORIES[programa]
        print(f"Copiando {programa} de {source} a {destination}...")
        try:
            if os.path.exists(destination):
                shutil.rmtree(destination)
            shutil.copytree(source, destination)
            print(f"{programa} copiado exitosamente.")
        except Exception as e:
            print(f"Error al copiar {programa}: {e}")
    
    else:
        print(f"No hay un instalador definido para {programa}")

if __name__ == "__main__":
    # Para probar la instalación de todos los programas y carpetas
    programas = [
        "aida64", "rustdesk", "Anydesk", "Xprinter", "winrar",
        "Crystaldisk", "Edge", "Chrome", "GanaT", "Accesos_Directos",
        "Folders", "GanaT_Bolivares", "GanaT_Pesos", "GanaT_Dolares"
    ]
    for programa in programas:
        instalar_programa(programa)
