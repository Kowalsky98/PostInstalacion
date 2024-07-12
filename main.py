from verificador import verificar_programas
from instalador import instalar_programa

def main():
    programas = [
        "aida64", "rustdesk", "Anydesk", "Xprinter", "winrar", 
        "Crystaldisk", "Edge", "Chrome", "Folders", "GanaT", 
        "Accesos_Directos", "GanaT_Bolivares", "GanaT_Pesos", "GanaT_Dolares"
    ]
    faltantes = verificar_programas(programas)
    for programa in faltantes:
        instalar_programa(programa)

if __name__ == "__main__":
    main()
