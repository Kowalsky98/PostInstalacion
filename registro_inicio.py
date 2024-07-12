import os
import shutil

def crear_acceso_directo():
    # Ruta al archivo ejecutable o al acceso directo que deseas iniciar automáticamente
    origen = r'C:\ruta\a\Main.exe'  # Actualiza con la ruta correcta

    # Ruta de la carpeta de inicio del menú de inicio (Start Menu\Programs\Startup)
    destino = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Crear el acceso directo en la carpeta de inicio del menú de inicio
    try:
        shutil.copy(origen, destino)
        print(f"Acceso directo creado en: {destino}")
    except Exception as e:
        print(f"Error al crear el acceso directo: {e}")

if __name__ == "__main__":
    crear_acceso_directo()
