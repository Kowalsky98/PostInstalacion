# main.py

from verificador import verificar_programas
from instalador import instalar_programa
from interfaz import preguntar_instalacion

def main():
    programas_faltantes = verificar_programas()
    if programas_faltantes:
        programa_a_instalar = preguntar_instalacion(programas_faltantes)
        if programa_a_instalar:
            instalar_programa(programa_a_instalar)
    else:
        print("Todos los programas están instalados.")

if __name__ == "__main__":
    main()
