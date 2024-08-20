import subprocess
import shutil
import os

def instalar_programa(programa):
    INSTALL_COMMANDS = {
        "aida64": r"C:\Windows\SysWOW64\Win_Apps1\aida64.exe /Silent",
        "rustdesk": r"C:\Windows\SysWOW64\Win_Apps1\rustdesk.exe",
        "Anydesk": r"C:\Windows\SysWOW64\Win_Apps1\AnyDesk.exe",
        "Xprinter": r"C:\Windows\SysWOW64\Win_Apps1\XPrinter.exe /SILENT",
        "winrar": r"C:\Windows\SysWOW64\Win_Apps1\winrar.exe",
        "Crystaldisk": r"C:\Windows\SysWOW64\Win_Apps1\CrystalDisk.exe /SILENT",
        "Edge": r"C:\Windows\SysWOW64\Win_Apps1\MicrosoftEdgeSetup.exe",
        "Chrome": r"C:\Windows\SysWOW64\Win_Apps1\Chrome.exe",
        "GanaT": r"cmd /c C:\Windows\SysWOW64\Win_Apps1\Taquilla.bat",
        "Accesos_Directos": r"cmd /c C:\Windows\SysWOW64\Win_Apps1\AccesosDirectos.bat",
        "KingDeportes": r"cmd /c C:\Windows\SysWOW64\Win_Apps1\Serial.bat"
    }
    
    COPY_DIRECTORIES = {
        "GanaT_Bolivares": (r"C:\Windows\SysWOW64\Win_Apps1\GanaT_Bolivares", r"C:\GanaT_Bolivares"),
        "GanaT_Pesos": (r"C:\Windows\SysWOW64\Win_Apps1\GanaT_Pesos", r"C:\GanaT_Pesos"),
        "GanaT_Dolares": (r"C:\Windows\SysWOW64\Win_Apps1\GanaT_Dolares", r"C:\GanaT_Dolares")
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
        "Crystaldisk", "Edge", "Chrome", "GanaT", "Accesos_Directos", "KingDeportes",
        "GanaT_Bolivares", "GanaT_Pesos", "GanaT_Dolares"
    ]
    for programa in programas:
        instalar_programa(programa)
