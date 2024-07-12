import subprocess
import shutil
import os

def instalar_programa(programa):
    INSTALL_COMMANDS = {
        "aida64": r"C:\Win_Apps\aida64.exe /Silent",
        "rustdesk": r"C:\Win_Apps\rustdesk.exe",
        "Anydesk": r"C:\Win_Apps\AnyDesk.exe",
        "Xprinter": r"C:\Win_Apps\XPrinter.exe /SILENT",
        "winrar": r"C:\Win_Apps\winrar.exe",
        "Crystaldisk": r"C:\Win_Apps\CrystalDisk.exe /SILENT",
        "Edge": r"C:\Win_Apps\MicrosoftEdgeSetup.exe",
        "Chrome": r"C:\Win_Apps\Chrome.exe",
        "Accesos_Directos": r"cmd /c C:\Win_Apps\AccesosDirectos.bat"
    }
    
    COPY_DIRECTORIES = {
        "GanaT_Bolivares": (r"C:\Win_Apps\GanaT_Bolivares", r"C:\GanaT_Bolivares"),
        "GanaT_Pesos": (r"C:\Win_Apps\GanaT_Pesos", r"C:\GanaT_Pesos"),
        "GanaT_Dolares": (r"C:\Win_Apps\GanaT_Dolares", r"C:\GanaT_Dolares")
    }
    
    if programa in INSTALL_COMMANDS:
        install_command = INSTALL_COMMANDS[programa]
        print(f"Instalando {programa}...")
        result = subprocess.run(install_command, shell=True)
        if result.returncode == 0:
            print(f"{programa} instalado exitosamente.")
        else:
            print(f"Error al instalar {programa}. Código de salida: {result.returncode}")
    
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

