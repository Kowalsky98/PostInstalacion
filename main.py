from verificador import verificar_programas
from instalador import instalar_programa

def main():
    programas_faltantes = verificar_programas()
    while programas_faltantes:
        for programa in programas_faltantes:
            instalar_programa(programa)
        programas_faltantes = verificar_programas()
    print("Todos los programas están instalados.")

if __name__ == "__main__":
    main()
